import time
import os

i = 1
j = 0
src_file = open("../results/data_set_" + str(i) + "/results_" + str(i) + ".txt", "r")
dst_file = open("../results/data_set_" + str(i) + "/results_" + str(i) + "_EDA_input.txt", "w")
for src_line in src_file:
    if src_line.startswith("Input_phrase"):
        j = j+1
    if src_line.startswith("("):
        end_index = src_line.find(")")
        dst_line = str(j) + "\t" + src_line[2:end_index-5] + "\n"
        dst_file.write(dst_line)
src_file.close()
dst_file.close()