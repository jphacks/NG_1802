#! /usr/bin/env python3

#料理を探す関数
#引数 
# cook: 料理名（オムライス、カレーなど）
#戻り値
# 料理がある場合は、料理のパスと中のファイルのリスト

#材料を返す関数
#引数 
# cook: 料理名（オムライス、カレーなど）
#戻り値
# material.dicの中身をリストで返す

#レシピを返す関数
#引数 
# cook: 料理名（オムライス、カレーなど）
#戻り値
# recipe.csvの中身をリストで返す

import sys, os
import csv

class find_cook():
    cook_name = {
            'ぎょーざ': "gyoza", 
            'おむらいす': "omuraisu",
            'ちゃーはん': "tya-han", 
            'ぱすた': "pasta", 
            'かれー': "curry",
            'みーとすぱげってぃ': "meatspagetti",
            'はんばーぐ': "hanba-gu",
            'おこのみやき': "okonomiyaki",
            'にくじゃが': "nikujaga",
            'はるまき': "harumaki",
        }
    def __init__(self, cook):
        self.dirName = os.getcwd() + "/src/cook/"+ self.cook_name[cook]
        self.cook_dir, self.cook_material, self.cook_recipe = self.find_cook(cook)

    def find_cook(self, cook):
        print(self.dirName)
        if os.path.exists(self.dirName):
            #print ("find directory "+ dirName)
            for curDir, dirs, files in os.walk(self.dirName):
                print('===================')
                print("現在のディレクトリ: " , curDir)
                print("内包するディレクトリ:" , dirs)
                print("内包するファイル: " , files)
            files.sort()
            material = files[0]
            recipe = files[1]
            return self.dirName, material, recipe
        else:
            print("not found "+ self.cook_name[cook])
            return self.dirName, "noFile", "noRecipe"

    def get_material(self):
        material = []
        if self.cook_material is not "noFile":
            with open(self.dirName +"/"+self.cook_material, 'r') as file:
                materials = file.readlines()
            for m in materials:
                material.append(eval(m))
            return material

    def get_recipe(self):
        if self.cook_recipe is not "noRecipe":
            r = []
            csv_file = open(self.dirName +"/"+self.cook_recipe, "r", errors="", newline="\n" )
            recipes = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\n", quotechar='"', skipinitialspace=True)
            for f in recipes:
                r.append(f)
            return r