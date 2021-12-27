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
my_file = open("data_sets/data_set_" + str(data_set_number) + ".txt", "r")
phrases = my_file.read().splitlines()

# Perform the paraphrasing using the parrot.augment() function
# that takes in as input argument the phrase being iterated.
# Generated paraphrases are assigned to the para_phrases variable.
diversity_ranker_array = ["levenshtein", "euclidean", "diff"]

dir = "../results/invariant_parameters/diversity_ranker/first"
if not os.path.exists(dir):
    os.mkdirs(dir)

file_index = 1


for current_diversity_ranker in diversity_ranker_array:
    tic2 = time.perf_counter()

    # examples
    # results/invariant_parameters/diversity_ranker_1
    # results/invariant_parameters/diversity_ranker_2
    f = open(dir + "/" + "diversity_ranker_" + str(file_index) + ".txt", "w")
    file_index = file_index + 1
    f.write("data_set_number = " + str(data_set_number) + "\n")
    f.write("diversity_ranker = " + current_diversity_ranker + "\n")
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
                                      diversity_ranker=current_diversity_ranker,
                                      do_diverse=True,
                                      max_return_phrases=10,
                                      max_length=32,
                                      adequacy_threshold=0.99,
                                      fluency_threshold=0.90)
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
print(f"Total time: {toc0 - tic0:0.4f} seconds")

