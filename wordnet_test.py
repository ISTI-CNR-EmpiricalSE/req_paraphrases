import time
import os
import sys

import spacy
from spacy_wordnet.wordnet_annotator import WordnetAnnotator
import nltk
from nltk.corpus import stopwords


def help_message():
    print("You have to choose between one of these three assets:")
    print("number of arguments =")
    print("0                        - default configuration, do all datasets from n1 included to n24 excluded")
    print("False n1,n5...           - not a cycle, but singles dataset n1 and n5")
    print("True n1,n5               - a cycle that goes from n2 included and n5 excluded")


def wordnet_test_func():
    """Function that replaces the non stop words found in each sentence with the synonyms found with worndet
        Produce an output file that is put inside the directory results, inside the directory of the relative dataset
        Format of the input file: results_file_index.txt (which was the output of parrot_test_func)
        Format of the output file: results_data_set_index_wordnet.txt
    """

    # I want to have the possibility to insert the dataset on which operate from command line
    # on the contrary, I identified the best asset of parameters, so they are fixed

    # INSTRUCTIONS:
    # number of arguments =
    # 0                         - default configuration, do all datasets from n1 included to n23 exluded
    # False n1,n5...            - not a cycle, but singles dataset n1 and n5
    # True n1,n5                - a cycle that goes from n2 included and n5 excluded

    start_index = None
    end_index = None
    data_set_list = []

    if len(sys.argv)-1 == 0:
        start_index = 1
        end_index = 24
    elif sys.argv[1] != "True" and sys.argv[1] != "False":
        help_message()
        return
    else:
        if sys.argv[1] == "True":
            if len(sys.argv)-2 != 2:
                help_message()
                return
            else:
                start_index = int(sys.argv[2])
                end_index = int(sys.argv[3])
        elif sys.argv[1] == "False":
            if len(sys.argv)-2 == 0:
                help_message()
                return
            else:
                # name false 1 5 3
                data_sets_list = []
                for i in range(2, len(sys.argv)):
                    data_set_list.append(int(sys.argv[i]))

    nlp = spacy.load('en')

    nlp.add_pipe(WordnetAnnotator(nlp.lang), after='tagger')

    stpwrd = nltk.corpus.stopwords.words('english')
    new_stopwords = ["an", "ss", "I", "to", "in", "so", "that", "and"]
    stpwrd.extend(new_stopwords)

    data_set_index_list = []
    if start_index is not None and end_index is not None:
        data_set_index_list = range(start_index, end_index)
        print("doing data_sets from " + str(start_index) + " included to " + str(end_index) + " excluded")
    elif data_set_list is not None:
        data_set_index_list = data_set_list
        print("doing data_sets")
        print(data_set_index_list)
    else:
        help_message()
        return

    tic0 = time.perf_counter()  # time for all datasets

    for data_set_index in data_set_index_list:
        tic1 = time.perf_counter()  # time for the single dataset
        # TODO: take parrot file as input
        input_file = open("results/data_set_" + str(data_set_index) + "/results_1.txt", "r")
        output_file = open("results/data_set_" + str(data_set_index) + "/results_" + str(data_set_index) +
                           "_wordnet.txt", "w")
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
                clean_phrase = dirty_phrase[2:end_index-5]
            else:
                continue

            # for each input phrase: 5 output phrases maximum
            phrase1 = clean_phrase
            phrase2 = clean_phrase
            phrase3 = clean_phrase
            phrase4 = clean_phrase
            phrase5 = clean_phrase

            output_file.write(str(j) + "." + str(c) + ") " + "Input phrase: " + clean_phrase + "\n")
            doc = nlp(clean_phrase)

            for token in doc:
                # replace synonym only of words that are not stopwords
                if token.text.lower() not in stpwrd:
                    # wordnet object link spacy token with nltk wordnet interface by giving access to synonyms
                    syns_dirty = token._.wordnet.synsets()

                    syns_clean = []

                    for i in syns_dirty:
                        # format: synonym.stuff
                        synonym_dirty = i.name()

                        # take off from first "."
                        index = synonym_dirty.find(".")
                        synonym = synonym_dirty[:index]

                        # insert synonym in final list only if :
                        # it's different from original word
                        # synonym different from token + 1
                        # synonym + 1 different from token
                        # and if absent from the final list
                        found = False
                        if synonym == token.text.lower():
                            found = True
                        if synonym[:len(synonym)-1] == token.text.lower():
                            found = True
                        if synonym == token.text.lower()[:len(token.text)-1]:
                            found = True
                        if synonym in syns_clean:
                            found = True
                        if found is False:
                            syns_clean.append(synonym)

                    print(token.text)
                    print(syns_clean)
                    print("\n")

                    # it returns 5 phrases that at the beginning are identical to the original
                    # until it finds (maximum 5) synonyms in the list it keeps substituting it
                    # when pop occurs the list change and element that is index 1 will become index 0
                    if syns_clean:
                        phrase1 = phrase1.replace(token.text, syns_clean[0])
                        syns_clean.pop(0)
                    if syns_clean:
                        phrase2 = phrase2.replace(token.text, syns_clean[0])
                        syns_clean.pop(0)
                    if syns_clean:
                        phrase3 = phrase3.replace(token.text, syns_clean[0])
                        syns_clean.pop(0)
                    if syns_clean:
                        phrase4 = phrase4.replace(token.text, syns_clean[0])
                        syns_clean.pop(0)
                    if syns_clean:
                        phrase5 = phrase5.replace(token.text, syns_clean[0])
                        syns_clean.pop(0)

            output_file.write(phrase1 + "\n")
            output_file.write(phrase2 + "\n")
            output_file.write(phrase3 + "\n")
            output_file.write(phrase4 + "\n")
            output_file.write(phrase5 + "\n")
            output_file.write("\n")

        toc1 = time.perf_counter()
        output_file.write(f"Time for the single dataset = {toc1 - tic1:0.4f} seconds = {(toc1 - tic1)/60:0.4f} "
                          f"minutes = {((toc1 - tic1)/60/60):0.4f} hours" + "\n")

    toc0 = time.perf_counter()
    output_file.write("\n")
    # if you execute the script only on one data set total time will be equal to single time
    output_file.write(f"Time for all datasets = {toc0 - tic0:0.4f} seconds = {(toc0 - tic0)/60:0.4f} "
                      f"minutes = {((toc0 - tic0)/60/60):0.4f} hours")


if __name__ == '__main__':
    wordnet_test_func()



