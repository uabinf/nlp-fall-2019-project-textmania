import math
import os
import time

import fasttext
import psutil


def get_memusage_gb():
    as_bytes = psutil.Process(os.getpid()).memory_info().rss
    return as_bytes / (1024 ** 3)


started = time.time()
MODEL_PATH = "../ignore-dir/BioWordVec_PubMed_MIMICIII_d200.bin"
path = '/home/mpenkov/data/' + 'BioWordVec_PubMed_MIMICIII_d200.bin'
print(f"Starting to Load Model")
model = fasttext.load_model(MODEL_PATH)
print(model)
print('loaded in %ds' % (time.time() - started))
print(get_memusage_gb())


def get_dist(word1, word2):
    print(word1, word2)
    v1 = model.get_word_vector(word1)
    v2 = model.get_word_vector(word2)
    err = ((v1 - v2) ** 2).sum()
    return math.sqrt(err)


print(get_dist('biomedical', 'medical'))
print(get_dist('biomedical', 'biological'))
print(get_dist('biomedical', 'biomechanical'))