# Easy data augmentation techniques for text classification
# Jason Wei and Kai Zou

import time
import eda_nlp.data.code.eda as eda_function  # PyCharm indicates an error but it works

# arguments to be parsed from command line
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--input", required=False, type=str, help="input file of unaugmented data")
ap.add_argument("--output", required=False, type=str, help="output file of unaugmented data")
ap.add_argument("--num_aug", required=False, type=int, help="number of augmented sentences per original sentence")
ap.add_argument("--alpha_sr", required=False, type=float,
                help="percent of words in each sentence to be replaced by synonyms")
ap.add_argument("--alpha_ri", required=False, type=float, help="percent of words in each sentence to be inserted")
ap.add_argument("--alpha_rs", required=False, type=float, help="percent of words in each sentence to be swapped")
ap.add_argument("--alpha_rd", required=False, type=float, help="percent of words in each sentence to be deleted")
args = ap.parse_args()

# the output file
output = None
if args.output:
    output = args.output
else:
    output = "output_file"

# number of augmented sentences to generate per original sentence
num_aug = 9  # default
if args.num_aug:
    num_aug = args.num_aug

# how much to replace each word by synonyms
alpha_sr = 0.1  # default
if args.alpha_sr is not None:
    alpha_sr = args.alpha_sr

# how much to insert new words that are synonyms
alpha_ri = 0.1  # default
if args.alpha_ri is not None:
    alpha_ri = args.alpha_ri

# how much to swap words
alpha_rs = 0.1  # default
if args.alpha_rs is not None:
    alpha_rs = args.alpha_rs

# how much to delete words
alpha_rd = 0.1  # default
if args.alpha_rd is not None:
    alpha_rd = args.alpha_rd

if alpha_sr == alpha_ri == alpha_rs == alpha_rd == 0:
    ap.error('At least one alpha should be greater than zero')


# generate more data with standard augmentation
def gen_eda(train_orig, output_dict, alpha_sr, alpha_ri, alpha_rs, alpha_rd, num_aug):
    """Function that generate more data with standard augmentation, substituting words with synonyms using Wordnet
        and also using other tricks like randomly swapping or deleting words
        but in our case we only use the substitution of synonym (setting sr to 0.1 and the others to 0)
        Produces an output file that is put inside the directory results, inside the directory of the relative dataset,
        inside the directory EDA_outputs
        Format of the input file: results_data_set_index_EDA_input.txt (which was the output of eda_format_func)
        Format of the output file: results_data_set_index_EDA_output_num_aug_alpha_sr_alpha_ri_alpha_rs_alpha_rd.txt

        :param file_path train_orig: path to the input file
        :param file_path output_dict: dict that will contain input phrase and list of outputs
        :param float alpha_sr: percentage of words substituted with synonyms, default to 0.1
        :param float alpha_ri: percentage of words randomly inserted, default to 0.1
        :param float alpha_rs: percentage of words randomly swapped, default to 0.1
        :param float alpha_rd: percentage of words randomly deleted, default to 0.1
        :param integer num_aug: number of produced sentences, default to 9
    """

    lines = open(train_orig, 'r').readlines()

    tic = time.perf_counter()

    for i, line in enumerate(lines):
        aug_sentences = eda_function.eda(line, alpha_sr=alpha_sr, alpha_ri=alpha_ri, alpha_rs=alpha_rs, p_rd=alpha_rd,
                                         num_aug=num_aug)
        aug_sentences_list = []
        for aug_sentence in aug_sentences:
            aug_sentences_list.append(aug_sentence)
        output_dict[line] = aug_sentences_list

    toc = time.perf_counter()
    print("generated augmented sentences with eda for " + train_orig + " with num_aug=" + str(num_aug))
