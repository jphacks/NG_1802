'''
作成:みぐりー
コンストラクタ引数:共有設定されたスプレットシートのタイトル

'''

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSpreadSheetEditor:

	def __init__(self, title, json):
		scope = ['https://spreadsheets.google.com/feeds',
				 'https://www.googleapis.com/auth/drive']

		# json_dir = 'SSGA-3d11131f4a36.json'

		credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)
		gc = gspread.authorize(credentials)
		self.wks = gc.open(title).sheet1

	def writeDate_cell(self, cell, date):
		self.wks.update_acell(str(cell), str(date))

	def writeData_line(self, line, list):
		cell_row = self.wks.range(str(line))
		for i in range(len(list)):
			cell_row[i].value = list[i]
		self.wks.update_cells(cell_row)

	def writeData_same(self, row, data):
		cell_row = self.wks.range(row + str(1) + ":" + row + str(1000))
		for i in range(0, 1000):
			cell_row[i].value = data
		self.wks.update_cells(cell_row)

	def readDate_cell(self, cell):
		return self.wks.acell(str(cell)).value

	def readDate_row(self, row):
		return self.wks.row_values(row)

	def readDate_col(self, col):
		return self.wks.col_values(col)

	def readDate_all(self):
		return self.wks.get_all_values()
