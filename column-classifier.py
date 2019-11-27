#play-columns.py
import pandas as pd
import math

from pandas import ExcelFile
from nltk.tokenize.stanford import StanfordTokenizer 
import Levenshtein as leven
import sys
import os

class ColumnClassifier:
	bool_set_1 = {0.0, 1.0}
	bool_set_2 = {0, 1}
	
	def _print_unique_vals(self, col_name, col_class, u_vals):
		print(f"{col_name} [{col_class}]")
		output = '  '
		for i, val in enumerate(u_vals):
			if i > 8:
				output += "..."
				break
		
			output += '"' + str(val) + '"' + " "
		print(output)
	
	def classify_col(self, df, col):
		col_class = 'UNK'
		u_vals = [x for x in df[col].unique() if (str(x) != 'nan')]
		
		
		if self.test_bool(u_vals):
			col_class = "BOOL"
		elif self.test_enum(u_vals):
			col_class = "ENUM"
			# if self.test_str(u_vals):
			# 	col_class = "ENUM-STR" #
			# elif self.test_int(u_vals):
			# 	col_class = "ENUM-INT"
			# elif self.test_float(u_vals):
			# 	col_class = "ENUM-FLOAT"
		elif self.test_str(u_vals):
			col_class = "STR"
		elif self.test_int(u_vals):
			col_class = "INT"
		elif self.test_float(u_vals):
			col_class = "FLOAT"
		
		self._print_unique_vals(col, col_class, u_vals)
		
		return col_class
		
	
	def test_bool(self, vals):
		if len(vals) > 2:
			return False
		elif len(vals) == 2:
			val_set = set(vals)
			return len(val_set.difference(self.bool_set_1)) == 0 or len(val_set.difference(self.bool_set_2)) == 0
		elif len(vals) == 1:
			return vals[0] == 0.0 or vals[0] == 1.0 or vals[0] == 1 or vals[0] == 0
		else:
			return False
	
	def test_enum(self, vals):
		return len(vals) <= 8 #Just eyeballing the data this seems like a good cut-off
	
	def test_str(self, vals):
		for v in vals:
			if not isinstance(v, str):
				return False
		return True
	
	def test_int(self, vals):
		for v in vals:
			if round(v) != v:
				return False
		return True	

	def test_float(self, vals):
		for v in vals:
			if not isinstance(v, float):
				return False
		return True


excel_filepath = f"{os.path.dirname(os.path.abspath(__file__))}/list_project_updated.xlsx"
excel_filepath = f"{os.path.dirname(os.path.abspath(__file__))}/txpl_project.xlsx"

output_filename = os.path.splitext(os.path.basename(excel_filepath))[0] + "-column-types.csv"
output_filepath = f"{os.path.dirname(os.path.abspath(__file__))}/{output_filename}"

df = pd.read_excel(excel_filepath)

col_to_class = {}
class_to_col = {}
col_classifier = ColumnClassifier()
for col in df.columns:
	# info = (col, ) #column name, type
	col_class = col_classifier.classify_col(df, col)
	
	col_to_class[col] = col_class
	if col_class not in class_to_col:
		class_to_col[col_class] = []
	class_to_col[col_class].append(col)
	
for key in class_to_col:
	print(key)
	print(class_to_col[key])
	print('\n')

df_prep = []
for key in col_to_class:
	df_prep.append([key, col_to_class[key]])

df = pd.DataFrame(df_prep, columns=["Column", "Type"])


df.to_csv(f"./{output_filename}", index=None, header=True)

