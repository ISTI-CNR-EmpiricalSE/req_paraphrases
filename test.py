import time
import os

tic = time.perf_counter()
f = open("my_file.txt", "w")
toc = time.perf_counter()
f.write(f"Time for the augment function:  {toc - tic:0.4f} seconds")