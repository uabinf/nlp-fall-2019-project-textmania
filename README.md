# nlp-fall-2019-project-textmania


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