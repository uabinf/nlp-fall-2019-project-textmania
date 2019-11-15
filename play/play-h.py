#play-h.py
import pandas as pd

from pandas import ExcelFile
from nltk.tokenize.stanford import StanfordTokenizer 
import Levenshtein as leven

df = pd.read_excel("list_dak.xlsx")
stk = StanfordTokenizer()

# print("Column Names:")
# print(df.columns)

# chd_summary = df["CHD_SUMMARY"]
# chd_summary = chd_summary.to_list()
#
# with open('chd_summary.txt', 'w') as fh:
#   for listitem in chd_summary:
#     fh.write('%s\n' % listitem)

# print("CHD_SUMMARY:")
# for item in chd_summary:
#   if type(item) is str:
#     if 'taxy' in item.lower():
#       print(item)
#     elif 'iso' in item.lower():
#       print(item)
#   elif type(item) is not float:
#     print(f"{type(item)} - {item}")
    
print("SPECOTH")
specoth = df["SPECOTH"]
specoth = specoth.to_list()

specoth = [x for x in specoth if type(x) is str]

print(f"Specoth Count: {len(specoth)}")
# print("\n".join(specoth))

for index, item in enumerate(specoth):
  if 'taxy' in item:
    print(f"SPEC: {index} - {item}")
    tokens = stk.tokenize(item)
    for t in tokens:
      print(f"EDIT DISTANCE: {leven.distance(item.lower(), 'HETROTAXY'.lower())}")

print("\n-----------\n")
chd_othsp = [item for item in df["CHD_OTHSP"].to_list() if type(item) is str]
print(f"Chd_Othsp Count: {len(chd_othsp)}")
# print("\n".join(chd_othsp))

for index, item in enumerate(chd_othsp):
  if 'taxy' in item:
    print(f"CHD: {index} - {item}")





