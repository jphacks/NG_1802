''''
作成:みぐりー
コンストラクタ引数:栄養素のサンプル表のcsvパス

◆getIngredient
 引数:材料名
 返り値:栄養素のリスト
'''


class IngredientReader:

	def __init__(self, csv):
		self.list = []
		csv_date = open(str(csv), "r")

		for line in csv_date:
			self.list.append(line)

	def calcAverage(self, list):
		if len(list) == 0:
			return 0
		result = {}
		for key in list[0]:
			temp = 0.0
			for data in list:
				temp += float(data[key])
			result.setdefault(key, temp / len(list))
		return result

	def getIngredient(self, food_name):
		result = []
		for i in range(19, len(self.list)):
			if food_name in self.list[i].split(",")[3]:
				ingredient = {}
				for j in range(4, len(self.list[i].split(","))):
					ingredient.setdefault(self.list[15].split(",")[j],
										  float(
											  self.list[i].split(",")[j].replace('(', '').replace(')', '').replace('-',
																												   '0').replace(
												  'Tr', '0')))
				result.append(ingredient)

		return self.calcAverage(result)