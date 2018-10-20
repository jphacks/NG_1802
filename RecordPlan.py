import os, sys

sys.path.append('tools/google')

import GoogleSpreadSheetEditor


class RecordPlan:

	def __init__(self, title):
		self.gsse = GoogleSpreadSheetEditor.GoogleSpreadSheetEditor(title, "tools/google/SSGA-3d11131f4a36.json")

	def read_phase(self):
		return self.gsse.readDate_cell("A2")

	def read_all_phase(self):
		return self.gsse.readDate_cell("B2")

	def update_phase(self):
		read = int(self.read_phase())
		if not read == -1:
			self.gsse.writeDate_cell("A2", str(int(self.read_phase()) + 1))
		else:
			print("フェーズがありません。")

	def set_phase(self, full):
		self.gsse.writeDate_cell("B2", full)
		self.gsse.writeDate_cell("A2", 0)

	def reset_phase(self):
		self.gsse.writeDate_cell("A2", -1)
		self.gsse.writeDate_cell("B2", -1)

	def judge_over(self):
		read = int(self.read_phase())
		if read == -1:
			return False

		if int(self.read_all_phase()) >= read:
			return True
		return False


r = RecordPlan("CookingPlan")

print(r.judge_over())
