# nlp-fall-2019-project-textmania

## Prediction of Single Ventricle Congenital Heart Disease from Free Text

A single ventricle defect is a type of heart defect that a child is born with. It occurs when one of the two pumping chambers in the heart, called ventricles, isn’t large enough or strong enough to work correctly. In some cases, the chamber might be missing a valve.

In the Pediatric Heart Transplant Society, single ventricle patients are the largest percentage of congenital heart disease (CHD) patients. These patients are of high clinical interest to surgeons as their risk for graft loss (death or retranspant) after a transplant is high. 

Text fields collected in PHTS can also yield valid data about congenital heart disease. Surgery history is collected for all patients in PHTS and contains information on operations performed on all patients. These surgeries can range from Fontan, Glenn, and Norwood operations. Dr. Kirklin will review these text fields and determine if the surgery listed can be classified as a single ventricle surgery, or not. This work is tedious and takes weeks, as these text fields contain thousands of entries.

Can a machine learning model help predict single ventricle status? Can introducing text fields into a machine learning help further these predictions? 

The future goal would be to have a machine learning model that could be fed in information on a patient, and the model determine if that patient is single ventricle or not.

## Running  Jupyter Notebooks on rc.uab.edu

For running Jupyter Notebooks on rc.uab.edu, please use the following settings.

Environment Setup:
```
module load cuda92/toolkit/9.2.88
module load cuda10.0/toolkit
module load CUDA/9.2.88-GCC-7.3.0-2.30
module load Anaconda3/5.3.1
pip install --user xlrd
pip install --user xgboost
pip install --user wordcloud
pip install --user Pillow
```

Extra jupyter arguments: `--gres=gpu:1`
Number of Hours: `3`
Partition: `pascalnodes`
Number of CPU: `2`
Memory per CPU (GB): `16`


## Setup 

Clone the project from github

```
git clone git@github.com:uabinf/nlp-fall-2019-project-textmania.git
```

Change directory to project folder.

```
cd nlp-fall-2019-project-textmania
```
**ON CHEAHA** Make and interactive instance

```
srun --ntasks=1 --cpus-per-task=2 --mem-per-cpu=16384 --time=2:00:00 --partition=express --job-name=NLP_OLEAJ --pty /bin/bash
```

Run the `setup.bash.sh` script. 
1. This will load the required module if on Cheaha.
2. Install `virtualenv`, if needed.
3. Setup a virtualenv folder called `venv` in the directory.
4. Use pip to install the dependencies in the `requirements.txt`
5. Use wget to download BioWordVec model and store in `${USER_SCRATCH}` If `${USER_SCRATCH}` is not defined it will define it at `${HOME}/scratch` and download the file there.

```
./setup.bash.sh
```

Once this is complete start-up the virtual environment with

```
module load Python/3.6.3-intel-2017a && source venv/bin/activate
```

You should be able to run any `.py` file the command
`python the-file.py`
