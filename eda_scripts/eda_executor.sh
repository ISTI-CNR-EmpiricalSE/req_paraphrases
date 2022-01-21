#!/bin/zsh
# script to execute eda with the best asset
# it executes eda on all files
# bash doesn't support decimals, use zsh
# to cycle on decimals, in the for cycle put integers and inside the for change it (for example: if i = 2 then i = 0.2)
# # warning: at least one parameter must be greater than
cd ../eda_nlp-master/data

# i = file_index
# file format : ../../results/data_set_${i}/results_${i}_EDA_output_${na}_${sr}_${rd}_${ri}_${rs}.txt
# best asset found = 9_0.1_0_0_0

# cycle on all datasets
for i in {1..1}
do
  python code/augment.py --input=../../results/data_set_${i}/results_${i}_EDA_input.txt --output=../../results/data_set_${i}/EDA_outputs/results_${i}_EDA_output_9_0.5_0_0_0.txt --num_aug=9 --alpha_sr=0.5 --alpha_rd=0 --alpha_ri=0 --alpha_rs=0
done
