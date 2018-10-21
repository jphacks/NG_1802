##このコードは複数ある料理から適切な栄養素を抜き出すスクリプト
#tabインデント
import IngredientReader
import numpy as np

ingredientReader = IngredientReader.IngredientReader("./data/database.csv")
cook_list = []
key_list = []
with open('../../src/cook/omuraisu/material.dic', 'r') as file:
	cook_list = file.readlines()
<<<<<<< HEAD
	for cook_dict in cook_list:
		cook_dict = eval(cook_dict)
		key_ = list(cook_dict.keys())  #１つのメニューを完成させるための材料
		key_list.append(key_)

for menu in key_list:  #複数メニューから１つ選ぶ
	nutrient_key_list = []
	nutrient_value_list = []
	for material in menu:
		nutrient_list = []
		result = ingredientReader.getIngredient(material)
		if not "<class 'int'>" == str(type(result)):
			n_key = list(result.keys())
			nutrient_key_list.append(n_key)
			#print("##", len(n_key))
			n_val = list(result.values())
			nutrient_value_list.append(n_val)
			#print("##", len(n_val))
		else:
			n_key = [0]*63
			nutrient_key_list.append(n_key)
			n_val = [0]*63
			nutrient_value_list.append(n_val)

	list_2_array = np.array(nutrient_value_list)
	list_2_array = np.vstack(list_2_array)
	l2a = list_2_array.T
	for i in range(len(l2a)):
		l2a[i] = np.sum(l2a[i])
	#print(l2a.T)
	l2a = l2a.T
	for l in l2a:
		l = list(l)
		print(l)
		print(type(l))
		print("####")

l2a = list(l2a)
print(type(l2a))
for l in l2a:
	with open('../../src/cook/omuraisu/nutrient.txt', 'w') as file:
			file.writelines(str(l))
=======
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
>>>>>>> 9efe54f8329decca8c3761ae4ee02b7562fc0cd0

stops
