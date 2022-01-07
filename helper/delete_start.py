import os


# delete start from plain-PROMISE
def delete_start_func():

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



