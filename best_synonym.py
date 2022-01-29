# wordnet nltk (similarities) + mine

import nltk
import spacy
from nltk.corpus import wordnet
from spacy_wordnet.wordnet_annotator import WordnetAnnotator
import os
import time

stpwrd = nltk.corpus.stopwords.words('english')
new_stopwords = ["an", "ss", "I", "to", "in", "so", "that", "and", "-", "_", ",", ";", ".", ":", "?", "!", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0" ]
stpwrd.extend(new_stopwords)

nlp = spacy.load('en')
nlp.add_pipe(WordnetAnnotator(nlp.lang), after='tagger')

similarity_array = ["path"]
simulate_root_array = [True]

tic0 = time.perf_counter()  # time for all datasets

for data_set_index in [1, 24]:
    file_index = 1
    for similarity in similarity_array:
        for simulate_root in simulate_root_array:

            tic1 = time.perf_counter()  # time for single file

            input_file = open("results/data_set_" + str(data_set_index) + "/results_1.txt", "r")
            dir = "results/data_set_" + str(data_set_index) + "/best_syn_outputs"
            if not os.path.exists(dir):
                os.makedirs(dir)
            output_file = open(dir + "/results_" + str(data_set_index) + "_best_syn" + str(file_index) + ".txt", "w")
            scoring_file = open(dir + "/scoring.txt", "w")

            scoring_file.write("similarity:" + similarity + "\n")
            scoring_file.write("simulate_root:" + str(simulate_root) + "\n")
            scoring_file.write("\n")

            file_index = file_index + 1
            output_file.write("data_set_number:" + str(data_set_index) + "\n")
            output_file.write("similarity:" + similarity + "\n")
            output_file.write("simulate_root:" + str(simulate_root) + "\n")
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

                synset_dict = {}
                for token in tokens:
                    if token.text.lower() not in stpwrd and not token.text.isnumeric():
                        synset = wordnet.synsets(token.text)
                        synset_dict[token.text] = synset

                scoring_file.write(str(synset_dict))

                # clean synset
                for token in tokens:
                    done = False
                    if token.text.lower() not in stpwrd and not token.text.isnumeric():
                        tmp = []
                        for copy in synset_dict[token.text]:
                            tmp.append(copy)
                        for syn in tmp:
                            syn_name = syn.name()
                            index = syn_name.find(".")
                            synonym = syn_name[:index]
                            # remove synonym equal to original or too similar (plural, singular, past participle ...)
                            if synonym == token.text.lower() or synonym[:len(synonym)-1] == token.text.lower() or synonym == token.text.lower()[:len(token.text)-1] or \
                                    synonym[:len(synonym)-2] == token.text.lower() or synonym == token.text.lower()[:len(token.text)-2]:
                                synset_dict[token.text].remove(syn)
                                # put the equal one in front, but do this just once
                                if synonym == token.text.lower() and not done:
                                    done = True
                                    synset_dict[token.text].insert(0, syn)

                scoring_file.write("cleaning synset_dict" + "\n")
                scoring_file.write(str(synset_dict))
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
                                # i'm not comparing a synonym with the original word of him
                                # compare_token.text != token.text and
                                if compare_token.text.lower() not in stpwrd and not compare_token.text.isnumeric():
                                    compare_synsets = synset_dict[compare_token.text]
                                    if compare_synsets:
                                        for compare_synset in compare_synsets:

                                            # confronto solo il synset che equivale a token
                                            # se vuoi confrontare un synset son tutti i synset di tutti i token tranne suo, commenta le tre righe sotto e if
                                            # compare_synset_name = compare_synset.name()
                                            # index = compare_synset_name.find(".")
                                            # compare_synset_name_final = compare_synset_name[:index]
                                            # if compare_synset_name_final.lower() == compare_token.text.lower():
                                            print(synset)
                                            print(compare_token.text)
                                            print(compare_synset)
                                            # with lch you need to have synset pos = compare_synset pos
                                            if similarity == "path" and simulate_root is True:
                                                sim = synset.path_similarity(compare_synset, simulate_root=True)
                                            elif similarity == "path" and simulate_root is False:
                                                sim = synset.path_similarity(compare_synset, simulate_root=False)
                                            elif similarity == "wup" and simulate_root is True:
                                                sim = synset.wup_similarity(compare_synset, simulate_root=True)
                                            elif similarity == "wup" and simulate_root is False:
                                                sim = synset.wup_similarity(compare_synset, simulate_root=False)
                                            print(sim)
                                            # it could not exists a path that connects, if you put simulate root true it always exists
                                            if sim:
                                                scoring = scoring + sim

                            scoring_dict[synset] = scoring
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


            output_file.write("\n")
            toc1 = time.perf_counter() # time for single file
            output_file.write(f"Time for single file = {toc1 - tic1:0.4f} seconds = {(toc1 - tic1) / 60:0.4f} "
                              f"minutes = {((toc1 - tic1) / 60 / 60):0.4f} hours")



toc0 = time.perf_counter()  # time for all datasets
output_file.write("\n")
# if you execute the script only on one data set total time will be equal to single time
output_file.write(f"Time for all datasets = {toc0 - tic0:0.4f} seconds = {(toc0 - tic0) / 60:0.4f} "
                  f"minutes = {((toc0 - tic0) / 60 / 60):0.4f} hours")


'''
putting (if exists FIX THIS) the equal to original (eto) synonym in front
comparing all synonyms of a word (ALSO the eto) with all synonyms of all other words (not his original word)
'''

'''
path similarity

- simulate root = true (default)
input : "As a Data user, I want to have the 12-19-2017 deletions processed."
As a data user, I desire to have the 12-19-2017 omission march.
input : "As a UI designer, I want to redesign the Resources page, so that it matches the new Broker design styles."
As a UI designer, I desire to redesign the Resources page, so that it equal the new broker plan styles.
input : "The system shall refresh the display every 60 seconds"
The system shall review the expose every 60 seconds

- simulate root = false
input : "As a Data user, I want to have the 12-19-2017 deletions processed."
As a data user, I need to have the 12-19-2017 omission processed.
input : "As a UI designer, I want to redesign the Resources page, so that it matches the new Broker design styles."
As a UI designer, I need to redesign the Resources page, so that it peer the new agent purpose styles.
input : "The system shall refresh the display every 60 seconds"
The system shall refresh the display every 60 seconds
'''

'''
lch_similarity
simulate root = true
Traceback (most recent call last):
  File "/home/isabella/PycharmProjects/req_paraphrases/best_synonym.py", line 61, in <module>
    sim = syn.lch_similarity(token_syn_format)
  File "/home/isabella/anaconda3/envs/req_paraphrases/lib/python3.9/site-packages/nltk/corpus/reader/wordnet.py", line 835, in lch_similarity
    raise WordNetError(
nltk.corpus.reader.wordnet.WordNetError: Computing the lch similarity requires Synset('datum.n.01') and Synset('want.v.02') to have the same part of speech.
non posso confrontare cose che hanno diverso pos ?????????????????????????????
simulate root = false
uguale
'''

'''
wup similarity

- simulate root = true (default)
As a data user, I desire to have the 12-19-2017 omission march.
input : "As a UI designer, I want to redesign the Resources page, so that it matches the new Broker design styles."
As a UI designer, I desire to redesign the Resources page, so that it equal the new agent plan styles.
input : "The system shall refresh the display every 60 seconds"
The system shall review the expose every 60 seconds

- simulate root = false
input : "As a Data user, I want to have the 12-19-2017 deletions processed."
As a data user, I need to have the 12-19-2017 omission processed.
input : "As a UI designer, I want to redesign the Resources page, so that it matches the new Broker design styles."
As a UI designer, I need to redesign the Resources page, so that it peer the new agent purpose styles.
input : "The system shall refresh the display every 60 seconds"
The system shall refresh the display every 60 seconds
'''

'''
putting (if exists FIX THIS) the equal to original (eto) synonym in front
comparing all synonyms of a word (NOT the eto) with all synonyms of all other words (not his original word)
drug user wins on exploiter -> compare also the eto (if the original was better just don't change it)
'''
