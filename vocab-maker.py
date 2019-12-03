#vocab-maker.py

###
# This file builds vocabularies from the dataset.
# It moves through each string columns in the dataset and builds a vocabularies with different methods.
# It write these vocabs to different files.

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
from nltk.tokenize import WhitespaceTokenizer
from nltk.corpus import stopwords
import Levenshtein as leven

class VocabBuilder():

    def __init__(self, tokenizer, stopwords=set(), token_transformer=None):
        self.tokenizer = tokenizer
        
        self.token_transformer = token_transformer
        
        if self.token_transformer:
            self.stopwords = set(map(lambda stopword: self.token_transformer(stopword), stopwords))
        else:
            self.stopwords = stopwords

        self.vocab = set()
    
    
    def build_with_text(self, text):
        tokens = self.tokenizer.tokenize(text)
        
        if self.token_transformer:
            trans_tokens = map(lambda token: self.token_transformer(token), tokens)
        else:
            trans_tokens = tokens
            
        final_tokens = filter(lambda token: token not in self.stopwords, trans_tokens)
        
        for item in final_tokens:
            self.vocab.add(item)
 
INPUT_FILE = f"{os.path.dirname(os.path.abspath(__file__))}/txpl_project.xlsx"
OUTPUT_PREFIX = 'vocab_'
OUTPUT_POSTFIX = os.path.splitext(os.path.basename(INPUT_FILE))[0] + ".txt"

print(f"Reading {INPUT_FILE}")
df = pd.read_excel(INPUT_FILE)

COLUMNS_TO_PROCESS = ['SPECOTH', 'CHD_OTHSP', 'SURGERY_HISTORY']

# Set up various vocab builders

vocab_builders = {
    "stanford" : VocabBuilder(StanfordTokenizer()),
    "stanford_stop" : VocabBuilder(StanfordTokenizer(), set(stopwords.words('english'))),
    "stanford_stop_lower" : VocabBuilder(StanfordTokenizer(), set(stopwords.words('english')), lambda x: x.lower()),

    "whitespace" : VocabBuilder(WhitespaceTokenizer()),
    "whitespace_stop" : VocabBuilder(WhitespaceTokenizer(), set(stopwords.words('english'))),
    "whitespace_stop_lower" : VocabBuilder(WhitespaceTokenizer(), set(stopwords.words('english')), lambda x: x.lower())
}
  
for builder_key in vocab_builders:
    print(f"Building Vocab for {builder_key}...")
    builder = vocab_builders[builder_key]
    for col_name in COLUMNS_TO_PROCESS:
        print(f"Processing {col_name}...")
        for index, item in enumerate(df[col_name]):
            if isinstance(item, str):
                builder.build_with_text(item)
            if (index % 500) == 0:
                print(f"  at index {index}")
    
    with open(f"{OUTPUT_PREFIX}_{builder_key}_{OUTPUT_POSTFIX}") as f:
        f.write("\n".join(builder.vocab))

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




