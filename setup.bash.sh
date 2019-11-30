#!/bin/bash

# Assume on Cheaha if we are ssh'd into something
if [ ${#SSH_CONNECTION} -gt 0 ]; then
  module load Python/3.6.3-intel-2017a
fi

# Install virtualenv
pip install virtualenv 

# Setup virtualenv
if [ ! -d ./venv ]; then
  virtualenv venv
fi

source ./venv/bin/activate

pip install -r requirements.txt

# Download the BioWordVec Model

if [ ! -d  "$USER_SCRATCH" ]; then
  export USER_SCRATCH="${HOME}/scratch"
  mkdir "$USER_SCRATCH"
fi

if [ ! -f "$USER_SCRATCH/BioWordVec_PubMed_MIMICIII_d200.bin" ]; then
  wget -P "$USER_SCRATCH" https://ftp.ncbi.nlm.nih.gov/pub/lu/Suppl/BioSentVec/BioWordVec_PubMed_MIMICIII_d200.bin
fi