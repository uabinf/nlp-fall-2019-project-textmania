#play-glob.py


import os
import glob


def create_input_output_file_pairs(vocab_dir):
    input_files = list(map(lambda fname: os.path.basename(fname), glob.glob(f'{vocab_dir}/vocab_*')))
    output_files = list(map(lambda fname: fname.replace('vocab_', 'vects_'), input_files))

    input_files = list(map(lambda fname: os.path.join(vocab_dir, fname), input_files))
    output_files = list(map(lambda fname: os.path.join(vocab_dir, fname), output_files))

    inout_files = list(zip(input_files, output_files))
    
    return inout_files
    
inout_files = create_input_output_file_pairs('vocabs')

for input_file, output_file in inout_files:
    print(f"input: {input_file}\noutput: {output_file}")