#bootstrap-classifier.py

###
# This file identifies instances of Heterotaxy using the Edit Distance with the Levenshtein algorithm
# It reads in a excel file then calculates the edit distance of each word against a list of keywords,
# which typically cause a patient to be flagged with Heterotaxy. 
# It output an excel file with an additional columnn of to make that these records should be reviewed. 

import sys
import os

new_classpath = os.path.join(os.path.dirname(__file__), "lib/JAVA_CLASSPATH")
if "CLASSPATH" in os.environ:
	new_classpath = os.environ['CLASSPATH'] + ":" + new_classpath

os.environ["CLASSPATH"] = new_classpath

import pandas as pd
import math

from pandas import ExcelFile
from nltk.tokenize.stanford import StanfordTokenizer 
import Levenshtein as leven


MAX_MATCH_EDIT_DISTANCE = 2
HETEROTAXY_KEYWORDS = ["Asplenia", "Heterotaxy", "Polysplenia", "Isomerism", "Dextrocardia"]
def matches_heterotaxy_words(tokens):
  for t in tokens:
    for keyword in HETEROTAXY_KEYWORDS:
      editdist = leven.distance(t.lower(), keyword.lower())
      if editdist <= MAX_MATCH_EDIT_DISTANCE:
        print(f"{col_name}[{index}] - {item} - {t} - [{keyword}] - {editdist}")
        return True
  return False
 
INPUT_FILE = f"list_project.xlsx"
OUTPUT_FILE = f"list_project_processed.xlsx"
print(f"Reading {INPUT_FILE}")
df = pd.read_excel(INPUT_FILE)

match_idx = set()
stk = StanfordTokenizer() #Dependencies in the lib folder, ADD IT TO YOUR `CLASSPATH` env variable
for col_name in ["SPECOTH", "CHD_OTHSP"]:
  for index, item in enumerate(df[col_name]):
    if type(item) is str:
      if(matches_heterotaxy_words(stk.tokenize(item))):
        match_idx.add(index)

print(f"Identified extra {len(match_idx)} cases of heterotaxy.")

for i in match_idx:
  df.at[i, "EDIT_DIST_HETEROTAXY"] = 1
  
df.to_excel(OUTPUT_FILE)


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




