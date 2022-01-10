import os


# plain-PROMISE_clean was called data_set_23 and put with other dataset
def delete_start_and_point_func(input_file: str, output_file: str):
    """it takes the output of delete_start (data_set_23) and break the phrases if there is a point
            producing output file (data_set_24)

         :param string input_file: name of the file to clean, the input file
         :param string output_file: name of the file produced, the output file

    """
    f1 = open(input_file, "r")
    f2 = open(output_file, "w")
    line = f1.readline()
    # substitute all points with \n
    while line:
        line = line.replace(".", "\n")
        # if you have double \n you want to remove one
        line = line.replace("\n"+"\n", "\n")
        f2.write(line)
        line = f1.readline()

    f1.close()
    f2.close()


if __name__ == '__main__':
    delete_start_and_point_func("../data_sets/data_set_23.txt", "../data_sets/data_set_24.txt")



