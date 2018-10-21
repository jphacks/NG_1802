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
			#nutrient_list = []
			#print(j)
			result = ingredientReader.getIngredient(j)
            if not "<class 'int'>" == str(type(result)):
				print(result)
