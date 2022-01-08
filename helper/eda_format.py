import time
import os


# put the data_set files in a format that is ok for Eda
def eda_format_func():
    """Function that put the input file in the right format to be processed by EDA
        The right format is that each line must be like this: label\tsentence
        The produced file is put in the directory results, inside the directory of the relative dataset
        Format of the input file: results_file_index.txt (which was the output of parrot_test_func)
        Format of the output file: results_data_set_index_EDA_input.txt
    """

    # since the time that it takes to do it it's very small, every time it process all the files
    for i in range(1, 24):
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


if __name__ == '__main__':
    eda_format_func()
