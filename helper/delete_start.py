import os


# plain-PROMISE_clean was called data_set_23 and put with other dataset
def delete_start_func(input_file: str, output_file: str):
    """Function to clean the plain-PROMISE file

        The plain-PROMISE file has, at the beginning of each line, some stuff before colons and sometimes an unnecessary
        space after the colons, this function manage to remove the everything before the colons, the colons and, if it
        is found, also the space after the colons, producing a clean file

        .. note::
            plain-PROMISE_clean was called data_set_23 and put with other dataset, plain-PROMISE_dirty deleted

         :param string input_file: name of the file to clean, the input file
         :param string output_file: name of the file produced, the output file

    """
    f1 = open(input_file, "r")
    f2 = open(output_file, "w")
    dirty_line = f1.readline()
    while dirty_line:
        # delete from colons
        index = dirty_line.find(":")
        # check that colons actually exist
        if index != -1:
            # if after colons there is a space delete it
            if dirty_line[index + 1].isspace():
                index = index + 1
            clean_line = dirty_line[index + 1:]
        else:
            clean_line = dirty_line
        f2.write(clean_line)
        dirty_line = f1.readline()
    f1.close()
    f2.close()


if __name__ == '__main__':
    delete_start_func("plain-PROMISE_dirty.txt", "plain-PROMISE_clean.txt")



