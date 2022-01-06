#!/bin/zsh
# bash non supporta decimali, usa zsh

# echo $(pwd)   # /home/isabella/PycharmProjects/req_paraphrases/helper

cd ../eda_nlp-master/data

# i = file_index
# formato file : ../../results/data_set_${i}/results_${i}_EDA_output_${na}_${sr}_${rd}_${ri}_${rs}.txt

# mi da warning che almeno un parametro deve essere maggiore di 0

# start_time=$SECONDS

python code/augment.py --input=../../results/plain-PROMISE/results_plain-PROMISE_EDA_input.txt --output=../../results/plain-PROMISE/EDA_outputs/results_plain-PROMISE_EDA_output_9_0.1_0_0_0.txt --alpha_sr=0.1 --alpha_rd=0 --alpha_ri=0 --alpha_rs=0


# elapsed=$(( SECONDS - start_time ))
# echo "data_sets from 1 to 22" > ../EDAtime.txt
# echo "na : 5 10 15" > ../EDAtime.txt
# echo "sr : 0 0.1" > ../EDAtime.txt
# echo "rd : 0 0.1" > ../EDAtime.txt
# echo "ri : 0 0.1" > ../EDAtime.txt
# echo "rs : 0 0.1" > ../EDAtime.txt
# echo $elapsed > ../EDAtime.txt
# eval "echo Elapsed time: $(date -ud "@$elapsed" +'$((%s/3600/24)) days %H hr %M min %S sec')" > ../EDAtime.txt
# python code/augment.py --input=results_1_EDA_input.txt --output=../../results/data_set_1/results_1_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_2_EDA_input.txt --output=results_2_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_3_EDA_input.txt --output=results_3_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_4_EDA_input.txt --output=results_4_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_5_EDA_input.txt --output=results_5_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_6_EDA_input.txt --output=results_6_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_7_EDA_input.txt --output=results_7_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_8_EDA_input.txt --output=results_8_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_9_EDA_input.txt --output=results_9_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_10_EDA_input.txt --output=results_10_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_11_EDA_input.txt --output=results_11_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_12_EDA_input.txt --output=results_12_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_13_EDA_input.txt --output=results_13_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_14_EDA_input.txt --output=results_14_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_15_EDA_input.txt --output=results_15_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_16_EDA_input.txt --output=results_16_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_17_EDA_input.txt --output=results_17_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_18_EDA_input.txt --output=results_18_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_19_EDA_input.txt --output=results_19_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_20_EDA_input.txt --output=results_20_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_21_EDA_input.txt --output=results_21_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
# python code/augment.py --input=results_22_EDA_input.txt --output=results_22_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0