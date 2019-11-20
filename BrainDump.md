
## Steps

* Define your problem
    * What is the problem? - Binary Classification of Heterotaxy or not.
    * Why does the problem need to be solved? - Save human time
    * How would I solve the problem? - See Below
* Prepare the data
    * Label the data.
    * Split Data into Train, Dev, Validate
* Spot check various algorithms
    * Edit-Distance
    * Use Document Similarity - Vectorize Document and attempt to create two clusters based on those number (Topic Model approach / SVD)?
    * Logistic Regression
    * Bert with Task Based fine-tuning?
* Tune well-performing algorithms
* Present results

## Questions

* How do we represent the document as a vector?
    * Since there are a bunch of fields with a mix of structured and unstructed data.
    * Do we convert the structured data back to words using the forms? (Example: CHD_ASPL 1 -> "Asplenia or Right Isomerism" 0 -> "") [Kinda would work better with NLP....]
* Do we have enough data for Neural Networks?
* Are BERT embeddings going to work with Medical Terminology.
* Can we use a Medical Knowledge Graph to connect words associated with Heterotaxy?


## Info

Mimic Database has no instances of Heterotaxy.
Situs Inversus is the closest condition in the database to Heterotaxy.


