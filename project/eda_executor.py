import eda_nlp as augment_function


def eda_executor_func(filename, parameters_list, output_dict):
    alpha_sr = parameters_list[0]
    print("alpha_sr " + str(alpha_sr))
    alpha_ri = parameters_list[1]
    print("alpha_ri " + str(alpha_ri))
    alpha_rs = parameters_list[2]
    print("alpha_rs " + str(alpha_rs))
    alpha_rd = parameters_list[3]
    print("alpha_rd " + str(alpha_rd))
    num_aug = parameters_list[4]
    print("num_aug " + str(num_aug))
    augment_function.gen_eda(filename, output_dict, alpha_sr, alpha_ri, alpha_rs, alpha_rd, num_aug)