import Cookpad

PATH = "../../src/cook/okonomiyaki/"

recipe_file = open(PATH + "recipe.csv", "w")

material_file = open(PATH + "material.dic", "w")

links = Cookpad.getLink("お好み焼き")

for l in links:
	print(l)
	material = Cookpad.getMaterial(l)
	if str(material) == '{}':
		continue
	recipe = Cookpad.getRecipe(l)
	flow = ''
	for i in recipe:
		flow = flow + recipe[i] + ","
	flow = flow[:-1].replace("\u3000", "") + "\n"
	recipe_file.write(flow)
	material_file.write(str(material) + "\n")

'''

material_sample = open("material", "r")

list = []

for i in material_sample:
	list.append(eval(i))

print(list[2])
'''