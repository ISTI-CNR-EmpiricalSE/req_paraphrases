#!/bin/bash

# to install packages that it is possible to install with pip
pip3 install -r requirements.txt

# to install packages that failed with pip
conda install -c intel mkl-service
conda install -c intel mkl_random
conda install -c intel mkl_fft
conda install -c conda-forge bottleneck

# parrot
pip install git+https://github.com/PrithivirajDamodaran/Parrot_Paraphraser.git

# spacy models
sudo python -m spacy download en
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md
