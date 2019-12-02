#bioword-maker.py

###
# This file builds a vocabulary from the dataset.
# It moves through each string column in the dataset tokenizes each cell
# And adds each token to a vocublary list and then write this out to a file.

import sys
import os


#Updates Classpath to fix dependency.
new_classpath = os.path.join(os.path.dirname(__file__), "lib/JAVA_CLASSPATH")
if "CLASSPATH" in os.environ:
	new_classpath = os.environ['CLASSPATH'] + ":" + new_classpath

os.environ["CLASSPATH"] = new_classpath

import pandas as pd
import math

from pandas import ExcelFile
from nltk.tokenize.stanford import StanfordTokenizer 
import Levenshtein as leven
from collections import Counter
 
INPUT_FILE = f"{os.path.dirname(os.path.abspath(__file__))}/txpl_project.xlsx"
OUTPUT_FILENAME = "biowords_" + os.path.splitext(os.path.basename(INPUT_FILE))[0] + ".txt"
OUTPUT_FILE = f"{os.path.dirname(os.path.abspath(__file__))}/{OUTPUT_FILENAME}"
print(f"Reading {INPUT_FILE}")
df = pd.read_excel(INPUT_FILE)

COLUMNS_TO_PROCESS = ['SPECOTH', 'CHD_OTHSP', 'SURGERY_HISTORY', 'LSNYHA_T', 'LSRHFCL_T', 'SLINODS']

vocab = Counter()
stk = StanfordTokenizer() #Dependencies in the lib folder, ADD IT TO YOUR `CLASSPATH` env variable
for col_name in COLUMNS_TO_PROCESS:
  print(f"Processing {col_name}...")
  for index, item in enumerate(df[col_name]):
    if type(item) is str:
      vocab.update(stk.tokenize(item))
    if (index % 500) == 0:
      print(f"  at index {index}")


print(f"Vocab Size: {len(vocab)}")

print("\n".join(vocab.keys()))

with open(OUTPUT_FILE, 'w') as f:
	f.write("\n".join(vocab.keys()))


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




