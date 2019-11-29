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

### Load BioWordVec
started = time.time()
MODEL_PATH = f"{os.environ['USER_SCRATCH']}/BioWordVec_PubMed_MIMICIII_d200.bin"
print(f"Starting to Load Model")
model = fasttext.load_model(MODEL_PATH)
print(model)
print('loaded in %ds' % (time.time() - started))
print(f"GB MEM Useage: {get_memusage_gb()}")


### Load input File one word per line
with open('biowords.txt') as f:
	read_data = r.read()



def get_dist(word1, word2):
    print(word1, word2)
    v1 = model.get_word_vector(word1)
    v2 = model.get_word_vector(word2)
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


print(get_dist('heterotaxy', 'asplenia'))
print(get_dist('isomerism', 'heterotaxy'))
print(get_dist('isomerism', 'asplenia'))
