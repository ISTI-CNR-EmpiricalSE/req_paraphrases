import os


# plain-PROMISE_clean was called data_set_23 and put with other dataset
def delete_start_func():
    """Function to clean the plain-PROMISE file

        The plain-PROMISE file has, at the beginning of each line, some stuff before colons and sometimes an unnecessary
        space after the colons, this function manage to remove the everything before the colons, the colons and, if it
        is found, also the space after the colons, producing a clean file
        Format of the input file: plain-PROMISE_dirty.txt
        Format of the output file: plain-PROMISE_clean.txt
        .. note::
            plain-PROMISE_clean was called data_set_23 and put with other dataset, plain-PROMISE_dirty deleted

    """

    f1 = open("plain-PROMISE_dirty.txt", "r")
    f2 = open("plain-PROMISE_clean.txt", "w")
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
    delete_start_func()



