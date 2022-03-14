# parrot

import time
import os
import sys
from parrot import Parrot
import torch
import warnings
from pathlib import Path


def parrot_executor_func(filename, parameters_list, output_dict):
    """
    Function that executes Parrot augment function on a file
    :param filename: name of the input file
    :param output_dict: dictionary at the beginning empty that will contain outputs
    :type filename: str
    :type output_dict: dict
    :return: A dictionary in which the keys are the inputs phrases and the values are the lists of relative outputs
    :rtype: dict

    """

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

    # Init models (make sure you init ONLY once if you integrate this to your code)
    # this was not working but I did pip install protobuf and it worked
    # it was giving this error --->
    # ImportError: T5 Converter requires the protobuf library but it was not found in your environment.
    # Checkout the instructions on the installation page of its repo:
    # https://github.com/protocolbuffers/protobuf/tree/master/python#installation
    # and follow the ones that match your environment.
    # Protocol Buffers are Google’s data interchange format

    parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")

    toc1 = time.perf_counter()

    print(f"Downloaded the parrot_paraphraser_on_T5 in {toc1 - tic1:0.4f} seconds")

    tic0 = time.perf_counter()

    my_file = open(filename, "r")
    phrases = my_file.read().splitlines()


    # Perform the paraphrasing using the parrot.augment() function
    # that takes in as input argument the phrase being iterated.
    # Generated paraphrases are assigned to the para_phrases variable.

    use_gpu = False
    diversity_ranker = "levenshtein"
    max_length = 32
    max_return_phrases = parameters_list[0]
    print("max re phr " + max_return_phrases)
    do_diverse = parameters_list[1]
    print("do_diverse " + str(do_diverse))
    adequacy_threshold = parameters_list[2]
    print("adequacy " + str(adequacy_threshold))
    fluency_threshold = parameters_list[3]
    print("fluency " + str(fluency_threshold))

    tic2 = time.perf_counter()

    for phrase in phrases:

        tic3 = time.perf_counter()
        para_phrases = parrot.augment(input_phrase=phrase,
                                      use_gpu=use_gpu,
                                      diversity_ranker=diversity_ranker,
                                      do_diverse=do_diverse,
                                      max_return_phrases=max_return_phrases,
                                      max_length=max_length,
                                      adequacy_threshold=adequacy_threshold,
                                      fluency_threshold=fluency_threshold)
        toc3 = time.perf_counter()
        print(f"Time for the augment function:  {toc3 - tic3:0.4f} seconds")

        # it was giving problems iterating on an empty list
        # if it given no paraphrases the list is empty
        # empty list = None = False
        if not para_phrases:
            print("None")
            para_phrases = ["None"]

        paraphrase_list = []
        for para_phrase in para_phrases:
            paraphrase_list.append(para_phrase)

        output_dict[phrase] = paraphrase_list

        toc2 = time.perf_counter()

    toc0 = time.perf_counter()


