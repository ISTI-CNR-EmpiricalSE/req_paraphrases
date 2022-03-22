# parrot

import time
from parrot import Parrot
import torch
import warnings


def parrot_executor_func(filename, parameters_list, output_dict):
    """
    Function that executes Parrot augment function on a file
    :param filename: name of the input file
    :param parameters_list: list of parameters configured by the user [syn_vs_synsets, syn_vs_term, n_max]
    :param output_dict: dictionary that will contain the outputs {input_1: [output_1.1, output_1.2...], input_2...}
    :return:

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
    parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")

    toc1 = time.perf_counter()

    print(f"Downloaded the parrot_paraphraser_on_T5 in {toc1 - tic1:0.4f} seconds")

    tic0 = time.perf_counter()

    my_file = open(filename, "r")
    phrases = my_file.read().splitlines()

    # Perform the paraphrasing using the parrot.augment() function

    # parrot.augment() arguments
    use_gpu = False
    diversity_ranker = "levenshtein"
    max_length = 32
    max_return_phrases = parameters_list[0]  # configurable (default: 15)
    print("max re phr " + str(max_return_phrases))
    do_diverse = parameters_list[1]  # configurable (default: True)
    print("do_diverse " + str(do_diverse))
    adequacy_threshold = parameters_list[2]  # configurable (default: 0.5)
    print("adequacy " + str(adequacy_threshold))
    fluency_threshold = parameters_list[3]  # configurable (default: 0.5)
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
            # you don't want {}, para_phrase it's a tuple and you want the first object
            paraphrase_list.append(para_phrase[0])

        output_dict[phrase] = paraphrase_list

        toc2 = time.perf_counter()

    toc0 = time.perf_counter()


