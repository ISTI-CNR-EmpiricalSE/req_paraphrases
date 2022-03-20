# req_paraphrases

## Installation

Create a **Virtual Environment** and activate it.


To install all **Required Libraries** run the following command:
```
./installation.sh
```

Open the **Python's interactive shell** by running `python` and then type the following commands:
```
>>> import nltk
>>> nltk.download('stopwords')
>>> nltk.download('punkt')
>>> nltk.download('averaged_perceptron_tagger')
>>> nltk.download('universal_tagset')
>>> nltk.download('wordnet')
```
Exit the shell by running `quit()`


Eventually, download the **Model** that can be found to this 
[link](http://doi.org/10.5281/zenodo.1199620) into the directory **project**