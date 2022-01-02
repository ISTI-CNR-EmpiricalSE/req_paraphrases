#!/bin/zsh
# bash non supporta decimali, usa zsh

# echo $(pwd)   # /home/isabella/PycharmProjects/req_paraphrases/helper

cd ../eda_nlp-master/data

# i = file_index
# formato file : ../../results/data_set_${i}/results_${i}_EDA_output_${na}_${sr}_${rd}_${ri}_${rs}.txt

# mi da warning che almeno un parametro deve essere maggiore di 0

start_time=$SECONDS

i=20
# for i in {1..22}
#do
  # for na in {5..15..5}
  # do
    for sr in {3..5..2}
    do
      for rd in {3..5..2}
      do
        for ri in {3..5..2}
        do
          for rs in {3..5..2}
          do
            if [ ${sr} == 3 ]; then
              sr=0.3
            fi
            if [ ${rd} == 3 ]; then
              rd=0.3
            fi
            if [ ${ri} == 3 ]; then
              ri=0.3
            fi
            if [ ${rs} == 3 ]; then
              rs=0.3
            fi
            if [ ${sr} == 5 ]; then
              sr=0.5
            fi
            if [ ${rd} == 5 ]; then
              rd=0.5
            fi
            if [ ${ri} == 5 ]; then
              ri=0.5
            fi
            if [ ${rs} == 5 ]; then
              rs=0.5
            fi
            python code/augment.py --input=../../results/data_set_${i}/results_${i}_EDA_input.txt --output=../../results/data_set_${i}/EDA_outputs_3/results_${i}_EDA_output_${na}_${sr}_${rd}_${ri}_${rs}.txt --alpha_sr=${sr} --alpha_rd=${rd} --alpha_ri=${ri} --alpha_rs=${rs}
          done
        done
      done
    done
  # done
# done

elapsed=$(( SECONDS - start_time ))
echo "data_sets from 1 to 22" > ../EDAtime.txt
echo "na : 5 10 15" > ../EDAtime.txt
echo "sr : 0 0.1" > ../EDAtime.txt
echo "rd : 0 0.1" > ../EDAtime.txt
echo "ri : 0 0.1" > ../EDAtime.txt
echo "rs : 0 0.1" > ../EDAtime.txt
echo $elapsed > ../EDAtime.txt
eval "echo Elapsed time: $(date -ud "@$elapsed" +'$((%s/3600/24)) days %H hr %M min %S sec')" > ../EDAtime.txt
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