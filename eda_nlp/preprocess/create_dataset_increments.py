import os

datasets = ['cr', 'pc', 'sst1', 'sst2', 'subj', 'trec']

for dataset in datasets:
	line = 'cat increment_datasets_f2/' + dataset + '/test.py > sized_datasets_f1/test/' + dataset + '/test.py'
	os.system(line)