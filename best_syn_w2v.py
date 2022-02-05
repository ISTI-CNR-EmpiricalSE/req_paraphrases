# wordnet nltk (similarities) + mine

import nltk
import spacy
from nltk.corpus import wordnet
from spacy_wordnet.wordnet_annotator import WordnetAnnotator
import os
import time
import gensim.downloader
from gensim.models import Word2Vec
from gensim.test.utils import common_texts, common_dictionary, common_corpus

stpwrd = nltk.corpus.stopwords.words('english')
new_stopwords = ["an", "ss", "I", "to", "in", "so", "that", "and", "-", "_", ",", ";", ".", ":", "?", "!", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0" ]
stpwrd.extend(new_stopwords)

nlp = spacy.load('en')
nlp.add_pipe(WordnetAnnotator(nlp.lang), after='tagger')

w2v_model = gensim.downloader.load('word2vec-google-news-300')

tic0 = time.perf_counter()  # time for all datasets

for data_set_index in [1, 24]:
    file_index = 1
    tic1 = time.perf_counter()  # time for single file

    input_file = open("results/data_set_" + str(data_set_index) + "/results_1.txt", "r")
    dir = "results/data_set_" + str(data_set_index) + "/best_syn_w2v_outputs"
    if not os.path.exists(dir):
        os.makedirs(dir)
    output_file = open(dir + "/results_" + str(data_set_index) + "_best_syn_w2v.txt", "w")
    scoring_file = open(dir + "/scoring_w2v.txt", "w")

    file_index = file_index + 1
    output_file.write("data_set_number:" + str(data_set_index) + "\n")
    output_file.write("\n")
    dirty_phrases = input_file.read().splitlines()
    clean_phrase = ""
    j = 0
    c = 0
    for dirty_phrase in dirty_phrases:
        if "Input_phrase" in dirty_phrase:
            j = j + 1
            c = 0
            if dirty_phrase.startswith("Input_phrase:"):
                # the format of the line is: Input_phrase: phrase
                clean_phrase = dirty_phrase[14:]
            else:
                # the format of the line is: number) Input_phrase: phrase
                clean_phrase = dirty_phrase[17:]
        elif dirty_phrase.startswith("("):
            c = c + 1
            end_index = dirty_phrase.find(")")
            clean_phrase = dirty_phrase[2:end_index - 5]
        else:
            continue
        phrase = clean_phrase
        output_file.write(str(j) + "." + str(c) + ") " + "Input phrase: " + phrase + "\n")
        tokens = nlp(phrase)
        # everything is a token apart from space
        scoring_file.write(clean_phrase + "\n")

        synset_dict = {}
        for token in tokens:
            if token.text.lower() not in stpwrd and not token.text.isnumeric():
                synset = wordnet.synsets(token.text)
                synset_dict[token.text] = synset

        best_syn_list = []

        for token in tokens:
            if token.text.lower() not in stpwrd and not token.text.isnumeric():
                # we don't want that modifying synsets leads to modify synset_dict[token.text]
                synsets = []
                for a in synset_dict[token.text]:
                    synsets.append(a)
                # for each token i have a dictionary to save the scoring of each of his synonym
                # scoring is similarity calculated summing single similarities of the synonym
                # with all (not his original) the synsets of other words
                # if synsets:
                    # synsets.pop(0)  # comment this to compare the eto, uncomment to not compare
                scoring_dict = {}
                for synset in synsets:
                    scoring = 0
                    for compare_token in tokens:
                        # to not compare a synonym with the original word of him uncomment below
                        # compare_token.text != token.text and
                        if compare_token.text.lower() not in stpwrd and not compare_token.text.isnumeric():
                            compare_synsets = synset_dict[compare_token.text]
                            if compare_synsets:
                                for compare_synset in compare_synsets:

                                    # sinonimo che deve accumulare punteggio, in formato non synset
                                    synset_name = synset.name()
                                    index = synset_name.find(".")
                                    synset_name_final = synset_name[:index]

                                    # roba a cui lo confronto, in formato non synset
                                    compare_synset_name = compare_synset.name()
                                    index = compare_synset_name.find(".")
                                    compare_synset_name_final = compare_synset_name[:index]

                                    # se if commentato è tecnica 1, syn vs synsets (per stabilire punteggio di sinonimo lo confronto con tutti i termini e sinonimi)
                                    # se if non è commentato è tecnica 2, syn vs term (per stabilire punteggio di sinonimo lo confronto con tutti i termini)
                                    # if compare_synset_name_final.lower() == compare_token.text.lower():
                                    print(synset)
                                    print(compare_token.text)
                                    print(compare_synset)
                                    # with lch you need to have synset pos = compare_synset pos
                                    sim = w2v_model.similarity(synset_name_final, compare_synset_name_final)
                                    print(sim)
                                    # it could not exists a path that connects, if you put simulate root true it always exists
                                    if sim:
                                        scoring = scoring + sim

                    scoring_dict[synset] = scoring
                scoring_file.write("synonyms for " + token.text + "\n")
                scoring_file.write(str(scoring_dict) + "\n")
                # save the synonym with higher score
                max = 0
                for syn in scoring_dict.keys():
                    if scoring_dict[syn] > max:
                        max = scoring_dict[syn]
                        best_syn = syn
                if max != 0:
                    print(best_syn)
                    best_syn_list.append(best_syn)
                    best_syn_name = best_syn.name()
                    index = best_syn_name.find(".")
                    best_syn_name_final = best_syn_name[:index]
                    # you don't want to substitute parts of words
                    # (example of wrong behaviour: if design substituted with plan -> redesign is substituted with replan)
                    if " " + token.text + " " in phrase:
                        phrase = phrase.replace(" " + token.text + " ", " " + best_syn_name_final + " ")
                    elif " " + token.text + "," in phrase:
                        phrase = phrase.replace(" " + token.text + ",", " " + best_syn_name_final + ",")
                    elif " " + token.text + "\n" in phrase:
                        phrase = phrase.replace(" " + token.text + "\n", " " + best_syn_name_final + "\n")
                    elif " " + token.text + "." in phrase:
                        phrase = phrase.replace(" " + token.text + ".", " " + best_syn_name_final + ".")

        output_file.write(phrase + "\n")
        scoring_file.write(phrase + "\n\n")


    output_file.write("\n")
    toc1 = time.perf_counter() # time for single file
    output_file.write(f"Time for single file = {toc1 - tic1:0.4f} seconds = {(toc1 - tic1) / 60:0.4f} "
                      f"minutes = {((toc1 - tic1) / 60 / 60):0.4f} hours")



toc0 = time.perf_counter()  # time for all datasets
output_file.write("\n")
# if you execute the script only on one data set total time will be equal to single time
output_file.write(f"Time for all datasets = {toc0 - tic0:0.4f} seconds = {(toc0 - tic0) / 60:0.4f} "
                  f"minutes = {((toc0 - tic0) / 60 / 60):0.4f} hours")
