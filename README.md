# [重要] 作業ブランチは基本developで行う

## masterへのpush、ダメ！絶対！！！

## submasterをmasterの代わりとして使用する

# [重要] commitメッセージの書き方

[${commit種別}] (${issue No.}) やったこと

## commit種別

- fix：バグ修正
- add：新規（ファイル）機能追加
- update：機能修正（バグではない）
- remove：削除（ファイル）

## 例　（issue NO.なし）

`[add] Hogehoge.pyを追加`

(意味) Hogehoge.pyを追加したよ

## 例　（issue NO.あり）

`[fix] #18 Hogehoge.pyを修正`

(意味) issue18通りにHogehoge.pyのバグを修正したよ

## ディレクトリツリー

```
├── LICENSE
├── README.md
├── RecordPlan.py
├── docs
│   └── _config.yml
├── image.png
├── lambda_function.py
├── src
│   ├── cook
│   │   ├── gyoza
│   │   │   ├── material.dic
│   │   │   └── recipe.csv
│   │   ├── harumaki
│   │   │   ├── material.dic
│   │   │   └── recipe.csv
│   │   ├── nikujaga
│   │   │   ├── material.dic
│   │   │   └── recipe.csv
│   │   ├── okonomiyaki
│   │   │   ├── material.dic
│   │   │   └── recipe.csv
│   │   ├── omuraisu
│   │   │   ├── material.dic
│   │   │   └── recipe.csv
│   │   └── tya-han
│   │       ├── material.dic
│   │       └── recipe.csv
│   └── kernel
│       ├── Malnutrition.py
│       ├── RecipeSelecter.py
│       ├── data
│       │   └── Standard_Data.csv
│       └── find_cook.py
├── test
│   ├── README.md
│   └── find_cook_test.py
└── tools
    ├── database
    │   ├── Cookpad.py
    │   ├── IngredientReader.py
    │   ├── __pycache__
    │   │   └── IngredientReader.cpython-36.pyc
    │   ├── createDB.py
    │   ├── data
    │   │   └── database.csv
    │   └── test.py
    ├── google
    │   └── GoogleSpreadSheetEditor.py
    └── main_tset.py
```
