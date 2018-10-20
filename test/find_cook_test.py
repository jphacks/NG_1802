#! /usr/bin/env python3
#encoding : utf-8

#料理を探す関数を作成
#引数 
# cook: 料理名（オムライス、カレーなど）

import sys, os
import shutil

def finder_test():
    cook = ["gyoza", "omurisu", "tya-han"]
    dirName = "./src/cook/"

    for c in cook:
        dirName = "./src/cook/" + c
        if not os.path.exists(dirName):
            print ("make test directory "+ dirName)
            os.makedirs(dirName)
            with open(dirName+"/material.dic", 'w') as f:
              f.write('test')
            with open(dirName+"/recipe.csv", 'w') as f:
              f.write('test')


def find_cook(cook):
    dirName = "./src/cook/"+ cook

    if os.path.exists(dirName):
        print ("find directory "+ dirName)
        for curDir, dirs, files in os.walk(dirName):
            print('===================')
            print("現在のディレクトリ: " , curDir)
            print("内包するディレクトリ:" , dirs)
            print("内包するファイル: " , files)
        print("exit "+dirName+"\n")
    else:
        print("not found "+ cook)

d = "./src/"

finder_test()
cook = {'ぎょうざ': "gyoza", 
        'おむらいす': "omurisu",
        'ちゃーはん': "tya-han", 
        'ぱすた': "pasta", 
        'かれー': "curry"
       }
for c in cook:
    find_cook(cook[c])

print("delete test dir")
shutil.rmtree(d)