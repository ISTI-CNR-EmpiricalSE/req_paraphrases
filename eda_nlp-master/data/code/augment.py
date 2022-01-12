# Easy data augmentation techniques for text classification
# Jason Wei and Kai Zou

from eda import *
import time

#arguments to be parsed from command line
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--input", required=True, type=str, help="input file of unaugmented data")
ap.add_argument("--output", required=False, type=str, help="output file of unaugmented data")
ap.add_argument("--num_aug", required=False, type=int, help="number of augmented sentences per original sentence")
ap.add_argument("--alpha_sr", required=False, type=float, help="percent of words in each sentence to be replaced by synonyms")
ap.add_argument("--alpha_ri", required=False, type=float, help="percent of words in each sentence to be inserted")
ap.add_argument("--alpha_rs", required=False, type=float, help="percent of words in each sentence to be swapped")
ap.add_argument("--alpha_rd", required=False, type=float, help="percent of words in each sentence to be deleted")
args = ap.parse_args()

#the output file
output = None
if args.output:
    output = args.output
else:
    from os.path import dirname, basename, join
    output = join(dirname(args.input), 'eda_' + basename(args.input))

#number of augmented sentences to generate per original sentence
num_aug = 9 #default
if args.num_aug:
    num_aug = args.num_aug

#how much to replace each word by synonyms
alpha_sr = 0.1#default
if args.alpha_sr is not None:
    alpha_sr = args.alpha_sr

#how much to insert new words that are synonyms
alpha_ri = 0.1#default
if args.alpha_ri is not None:
    alpha_ri = args.alpha_ri

#how much to swap words
alpha_rs = 0.1#default
if args.alpha_rs is not None:
    alpha_rs = args.alpha_rs

#how much to delete words
alpha_rd = 0.1#default
if args.alpha_rd is not None:
    alpha_rd = args.alpha_rd

if alpha_sr == alpha_ri == alpha_rs == alpha_rd == 0:
     ap.error('At least one alpha should be greater than zero')

#generate more data with standard augmentation
def gen_eda(train_orig, output_file, alpha_sr, alpha_ri, alpha_rs, alpha_rd, num_aug=9):
    """Function that generate more data with standard augmentation, substituting words with synonyms using Wordnet
        and also using other tricks like randomly swapping or deleting words
        but in our case we only use the substitution of synonym (setting sr to 0.1 and the others to 0)
        Produces an output file that is put inside the directory results, inside the directory of the relative dataset,
        inside the directory EDA_outputs
        Format of the input file: results_data_set_index_EDA_input.txt (which was the output of eda_format_func)
        Format of the output file: results_data_set_index_EDA_output_num_aug_alpha_sr_alpha_ri_alpha_rs_alpha_rd.txt

        :param file_path train_orig: path to the input file
        :param file_path output_file: path to the output file
        :param float alpha_sr: percentage of words substituted with synonyms, default to 0.1
        :param float alpha_ri: percentage of words randomly inserted, default to 0.1
        :param float alpha_rs: percentage of words randomly swapped, default to 0.1
        :param float alpha_rd: percentage of words randomly deleted, default to 0.1
        :param integer num_aug: number of produced sentences, default to 9
    """

    writer = open(output_file, 'w')
    lines = open(train_orig, 'r').readlines()

    writer.write("num aug = " + str(num_aug) + "\n")
    writer.write("alpha_sr = " + str(alpha_sr) + "\n")
    writer.write("alpha_rd = " + str(alpha_rd) + "\n")
    writer.write("alpha_ri = " + str(alpha_ri) + "\n")
    writer.write("alpha_rs = " + str(alpha_rs) + "\n")

    tic = time.perf_counter()
    j = 0
    # we use old_label to understand when the label changes, because we have to put j to 1 when that happens
    old_label = 0
    for i, line in enumerate(lines):
        # I put print of the sentence to see which one had problems
        parts = line[:-1].split('\t')
        label = parts[0]
        if label != old_label:
            j = 0
        old_label = label
        sentence = parts[1]
        # the sentence in the format label.0) is the original sentence which is not even passed through parrot
        writer.write(label + "." + str(j) + ") " + sentence + '\n')
        j = j+1
        aug_sentences = eda(sentence, alpha_sr=alpha_sr, alpha_ri=alpha_ri, alpha_rs=alpha_rs, p_rd=alpha_rd, num_aug=num_aug)
        w = 1
        for aug_sentence in aug_sentences:
            writer.write(str(w) + " " + aug_sentence + '\n')
            w = w+1
    toc = time.perf_counter()
    writer.write(f"Total time = {toc - tic:0.4f} seconds\n")
    writer.close()
    print("generated augmented sentences with eda for " + train_orig + " to " + output_file + " with num_aug=" + str(num_aug))

#main function
if __name__ == "__main__":

    #generate augmented sentences and output into a new file
    gen_eda(args.input, output, alpha_sr=alpha_sr, alpha_ri=alpha_ri, alpha_rs=alpha_rs, alpha_rd=alpha_rd, num_aug=num_aug)