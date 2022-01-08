import time
import os

import spacy
from spacy_wordnet.wordnet_annotator import WordnetAnnotator
import nltk
from nltk.corpus import stopwords


def wordnet_test_func():
    """Function that replaces the non stop words found in each sentence with the synonyms found with worndet
        Produce an output file that is put inside the directory results, inside the directory of the relative dataset
        Format of the input file: results_file_index.txt (which was the output of parrot_test_func)
        Format of the output file: results_data_set_index_wordnet.txt
    """

    stpwrd = nltk.corpus.stopwords.words('english')
    new_stopwords = ["an", "ss", "I", "to", "in", "so", "that", "and"]
    stpwrd.extend(new_stopwords)

    nlp = spacy.load('en')

    nlp.add_pipe(WordnetAnnotator(nlp.lang), after='tagger')

    tic0 = time.perf_counter()  # time for all datasets

    for data_set_index in range(1, 24):
        tic1 = time.perf_counter()  # time for the single dataset
        input_file = open("data_sets/data_set_" + str(data_set_index) + ".txt", "r")
        # input_file = open("data_sets/data_set_23.txt", "r")
        output_file = open("results/data_set_" + str(data_set_index) + "/results_" + str(data_set_index) +
                           "_wordnet.txt", "w")
        # output_file = open("results/data_set_23/results_23_wordnet.txt","w")
        output_file.write("data_set_number:" + str(data_set_index) + "\n")
        output_file.write("\n")
        phrases = input_file.read().splitlines()

        for phrase in phrases:

            # for each input phrase: 5 output phrases maximum
            phrase1 = phrase
            phrase2 = phrase
            phrase3 = phrase
            phrase4 = phrase
            phrase5 = phrase

            output_file.write("Input phrase: " + phrase + "\n")
            doc = nlp(phrase)

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
                        # it's different from the plural of the original word (synonym different from token + s)
                        # it's different from the singular of the original word (synonym + s different from token)
                        # and if absent from the final list
                        found = False
                        if synonym == token.text.lower():
                            found = True
                        if synonym == token.text.lower() + "s":
                            found = True
                        if synonym + "s" == token.text.lower():
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



