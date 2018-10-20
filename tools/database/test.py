##このコードは複数ある料理から適切な栄養素を抜き出すスクリプト
#tabインデント
import IngredientReader

ingredientReader = IngredientReader.IngredientReader("./data/database.csv")
cook_list = []
with open('../../src/cook/omuraisu/material.dic', 'r') as file:
	for line in file:
		cook_list.append(line)
		# print(line)
	for i in cook_list:
		nutrient_list = []
		print("#############")
		#栄養値の初期化
		sum_haiki = 0
		sum_kcal = 0
		#ナトリウム
		sum_na = 0
		#食塩相当量の合計量
		sum_solt = 0
		for j in eval(i):
			#print(j)
			result = ingredientReader.getIngredient(j)
			print(result)

			if not "<class 'int'>" == str(type(result)):

				print(result["廃棄"])
				sum_haiki += result["廃棄"]
				sum_kcal += result["エネルギー（kcal）"]
				sum_na += result["ナトリウム"]
				sum_solt += result["食塩相当量"]
		print("廃棄の合計値:",sum_haiki)
		print("kcalの合計値:",sum_kcal)
		print("ナトリウムの合計値:",sum_na)
		print("食塩相当量の合計値:",sum_solt)
			#nutrient_list.append(result)
			#print(type(result))

	# for i in cook_list:
	# print(" ")
	# print(i)