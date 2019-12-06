#vocab-to-vects.py

###
# This file uses a fastText word embedding model to create word embeddings for each token in a vocabulary.
# The vocabulary should be a file with one token per-line and begin with `vocab_`.
# The will be found in the vocabs directory off the current working directory
# The output will be a json dictionary which tokens as keys and word embeddings as values
# The output will be written to the same directory as the input but the filename will begin with 'vect_' instead.

import math
import os
import time
import glob

import fasttext
import psutil
import numpy as np
import json

def get_memusage_gb():
    as_bytes = psutil.Process(os.getpid()).memory_info().rss
    return as_bytes / (1024 ** 3)


def create_input_output_file_pairs(vocab_dir):
    input_files = list(map(lambda fname: os.path.basename(fname), glob.glob(f'{vocab_dir}/vocab_*')))
    output_files = list(map(lambda fname: fname.replace('vocab_', 'vects_'), input_files))

    input_files = list(map(lambda fname: os.path.join(vocab_dir, fname), input_files))
    output_files = list(map(lambda fname: os.path.join(vocab_dir, fname), output_files))

    inout_files = list(zip(input_files, output_files))
    
    return inout_files
    

####
# Load the word vec model.
#

started = time.time()
MODEL_PATH = f"{os.environ['USER_SCRATCH']}/BioWordVec_PubMed_MIMICIII_d200.bin"
print(f"Starting to Load Model")
model = fasttext.load_model(MODEL_PATH)
print(model)
print('loaded in %ds' % (time.time() - started))
print(f"GB MEM Useage: {get_memusage_gb()}")

###
# Now start processing each file one by one

inout_files = create_input_output_file_pairs('vocabs')

for input_file, output_file in inout_files:
    
    print("Processing Vocab {}".format(input_file))
    
    vocab = []
    with open(input_file) as f:
        vocab = f.read().splitlines()
        
    word_to_vect = {}
    for index, word in enumerate(vocab):
        if (index + 1) % 500: 
            print("  Processing index {}".format(index))
        vect = model.get_word_vector(word)
        word_to_vect[word] = vect.tolist()
   
    with open(output_file, 'w') as f:
        json.dump(word_to_vect, f)
      
    print("  Wrote Mapping to {}".format(output_file))

print("!!!Completed Processing all Vocab Files")