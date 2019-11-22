#play-h.py
import pandas as pd
import math

from pandas import ExcelFile
from nltk.tokenize.stanford import StanfordTokenizer 
import Levenshtein as leven
import sys
import os

print(os.path.abspath(__file__))
df = pd.read_excel(f"{os.path.dirname(os.path.abspath(__file__))}/ignore-dir/list_dak.xlsx")
stk = StanfordTokenizer() #Dependencies in the lib folder, ADD IT TO YOUR `CLASSPATH` env variable
keywords = ["Asplenia", "Heterotaxy", "Polysplenia", "Isomerism", "Dextrocardia"]
keygroups = [["Unbalanced", "AV", "Canal"]]

flagged_idx = set()
for col_name in ["SPECOTH", "CHD_OTHSP"]:
  for index, item in enumerate(df[col_name]):
    if type(item) is str:
      # print(f"{index}: {item}")
      tokens = stk.tokenize(item)
      for t in tokens:
        for keyword in keywords:
          editdist = leven.distance(t.lower(), keyword.lower())
          if editdist < 3:
            flagged_idx.add(index)
            print(f"{col_name}[{index}] - {item} - {t} - [{keyword}] - {editdist}")

print(f"COUNT: {len(flagged_idx)}")

for i in flagged_idx:
  print(i)

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




