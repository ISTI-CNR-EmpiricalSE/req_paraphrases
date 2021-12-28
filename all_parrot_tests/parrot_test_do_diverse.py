import time
import os

# PARAMETRO DA TENERE FISSO A "levenshtein", TANTO NON CAMBIA NULLA

tic0 = time.perf_counter()

from parrot import Parrot
import torch
import warnings
warnings.filterwarnings("ignore")

# uncomment to get reproducable paraphrase generations
# In order to allow reproducibility of the text paraphrasing, the random seed number will be set.
# What this does is produce the same results for the same seed number (even if it is re-run multiple times).
def random_state(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

random_state(1234)

tic1 = time.perf_counter()

#Init models (make sure you init ONLY once if you integrate this to your code)
parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")

toc1 = time.perf_counter()
print(f"Downloaded the model in {toc1 - tic1:0.4f} seconds")

data_set_number = input("Inserisci il numero di data set: ")
my_file = open("../data_sets/data_set_" + str(data_set_number) + ".txt", "r")
phrases = my_file.read().splitlines()

# Perform the paraphrasing using the parrot.augment() function
# that takes in as input argument the phrase being iterated.
# Generated paraphrases are assigned to the para_phrases variable.
do_diverse_array = [True, False]

dir = "../results/parameters/do_diverse/second"
if not os.path.exists(dir):
    os.makedirs(dir)

file_index = 1


for current_do_diverse in do_diverse_array:
    tic2 = time.perf_counter()

    # examples
    # results/parameters/diversity_ranker_1
    # results/parameters/diversity_ranker_2
    f = open(dir + "/" + "do_diverse_" + str(file_index) + ".txt", "w")
    file_index = file_index + 1
    f.write("data_set_number = " + str(data_set_number) + "\n")
    f.write("\n")
    f.write("use_gpu = False\n")
    f.write("diversity_ranker = levenshtein\n")
    f.write("max_length = 32\n")
    f.write("max_return_phrases = 15\n")
    f.write("adequacy_threshold = 0.5\n")
    f.write("fluency_threshold = 0.1\n")
    f.write("\n")
    f.write("do_diverse = " + str(current_do_diverse) + "\n")
    f.write("\n")
    phrase_index = 1
    for phrase in phrases:
        f.write("-"*100)
        f.write("\n")
        f.write(str(phrase_index) + ") ")
        phrase_index = phrase_index + 1
        f.write("Input_phrase: " + phrase)
        f.write("\n")
        f.write("-"*100)
        f.write("\n")

        tic3 = time.perf_counter()
        para_phrases = parrot.augment(input_phrase=phrase,
                                      use_gpu=False,
                                      diversity_ranker="levenshtein",
                                      do_diverse=current_do_diverse,
                                      max_return_phrases=15,
                                      max_length=32,
                                      adequacy_threshold=0.5,
                                      fluency_threshold=0.1)
        toc3 = time.perf_counter()
        print(f"Time for the augment function:  {toc3 - tic3:0.4f} seconds")

        if not para_phrases:  # in realtà se non c'erano parafrasi para_phrases non è lista vuota (che vale false) (non ci sarebbero problemi a iterare su lista vuota), ma è None, ma anche None vale false !!!
            para_phrases = ["None"]

        for para_phrase in para_phrases:
            f.write(str(para_phrase) + "\n")

        toc2 = time.perf_counter()
    f.write("\n")
    f.write(f"Got the paraphrases in {toc2 - tic2:0.4f} seconds")
    f.write("\n")

toc0 = time.perf_counter()
f = open(dir + "/" + "do_diverse_" + str(file_index - 1) + ".txt", "a")
f.write("\n")
f.write(f"Total time = {toc0 - tic0:0.4f} seconds = {((toc0 - tic0)/60/60):0.4f} hours")

