import random

path = 'data/Standard_Data.csv'

standard = open(path, "r")


def get_malnutrition():
	return random.choice()


standard_dic = {}

for e in standard:
	standard_dic.setdefault(e.split(",")[0], e.split(",")[1])

print(standard_dic)