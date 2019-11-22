#play-h.py
import pandas as pd
import math

from pandas import ExcelFile
from nltk.tokenize.stanford import StanfordTokenizer 
import Levenshtein as leven
import sys
import os

keywords = ["Asplenia", "Heterotaxy", "Polysplenia", "Isomerism", "Dextrocardia"]
keygroups = [["Unbalanced", "AV", "Canal"]]
def matches_heterotaxy_words(tokens):
  for t in tokens:
    for keyword in keywords:
      editdist = leven.distance(t.lower(), keyword.lower())
      if editdist < 3:
        print(f"{col_name}[{index}] - {item} - {t} - [{keyword}] - {editdist}")
        return True
  return False
  
print(os.path.abspath(__file__))
df = pd.read_excel(f"{os.path.dirname(os.path.abspath(__file__))}/docs/list_project.xlsx")



match_idx = set()
stk = StanfordTokenizer() #Dependencies in the lib folder, ADD IT TO YOUR `CLASSPATH` env variable
for col_name in ["SPECOTH", "CHD_OTHSP"]:
  for index, item in enumerate(df[col_name]):
    if type(item) is str:
      if(matches_heterotaxy_words(stk.tokenize(item))):
        match_idx.add(index)

print(f"COUNT: {len(match_idx)}")

for i in match_idx:
  df.at[i, "HETEROTAXY"] = 1
  
df.to_excel(f"{os.path.dirname(os.path.abspath(__file__))}/docs/list_project_updated.xlsx")


# print(f"Specoth Count: {len(specoth)}")
#
# for keyword in keywords:
#   for index, item in enumerate(specoth):
#     tokens = stk.tokenize(item)
#     for t in tokens:
#       editdist = leven.distance(t.lower(), 'heterotaxy'.lower())
#       if editdist < 4:
#         print(f"{index} - {item} - {t}")
#         print(f"EDIT DISTANCE: {editdist}")
#
# print("\n-----------\n")
# print("CHD_OTHSP")
# chd_othsp = [item for item in df["CHD_OTHSP"].to_list() if type(item) is str]
# print(f"Chd_Othsp Count: {len(chd_othsp)}")
# # print("\n".join(chd_othsp))
#
# for index, item in enumerate(chd_othsp):
#   tokens = stk.tokenize(item)
#   for t in tokens:
#     editdist = leven.distance(t.lower(), 'heterotaxy'.lower())
#     if editdist < 4:
#       print(f"{index} - {item} - {t}")
#       print(f"EDIT DISTANCE: {editdist}")




