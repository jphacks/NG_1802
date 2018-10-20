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

	def update_phase(self):
		read = int(self.read_phase())
		if not read == -1:
			self.gsse.writeDate_cell("A2", str(int(self.read_phase()) + 1))
		else:
			print("フェーズがありません。")

	def set_phase(self, recipe_list):
		for i in range(len(recipe_list)):
			self.gsse.writeDate_cell("B" + str(i + 1), recipe_list[i])

		self.gsse.writeDate_cell("A2", 0)

	def reset_phase(self):
		self.gsse.writeDate_cell("A2", -1)


r = RecordPlan("CookingPlan")

print(r.test())
