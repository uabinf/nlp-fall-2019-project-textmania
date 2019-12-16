# nlp-fall-2019-project-textmania

## Improving Prediction of Single Ventricle Congenital Heart Disease with Free Text

A single ventricle defect is a type of heart defect that a child is born with. It occurs when one of the two pumping chambers in the heart, called ventricles, isn’t large enough or strong enough to work correctly. In some cases, the chamber might be missing a valve.

In the Pediatric Heart Transplant Society (PHTS), single ventricle patients are the largest percentage of congenital heart disease (CHD) patients. These patients are of high clinical interest to surgeons as their risk for graft loss (death or retranspant) after a transplant is high. 

Text fields collected in PHTS can also yield valid data about congenital heart disease. Surgery history is collected for all patients in PHTS and contains information on operations performed on all patients. These surgeries can range from the Norwood, Glenn, and Fontan operations. Dr. James K. Kirklin, a world-renowned cardiac surgeon, will review these text fields and determine if the surgery listed can be classified as a single ventricle surgery, or not. This work is tedious and takes weeks, as these text fields contain thousands of entries. 

Two other text fields where information can be collected on this type of disease is Congenital Heart Disease: Other Specify and Medical History at Listing: Specify. Coordinators are free to enter in free text of their assessment of disease.

Can a machine learning model help predict single ventricle status? Can introducing text fields into a machine learning model help further these predictions? Are medical personnel doomed to scan thousands of text boxes and continue to make decisions instead of focusing on patient care?

The future goal would be to have a machine learning model that could be fed in information on a patient, and the model determine if that patient is single ventricle or not. 

This will be the first machine learning project done on PHTS data! What lessons we learn from this project we can take into future endeavors.


## Running the Project

### Clone from Github

Clone the project from github

```
git clone git@github.com:uabinf/nlp-fall-2019-project-textmania.git
```

### Running  Jupyter Notebooks on rc.uab.edu

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

Other Setup:

* Extra jupyter arguments: `--gres=gpu:1`
* Number of Hours: `3`
* Partition: `pascalnodes`
* Number of CPU: `2`
* Memory per CPU (GB): `16`


### Running python files interactively in a SSH terminal on Cheaha

Change directory to project folder.

```
cd nlp-fall-2019-project-textmania
```

**ON CHEAHA** Make and interactive instance

```
srun --ntasks=1 --cpus-per-task=2 --mem-per-cpu=16384 --time=2:00:00 --partition=express --job-name=NLP_OLEAJ --pty /bin/bash
```

Run the `setup.bash.sh` script. `./setup.bash.sh`

The script does the following.

1. Load the apporiate Python module. 
2. Install `virtualenv`, if needed.
3. Setup a virtualenv folder called `venv` in the directory.
4. Use pip to install the dependencies in the `requirements.txt`
5. Use wget to download BioWordVec model and store in `${USER_SCRATCH}` If `${USER_SCRATCH}` is not defined it will define it at `${HOME}/scratch` and download the file there.

Once this is complete start-up the virtual environment with

```
module load Python/3.6.3-intel-2017a && source venv/bin/activate
```

You should be able to run any `.py` file the command
`python the-file.py`

### Running sbatch files on cheha in a SSH terminal.

In the `sbatch` subdirectory any of the shell scripts should be runnable with `sbatch <filename>`.


## List of Files

* `BrainDump.md` - Random thoughts from the beginning of the project, can be ignored.
* `GOLD STANDARD.xlsx` - Single Ventricle patients that were identified by a human, most not originally flagged as single ventricle. (Filtered based on the `Light Yellow` highlight color on the three end columns produces the list.)
* `Prediction of SV Congenital Heart Disease.ipynb` - Notebook file with the Machine Learning models.
* `README.md` - You are reading it.
* `RESOURCES.txt` - List of Online Resources.
* `SV-Gold-Simplified.xlsx` - The is just a simpilifed list of the Single Ventricle patients that were identified based on text fields by a human, most were not originally flagged as single ventricle.
* `bioword-maker.py` - The Vocabulary builder used for the poster.
* `biowords-to-vects.json` - Mapping of vocabulary to word embedding vectors used in the poster.
* `biowords_txpl_project.txt` - Vocbulary used for the poster.
* `column-classifier.py` - Simple script to identify column types, which are strings / enumerations (categorical) / numeric.
* `docs/*.pdf` - Forms used to collect the data the fields in the excel is identified in the form.
* `heart2.jpg` - Image Mask for WordCloud.
* `heterotaxy/heterotaxy-classifier.py` - Script that identifies patient's not classified as having heterotaxy that should be by using an edit distance algorithm.
* `heterotaxy/list_project.xlsx` - Data from PHTS for use with identifying heterotaxy.
* `heterotaxy/list_project_process.xlsx' - additional heterotaxy patients identified by simple edit distance algorithm.
* `heterotaxy/list_project_updated.xlsx` - list project with additonal patients classified as Heterotaxy using simple heterotaxy classifier and a file with PHI, so can't be on github.
* `lib/JAVA_CLASSPATH` - Dependencies that need to be place in the JAVA_CLASSPATH for Stanford Tokenizer to work.
* `lib/Stopwatch.py` - Simple class for timing how long things take.
* `papers/*.pdf` - Some papers used for researching.
* `play/*` - Just a play area for testing out stuff and messing around.
* `poster_draft_update_SV Status PDF.pdf` - PDF of the poster.
* `poster_draft_update_SV Status PDF.pptx` - Power Point of the poster.
* `requirements.txt` - Requirement for the virtual environment.
* `row2vect.xlsx`- Embedding for text in each row used to produce the results in the poster.
* `sbatch/*.sh` - sbatch shell script for running on cheaha.
* `setup.bash.sh` - Shell script for doing initial setup that allows one to easy run the project.
* `sv-add-gold.py` - Script for adding the single ventricle patients identified by a human with those already marked with checkbox on the form.
* `txpl_project-column-types.csv` - Columns types produced by the column classifier from the `txpl_project.xlsx`.
* `txpl_project.xlsx` - Original dataset of transplant patients.
* `txpl_project_updated.xlsx` - Dataset with SV set to 1 for patient identified as Single Ventricle by a human.
* `txpl_row2vec.py` - Script used for the poster result, that generates a vector from word embedding for each row.
* `vocab-maker.py` - Script that produces different types of vocabularies from the dataset.
* `vocabs/*` - Directory of output from the vocab-maker.py script.

## Division of Work

Devin was the lead on this project. She got the compiled and cleaned the data available from PHTS into an excel format and stripped fields that contained PHI information. Devin also did the work in the Junypter Python Notebook running the data through Machine Learning models, which was the bulk of the project. Tobias contributed by cleaning up the data like adding patient classified as single ventricle by a human and producing the embeddings representing the text from each row of the data and making sure that everything would run correctly on Cheaha.

