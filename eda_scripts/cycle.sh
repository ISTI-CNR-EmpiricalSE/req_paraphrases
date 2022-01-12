#!/bin/zsh
# script to execute eda
# it executes eda on all files
# bash doesn't support decimals, use zsh
# to cycle on decimals, in the for cycle put integers and inside the for change it (for example: if i = 2 then i = 0.2)
# # warning: at least one parameter must be greater than
cd ../eda_nlp-master/data

# i = file_index
# file format : ../../results/data_set_${i}/results_${i}_EDA_output_${na}_${sr}_${rd}_${ri}_${rs}.txt
# best asset found = 9_0.1_0_0_0

# cycle on all datasets
for i in {23..24}
do
  for na in {5..15..5}:
  do
    for sr in {1..9..4}:
    do
      for rd in {1..9..4}:
      do
        for ri in {1..9..4}:
        do
          for rs in {1..9..4}:
          do
            if [[ ${sr} == 1 ]]
            then
              sr=0.1
            elif [[ ${sr} == 5 ]]
            then
              sr=0.5
            elif [[ ${sr} == 9 ]]
            then
              sr=0.9
            fi
            if [[ ${rd} == 1 ]]
            then
              rd=0.1
            elif [[ ${rd} == 5 ]]
            then
              rd=0.5
            elif [[ ${rd} == 9 ]]
            then
              rd=0.9
            fi
            if [[ ${ri} == 1 ]]
            then
              ri=0.1
            elif [[ ${ri} == 5 ]]
            then
              ri=0.5
            elif [[ ${ri} == 9 ]]
            then
              ri=0.9
            fi
            if [[ ${rs} == 1 ]]
            then
              rs=0.1
            elif [[ ${rs} == 5 ]]
            then
              rs=0.5
            elif [[ ${rs} == 9 ]]
            then
              rs=0.9
            fi
            python code/augment.py --input=../../results/data_set_${i}/results_${i}_EDA_input.txt --output=../../results/data_set_${i}/EDA_outputs/results_${i}_EDA_output_9_0.1_0_0_0.txt --num_aug=${na} --alpha_sr=${sr} --alpha_rd=${rd} --alpha_ri=${ri} --alpha_rs=${rs}
          done
        done
      done
    done
  done
done

