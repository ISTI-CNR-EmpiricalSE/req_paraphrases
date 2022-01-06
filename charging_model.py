import os
import time

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

# non funziona file.bin messi dentro archivio, poi non li trova, devi scaricare git lsf e clonare modello in repository
# parrot = Parrot(model_tag="directory parrot_paraphraser_on_T5")

# dopo clone in directory parrot_paraphraser_on_T5
parrot = Parrot(model_tag="parrot_paraphraser_on_T5")

#Init models (make sure you init ONLY once if you integrate this to your code)
#parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")

toc1 = time.perf_counter()
print(f"Downloaded the model in {toc1 - tic1:0.4f} seconds")
