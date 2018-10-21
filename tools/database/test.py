##このコードは複数ある料理から適切な栄養素を抜き出すスクリプト
#tabインデント
import IngredientReader

ingredientReader = IngredientReader.IngredientReader("./data/database.csv")
cook_list = []
with open('../../src/cook/omuraisu/material.dic', 'r') as file:
	cook_list = file.readlines()
	key_list = []
	for cook_dict in cook_list:
		cook_dict = eval(cook_dict)
		key_ = list(cook_dict.keys())
		key_list.append(key_)

	print(key_list)

	for i in key_list:
		for j in i:
			nutrient_list = []
			print("#############")
			#print(j)
			result = ingredientReader.getIngredient(j)
			print(result.keys())
			print(result.values())

stops
		#if not "<class 'int'>" == str(type(result)):

			#print(result["廃棄"])
		#	sum_haiki += result["廃棄"]
		#	sum_kcal += result["エネルギー（kcal）"]
		#	sum_na += result["ナトリウム"]
		#	sum_solt += result["食塩相当量"]

		#print("廃棄の合計値:",sum_haiki)
		#print("kcalの合計値:",sum_kcal)
		#print("ナトリウムの合計値:",sum_na)
		#print("食塩相当量の合計値:",sum_solt)
			#nutrient_list.append(result)
			#print(type(result))

	# for i in cook_list:
	# print(" ")
	# print(i)