echo $(pwd)   # /home/isabella/PycharmProjects/req_paraphrases/helper

cd ../eda_nlp-master/data

for (( i=1; i<23; i++ ))
do
   python code/augment.py --input=../../results/data_set_${i}/results_${i}_EDA_input.txt --output=../../results/data_set_${i}/results_${i}_EDA_output.txt --num_aug=16 --alpha_sr=0.1 --alpha_rd=0.0 --alpha_ri=0.0 --alpha_rs=0.0
done

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