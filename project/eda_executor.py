import eda_nlp.data.code.augment as augment_function
import time


def eda_executor_func(filename: str, parameters_list: list, output_dict: dict):
    """
    Function that executes Eda, calling the function gen_eda with the right parameters
    :param filename: name of the input file
    :param parameters_list: list of parameters configured by the user
    :param output_dict: dictionary that will contain the outputs {input_1: [output_1.1, output_1.2...], input_2...}
    :return:
    """

    alpha_sr = parameters_list[0]
    print("alpha_sr " + str(alpha_sr))  # configurable (default: 0.1)
    alpha_ri = parameters_list[1]
    print("alpha_ri " + str(alpha_ri))  # configurable (default: 0)
    alpha_rs = parameters_list[2]
    print("alpha_rs " + str(alpha_rs))  # configurable (default: 0)
    alpha_rd = parameters_list[3]
    print("alpha_rd " + str(alpha_rd))  # configurable (default: 0)
    num_aug = parameters_list[4]
    print("num_aug " + str(num_aug))  # configurable (default: 9)

    # call gen_eda
    augment_function.gen_eda(filename, output_dict, alpha_sr, alpha_ri, alpha_rs, alpha_rd, num_aug)


'''
if __name__ == "__main__":
    dict = {}
    tic = time.perf_counter()
    eda_executor_func("../finto_data_set.txt", [0.1,0,0,0,9], dict)
    toc = time.perf_counter()
    print(f"{toc - tic:0.4f} seconds")
'''
