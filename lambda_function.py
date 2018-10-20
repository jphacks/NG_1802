import requests
import sys
import RecordPlan as rp
sys.path.append("src/kernel/")
import RecipeSelecter as res


def lambda_handler(event, context):
    cook_plan = rp.RecordPlan("CookingPlan")
    name = "こんにちは"
    should_end_session = False
    #ggs = gs.GoogleSpreadSheetEditor("PersonalNutritionList_A")
    #print(ggs.readDate_cell("A1"))
    if event['request']['type'] == "LaunchRequest":
        name = "なんのレシピが知りたいですか"
        
    elif event['request']['type'] == "IntentRequest":
        
        intent = event['request']['intent']
        intent_name = intent['name']
        if intent_name == "cook":
            code = intent["slots"]["content"]["resolutions"]["resolutionsPerAuthority"][0]["status"]["code"]
            
            if code == "ER_SUCCESS_MATCH":
                item = intent['slots']["content"]['value']
                name = "レシピを送りました"
                material, recipe = res.selectRecipe(item)
                material = "\n" + material
                line(material)
                line(recipe_sort(recipe))
                
                cook_plan.reset_phase()
                cook_plan.set_phase(recipe)
                
                should_end_session = True
            else:
                name = "そんなレシピは知りません"
                
        elif intent_name == "next":
            code = intent["slots"]["next_key"]["resolutions"]["resolutionsPerAuthority"][0]["status"]["code"]
            if code == "ER_SUCCESS_MATCH":
                if cook_plan.judge_over():
                    name = "ちゃんと覚えろ"
                else:
                    cook_plan.reset_phase()
                    name = "問題が起きました"
                should_end_session = True
                
            else:
                name =  "日本語を喋ろう"
                
        elif intent_name == "finish":
            code = intent["slots"]["word"]["resolutions"]["resolutionsPerAuthority"][0]["status"]["code"]
            if code == "ER_SUCCESS_MATCH":
                name = "とまります"
                should_end_session = True
            else:
                name = "そんな言葉は知りません"
        else:
             name = "そんな言葉は知りません"
    else:
        name = "問題があります"
        
    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': name
            },
            'shouldEndSession': should_end_session
        }
    }

    return response
    
def line(message):
    line_notify_token = 'MGK4ZeCveXYJxNcp7HGrIxW7RsT9ycu4KDX3vxerNdl'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)

def recipe_sort(material_list):
    material = "\n" + "1:" + material_list[0] + "\n" + "\n"
    for i in range(1, len(material_list)):
        material += str(i+1) + ":" + material_list[i]
        if not i == len(material_list) - 1:
            material += "\n" + "\n"

    return material
