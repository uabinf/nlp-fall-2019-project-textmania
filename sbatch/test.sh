#!/bin/bash
#
#SBATCH --job-name=nlp_oleaj_batch
#SBATCH --error=error.txt
#SBATCH --output=output.txt
#SBATCH --ntasks=1
#SBATCH --partition=short
#SBATCH --time=04:00:00
#SBATCH --mem-per-cpu=16GB
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=$USER@uab.edu

###
# Error Function
function fail {
    printf '%s\n' "$1" >&2  ## Send message to stderr. Exclude >&2 if you don't want it that way.
    exit "${2-1}"  ## Return a code specified by $2 or 1 by default.
}


cd $HOME/uab-proj

###
# Setup Interactive Shell
###
if [ ! -f ${USER_SCRATCH}/BioWordVec_PubMed_MIMICIII_d200.bin ]; then
    cp ${USER_DATA}/BioWordVec_PubMed_MIMICIII_d200.bin ${USER_SCRATCH}/BioWordVec_PubMed_MIMICIII_d200.bin
fi

echo "Loading Python Module..."
module load Python/3.6.3-intel-2017a

echo "Activating Environment..."
if [ -d venv ]; then
    source venv/bin/activate
else
  fail "Python Environment Directory not found (venv)."
fi

echo "Running bioword-maker.py..."
python -u bioword-maker.py

echo "Running biowords-to-vects.py..."
python -u biowords-to-vects.py 

###
# CLEAN UP COMMAND
###

echo "Cleaning up User Scratch"
if [ -f ${USER_SCRATCH}/BioWordVec_PubMed_MIMICIII_d200.bin ]; then
    if [ ! -f ${USER_DATA}/BioWordVec_PubMed_MIMICIII_d200.bin ]; then
        mv ${USER_SCRATCH}/BioWordVec_PubMed_MIMICIII_d200.bin ${USER_DATA}/BioWordVec_PubMed_MIMICIII_d200.bin
    else
        rm ${USER_SCRATCH}/BioWordVec_PubMed_MIMICIII_d200.bin
    fi
fi 