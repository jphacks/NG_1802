import os, sys

sys.path.append('tools/google')

import GoogleSpreadSheetEditor


class RecordPlan:

	def __init__(self, title):
		self.gsse = GoogleSpreadSheetEditor.GoogleSpreadSheetEditor(title, "tools/google/SSGA-3d11131f4a36.json")

	def read_phase(self):
		return self.gsse.readDate_cell("A2")

	def read_all_phase(self):
		return self.gsse.readDate_cell("A4")

	def pop_phase(self):
		self.update_phase()
		read = self.read_phase()

		if read == "-1":
			return 'null'

		recipe = self.gsse.readDate_cell("B" + str(read))

		if recipe == "-1":
			return 'null'

		return recipe

	def update_phase(self):
		read = int(self.read_phase())
		if not read == -1:
			self.gsse.writeDate_cell("A2", str(int(self.read_phase()) + 1))
		else:
			print("フェーズがありません。")

	def set_phase(self, recipe_list):
		i = 1
		for l in recipe_list:
			self.gsse.writeDate_cell("B" + str(i), l)
			i += 1

		self.gsse.writeDate_cell("B" + str(i), -1)
		self.gsse.writeDate_cell("A2", 0)

	def reset_phase(self):
		self.gsse.writeDate_cell("A2", -1)
		self.gsse.writeDate_cell("A4", -1)
		self.gsse.writeData_same("B", "")


#r = RecordPlan("CookingPlan")

#l = ["qwer", "asdfadsf", "adsfadsf", "asdfsafpjpewfjwq"]

#r.set_phase(l)
