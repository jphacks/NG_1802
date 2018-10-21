import random
import sys, os

sys.path.append('../../tools/google/')

import GoogleSpreadSheetEditor


class Malnutrition:
	def __init__(self, standard_path, personal_title):
		self.gsse = GoogleSpreadSheetEditor.GoogleSpreadSheetEditor(personal_title,
																	"../../tools/google/SSGA-3d11131f4a36.json")

		self.standard = open(standard_path, "r")

	def get_malnutrition_random(self):
		return random.choice()

	def get_malnutrition(self):
		standard_dic = {}
		for e in self.standard:
			standard_dic.setdefault(e.split(",")[0], e.split(",")[1])

		personal_list = self.gsse.readDate_all()  # googleから読み取り

		max_data = 0
		max_element = ''
		for col in range(1, len(personal_list[0])):
			element = personal_list[0][col]

			if element in standard_dic:
				temp = 0.0

				for index in range(1, len(personal_list)):
					temp += float(personal_list[index][col])
				ave = temp / len(personal_list)  # 個人の栄養値の平均

				temp2 = float(standard_dic[element]) - ave  # 基準数値との差

				if temp2 > 0:
					if max_data < temp2:
						max_data = temp2
						max_element = element

		return max_element, max_data


m = Malnutrition("data/Standard_Data.csv", "PersonalNutritionList_A")
print(m.get_malnutrition())
