#sv-classifier.py

# This file identifies instances of Single Ventricle using the Levenshtein.
# Believe a simple tool like this could aid medical workers in finding the majority of cases in unstructured data.

import sys
import os

import pandas as pd
import math
import re

from pandas import ExcelFile


GOLD_STANDARD = f"SV-GoldStandard-Filtered.xlsx"
INPUT_FILE = f"txpl_project.xlsx"
OUTPUT_FILE = f"txpl_project_updated.xlsx"
print(f"Reading {GOLD_STANDARD}")
gold_df = pd.read_excel(GOLD_STANDARD)

print(f"Single Ventricle (SV) Gold Standard Shape: {gold_df.shape}")

print(f"Reading {INPUT_FILE}")
txpl_df = pd.read_excel(INPUT_FILE)

sv_gold = txpl_df['PATIENT_ID'].apply(lambda x: 1 if x in pd.to_numeric(gold_df['PTID']).unique() else 0)


def print_intersecting_patient_ids():
  """
  Prints the patient ids for gold records already flagged. Used for double-checking work.
  """
  for i, v in enumerate(zip(sv_gold, txpl_df['SV_GROUP'], txpl_df['PATIENT_ID'])):
    if v[0] == 1 and v[1] == 1:
      print(f"SV_GOLD & SV_GROUP == 1 for PATIENT_ID: {v[2]}")
# print_intersecting_patient_ids()

print(f"SV_GOLD Count: {sv_gold.sum()}" )
print(f"SV_GROUP Count: {txpl_df['SV_GROUP'].sum()}")

sv_combined = sv_gold | txpl_df['SV_GROUP']
sv_intersect = sv_gold & txpl_df['SV_GROUP']

print(f"Insection Count: {sv_intersect.sum()}")
print(f"Combined Count: {sv_combined.sum()}")

txpl_df['SV_GROUP'] = sv_combined
txpl_df.to_excel(OUTPUT_FILE, index=False)
print(f"Wrote Updated txpl_df to {OUTPUT_FILE}")






# match_idx = set()
# stk = StanfordTokenizer() #Dependencies in the lib folder, ADD IT TO YOUR `CLASSPATH` env variable
# for col_name in ["SPECOTH", "CHD_OTHSP"]:
#   for index, item in enumerate(df[col_name]):
#     if type(item) is str:
#       if(matches_heterotaxy_words(stk.tokenize(item))):
#         match_idx.add(index)
#
# print(f"Identified extra {len(match_idx)} cases of heterotaxy.")
#
# for i in match_idx:
#   df.at[i, "HETEROTAXY"] = 1
#
# df.to_excel(OUTPUT_FILE)