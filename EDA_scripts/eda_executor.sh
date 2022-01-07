#!/bin/zsh
# script to execute eda
# bash doesn't support decimals, use zsh
# to cycle on decimals, in the for cycle put integers and inside the for change it (for example: if i = 2 then i = 0.2)

# echo $(pwd)   # /home/isabella/PycharmProjects/req_paraphrases/helper

cd ../eda_nlp-master/data

# i = file_index
# file format : ../../results/data_set_${i}/results_${i}_EDA_output_${na}_${sr}_${rd}_${ri}_${rs}.txt
# best asset found = 9_0.1_0_0_0

# warning: at least one parameter must be greater than 0

# cycle on all datasets
i=20
python code/augment.py --input=../../results/data_set_${i}/results_${i}_EDA_input.txt --output=../../results/data_set_${i}/EDA_outputs_7/results_${i}_EDA_output_0.1_0_0_0.txt --alpha_sr=0.1 --alpha_rd=0 --alpha_ri=0 --alpha_rs=0

python code/augment.py --input=../../results/plain-PROMISE/results_plain-PROMISE_EDA_input.txt --output=../../results/plain-PROMISE/EDA_outputs/results_plain-PROMISE_EDA_output_9_0.1_0_0_0.txt --alpha_sr=0.1 --alpha_rd=0 --alpha_ri=0 --alpha_rs=0

