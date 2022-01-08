import sys


def help_message():
    print("You have to choose between one of these three assets:")
    print("number of arguments =")
    print("0                        - default configuration, do all datasets from n1 included to n23 exluded")
    print("False n1,n5...           - not a cycle, but singles dataset n1 and n5")
    print("True n1,n5               - a cycle that goes from n2 included and n5 excluded")


def parrot_test_func():

    # I want to have the possibility to insert the dataset on which operate from command line
    # on the contrary, I identified the best asset of parameters, so they are fixed

    # INSTRUCTIONS:
    # number of arguments =
    # 0                         - default configuration, do all datasets from n1 included to n23 exluded
    # False n1,n5...            - not a cycle, but singles dataset n1 and n5
    # True n1,n5                - a cycle that goes from n2 included and n5 excluded

    start_index = None
    end_index = None
    data_set_list = []

    if len(sys.argv)-1 == 0:
        start_index = 1
        end_index = 24
    elif sys.argv[1] != "True" and sys.argv[1] != "False":
        help_message()
        return
    else:
        if sys.argv[1] == "True":
            if len(sys.argv)-2 != 2:
                help_message()
                return
            else:
                start_index = int(sys.argv[2])
                end_index = int(sys.argv[3])
        elif sys.argv[1] == "False":
            if len(sys.argv)-2 == 0:
                help_message()
                return
            else:
                # name false 1 5 3
                data_sets_list = []
                for i in range(2, len(sys.argv)):
                    data_set_list.append(int(sys.argv[i]))

    data_set_index_list = []
    if start_index is not None and end_index is not None:
        data_set_index_list = range(start_index, end_index)
        print("doing data_sets from " + str(start_index) + " included to " + str(end_index) + " excluded")
    elif data_set_list is not None:
        data_set_index_list = data_set_list
        print("doing data_sets")
        print(data_set_index_list)
    else:
        help_message()
        return


if __name__ == '__main__':
    parrot_test_func()
