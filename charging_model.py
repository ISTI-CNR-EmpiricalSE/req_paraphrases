import os
import time

from parrot import Parrot
import torch
import warnings


def charging_model_func():
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

    # download files one by one and put them in a directory,
    # doesn't work because it doesn't find file.bin (they are put inside directory archive)
    # you have to download git lsf e clone model in repository
    # parrot = Parrot(model_tag="directory")

    # after clone in directory it takes it from that (test changing name)
    # but time is the same and it needs internet
    # parrot = Parrot(model_tag="parrot_paraphraser_on_T5")
    # TODO: error ->
    # VCS root configuration problems
    # The directory <Project>/parrot_paraphraser_on_T5 is registered as a Git root,
    # but no Git repositories were found there.
    # <Project>/model
    # Configure…

    # lfs was giving problems so -> git config lfs.https://github.com/ISTI-CNR-EmpiricalSE/req_paraphrases.git/info/lfs.locksverify false
    # cancellata dirctory parrot_paraphraser_on_T5
    # tolta parrot_paraphraser_on_T5 da version control

    # Init models (make sure you init ONLY once if you integrate this to your code)
    parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")

    toc1 = time.perf_counter()
    print(f"Downloaded the model in {toc1 - tic1:0.4f} seconds")


if __name__ == '__main__':
    charging_model_func()
