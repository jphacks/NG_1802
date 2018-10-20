import find_cook
import random


def selectRecipe(cook_name):
    fc = find_cook.find_cook(cook_name)
    fc_material = fc.get_material()
    fc_recipe = fc.get_recipe()

    if (fc_material is not None ) and (fc_recipe is not None):
        cook_num = random.randrange(len(fc_material))
        fc_m_dic = fc_material[cook_num]
        fc_r_csv = fc_recipe[cook_num]
        #print(fc_m_dic)
        #print(fc_r_csv)
        dic2list = []
        for key in fc_m_dic:
            d2l = '・'+key+','+fc_m_dic[key]
            dic2list.append(d2l)
        #print(dic2list)
        d2l = '\n'.join(dic2list)
        print(d2l)
        return d2l, fc_r_csv

#selectRecipe("おむらいす")
#selectRecipe("ぱすた")
#selectRecipe("はんばーぐ")
#selectRecipe("おこのみやき")