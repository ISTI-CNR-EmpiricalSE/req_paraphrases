#!/usr/bin/bash
cd eda_nlp-master/data
python code/augment.py --input=../../results/data_set_1/results_1_EDA_input.txt --output=../../results/data_set_1/EDA_outputs/results_1_EDA_output.txt
python code/augment.py --input=../../results/data_set_1/results_1_EDA_input.txt --output=../../results/data_set_1/EDA_outputs/results_1_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0