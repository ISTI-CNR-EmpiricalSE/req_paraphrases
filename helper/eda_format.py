import time
import os


# put the data_set files in a format that is ok for Eda
def eda_format_func():

    # data_sets_n
    for i in range(1,23):
        j = 0
        src_file = open("../results/data_set_" + str(i) + "/results_1.txt", "r")
        dst_file = open("../results/data_set_" + str(i) + "/results_" + str(i) + "_EDA_input.txt", "w")
        for src_line in src_file:
            if "Input_phrase" in src_line:
                j = j+1
            if src_line.startswith("("):
                end_index = src_line.find(")")
                dst_line = str(j) + "\t" + src_line[2:end_index-5] + "\n"
                dst_file.write(dst_line)
        src_file.close()
        dst_file.close()

    # plain-PROMISE
    j = 0
    src_file = open("../results/plain-PROMISE/results_1.txt", "r")
    dst_file = open("../results/plain-PROMISE/results_plain-PROMISE_EDA_input.txt", "w")
    for src_line in src_file:
        if "Input_phrase" in src_line:
            j = j + 1
        if src_line.startswith("("):
            end_index = src_line.find(")")
            dst_line = str(j) + "\t" + src_line[2:end_index - 5] + "\n"
            dst_file.write(dst_line)
    src_file.close()
    dst_file.close()


if __name__ == '__main__':
    eda_format_func()
