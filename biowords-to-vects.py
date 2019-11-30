import math
import os
import time

import fasttext
import psutil
import numpy as np
import json

def get_memusage_gb():
    as_bytes = psutil.Process(os.getpid()).memory_info().rss
    return as_bytes / (1024 ** 3)


# Load the word vec model.
started = time.time()
MODEL_PATH = f"{os.environ['USER_SCRATCH']}/BioWordVec_PubMed_MIMICIII_d200.bin"
print(f"Starting to Load Model")
model = fasttext.load_model(MODEL_PATH)
print(model)
print('loaded in %ds' % (time.time() - started))
print(f"GB MEM Useage: {get_memusage_gb()}")


# Load input File one word per line
with open('biowords_txpl_project.txt') as f:
	read_data = f.read()

words = read_data.splitlines()

word_to_vect = {}
for word in words:
   vect = model.get_word_vector(word)
   word_to_vect[word] = vect.tolist()
   
with open('biowords-to-vects.json', 'w') as f:
  json.dump(word_to_vect, f)
  


