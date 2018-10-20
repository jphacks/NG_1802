import random
import sys, os

sys.path.append('../../tools/google/')

import GoogleSpreadSheetEditor

gsse = GoogleSpreadSheetEditor.GoogleSpreadSheetEditor("PersonalNutritionList_A",
													   "../../tools/google/SSGA-3d11131f4a36.json")
path = 'data/Standard_Data.csv'

standard = open(path, "r")


def get_malnutrition():
	return random.choice()


standard_dic = {}

for e in standard:
	standard_dic.setdefault(e.split(",")[0], e.split(",")[1])

personal_list = gsse.readDate_all()

for index in range(1, len(personal_list)):
	temp = 0
	for line in personal_list:
		temp += line[index]

	

# print(gsse.readDate_all()[1])
