#txpl_row2vec.py


import sys
import os
import json
import time

import pandas as pd
import numpy as np
from pandas import ExcelFile

###
# JAVA_CLASSPATH Setup
###
def update_java_classpath_for_standford_tokenizer():
  """
  Updates java classpath to include the stanford tokenizer, must run from root of the project.
  """
  new_classpath = os.path.join(os.path.dirname(__file__), "lib/JAVA_CLASSPATH")
  
  if not os.path.exists(new_classpath):
    print >> sys.stderr, f"Unable to locate directory with standford tokenizer: {new_classpath}."
    exit(1)
  
  if "CLASSPATH" in os.environ:
  	new_classpath = os.environ['CLASSPATH'] + ":" + new_classpath

  os.environ["CLASSPATH"] = new_classpath
  
update_java_classpath_for_standford_tokenizer()


from nltk.tokenize.stanford import StanfordTokenizer


###
# Loads the Word to Vect Mapping into Dict from JSON file
#
lookup_dict = None
with open('biowords-to-vects.json') as json_file:
  lookup_dict = json.load(json_file)


if not lookup_dict:
  print >> sys.stderr, 'BioWord Vect Lookup Dictionary not loaded.'
  exit(1)

###
# Read Transplant Excel File
#
INPUT_FILE = 'txpl_project_updated.xlsx'
print(f"Reading {INPUT_FILE}")

txpl_df = pd.read_excel(INPUT_FILE)

print(f"Transplant Data Shape: {txpl_df.shape}")
print(f"Transplant Data Columns:\n{txpl_df.columns}")

###
# Process each row.
#

stk = StanfordTokenizer()
empty_vect = np.zeros(200)
def transform_text_to_vect(text):
  """
  Transforms a string into a vector by tokenizing with the StandfordTokenizer
  then looking up the BioWordVec embedding for the from a pre-computed dataset.
  then taking the centroid of the vectors.
  
  :param text: String to turn into a vector
  
  :returns: np.array of length 200, which is the centroid of embeddings of each token.
  """
  if not isinstance(text, str):
    return empty_vect
    
  tokens = stk.tokenize(text)

  vects = np.array(list(map(lambda token: np.array(lookup_dict[token]), tokens)))
  return np.mean(vects, axis=0)

TEXT_COLS = ['CHD_OTHSP','SPECOTH','SURGERY_HISTORY']

for colname in TEXT_COLS:
  txpl_df[colname].fillna('', inplace=True)
  
row2vect = []
start_time = time.time()
for index, row in txpl_df.iterrows():
  
  row_text = ''
  for colname in TEXT_COLS: 
    if len(txpl_df[colname]) > 0:
      row_text = ' '.join(txpl_df[colname])
  
  row_vect = transform_text_to_vect(row_text)

  new_row = [row['PATIENT_ID']] + row_vect.tolist()
  row2vect.append(new_row)
  
  if (index % 100) == 0:
    print(f"Processed: {index+1} rows {round(100.0*(index/txpl_df.shape[0]), 2)}% ({round(time.time() - start_time)} secs)")

row2vect_cols = ['PATIENT_ID'] + list(map(lambda x: f"WordVec{x}", range(200)))
row2vect = pd.DataFrame(row2vect, columns=row2vect_cols)

row2vect.to_excel('row2vect.xlsx', index=False)

  




