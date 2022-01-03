#!/bin/zsh
cd ../eda_nlp-master/data
i=20
python code/augment.py --input=../../results/data_set_${i}/results_${i}_EDA_input.txt --output=../../results/data_set_${i}/EDA_outputs_7/results_${i}_EDA_output_0.2_0_0_0.txt --alpha_sr=0.2 --alpha_rd=0 --alpha_ri=0 --alpha_rs=0
python code/augment.py --input=../../results/data_set_${i}/results_${i}_EDA_input.txt --output=../../results/data_set_${i}/EDA_outputs_7/results_${i}_EDA_output_0_0.2_0_0.txt --alpha_sr=0 --alpha_rd=0.2 --alpha_ri=0 --alpha_rs=0
python code/augment.py --input=../../results/data_set_${i}/results_${i}_EDA_input.txt --output=../../results/data_set_${i}/EDA_outputs_7/results_${i}_EDA_output_0_0_0.2_0.txt --alpha_sr=0 --alpha_rd=0 --alpha_ri=0.2 --alpha_rs=0
python code/augment.py --input=../../results/data_set_${i}/results_${i}_EDA_input.txt --output=../../results/data_set_${i}/EDA_outputs_7/results_${i}_EDA_output_0_0_0_0.2.txt --alpha_sr=0 --alpha_rd=0 --alpha_ri=0 --alpha_rs=0.2