# A simple Word Sense Disambiguation application + mine

import nltk
import codecs
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
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

# -----------------------------------------------------------------------------------

# Remove Stop Words . Word Stemming . Return new tokenised list.


def filteredSentence(sentence, token_text):

    filtered_sent = []
    lemmatizer = WordNetLemmatizer()  # lemmatizes the words
    ps = PorterStemmer()  # stemmer stems the root of the word.

    stop_words = set(stopwords.words("english"))
    words = word_tokenize(sentence)

    for w in words:
        # I compare the synonym of a word with all other words (not the word of whom it is synonym)
        if w.lower() not in stpwrd and not w.isnumeric() and w.lower() != token_text:
            filtered_sent.append(lemmatizer.lemmatize(ps.stem(w)))
            for i in synonymsCreator(w):
                filtered_sent.append(i)
    return filtered_sent

# --------------------------------------------------------------------------------------

# Add synonyms to match list


def synonymsCreator(word):
    synonyms = []

    for syn in wordnet.synsets(word):
        for i in syn.lemmas():
            synonyms.append(i.name())

    return synonyms

# ---------------------------------------------------------------------------------------

# Check and return similarity


def simlilarityCheck(word1, word2):

    word1 = word1 + ".n.01"
    word2 = word2 + ".n.01"
    try:
        w1 = wordnet.synset(word1)
        w2 = wordnet.synset(word2)

        return w1.wup_similarity(w2)

    except:
        return 0

# -----------------------------------------------------------------------------------------


def simpleFilter(sentence, token_text):

    filtered_sent = []
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(sentence)

    for w in words:
        # I compare the synonym of a word with all other words (not the word of whom it is synonym)
        if w.lower() not in stpwrd and not w.isnumeric() and w.lower() != token_text:
            filtered_sent.append(lemmatizer.lemmatize(w))
            # for i in synonymsCreator(w):
            # 	filtered_sent.append(i)
    return filtered_sent


tic0 = time.perf_counter()  # time for all datasets

for data_set_index in range(1, 2):
    file_index = 1

    tic1 = time.perf_counter()  # time for single file

    input_file = open("results/data_set_" + str(data_set_index) + "/results_1.txt", "r")
    # not eto
    # dir = "results/data_set_" + str(data_set_index) + "/best_syn_outputs_wsd_not_eto"
    # eto
    dir = "results/data_set_" + str(data_set_index) + "/best_syn_outputs_wsd"
    if not os.path.exists(dir):
        os.makedirs(dir)
    output_file = open(dir + "/results_" + str(data_set_index) + "_best_syn_wsd_" + str(file_index) + ".txt", "w")
    file_index = file_index + 1
    output_file.write("data_set_number:" + str(data_set_index) + "\n")
    output_file.write("\n")
    dirty_phrases = input_file.read().splitlines()
    clean_phrase = ""
    p = 0
    c = 0
    for dirty_phrase in dirty_phrases:
        if "Input_phrase" in dirty_phrase:
            p = p + 1
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
        sent = clean_phrase
        output_file.write(str(p) + "." + str(c) + ") " + "Input phrase: " + sent + "\n")

        tokens = nlp(sent)
        # everything is a token apart from space

        synset_dict = {}
        for token in tokens:
            if token.text.lower() not in stpwrd and not token.text.isnumeric():
                synset = wordnet.synsets(token.text)
                synset_dict[token.text] = synset

        # print(synset_dict)

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

        print(sent)
        print("dizionario chiave: termine, valore: sinonimi")
        print(synset_dict)
        print("\n\n")
        best_syn_list = []

        # scorro i sinonimi, metetndoli in forma di stringa e li confronto a frase usando di codice di wsd, salvo punteggio

        for token in tokens:
            if token.text.lower() not in stpwrd and not token.text.isnumeric():
                print("operazioni di rimpiazzamento per il termine: " + token.text)
                print("\n")
                synsets = synset_dict[token.text]
                # for each token i have a dictionary to save the scoring of each of his synonym
                # scoring is similarity calculated summing single similarities of the synonym
                # with all (not his original) the synsets of other words
                # uncomment to not eto
                # if synsets:
                    # synsets.pop(0)
                scoring_dict = {}
                for synset in synsets:
                    scoring = 0
                    syn_name = synset.name()
                    index = syn_name.find(".")
                    syn = syn_name[:index]
                    print("calcolo punteggio per sinonimo: " + syn)
                    print("\n")

                    # wsd
                    filtered_sent = []
                    filtered_syn = []

                    counter = 0
                    similarity = 0

                    print(sent)
                    print(syn)
                    filtered_sent = simpleFilter(sent, token.text.lower())
                    filtered_syn = simpleFilter(syn, "")  # nonostante sia uno solo è una lista, quindi poi fai for
                    print("Simple first filter...")
                    print(filtered_sent)
                    print(filtered_syn)
                    print("\n")

                    # compare sent (every word of sentence) with syn (the synonym, only one word)
                    for i in filtered_sent:
                        for j in filtered_syn:
                            counter = counter + 1
                            similarity = similarity + simlilarityCheck(i, j)

                    print("similarity:")
                    print(similarity)
                    print("\n")
                    filtered_sent = []
                    filtered_syn = []

                    print(sent)
                    print(syn)
                    filtered_sent = filteredSentence(sent, token.text.lower())
                    filtered_syn = filteredSentence(syn, "")  # nonostante sia uno solo è una lista, quindi poi fai for
                    print("Second filter...")
                    print(filtered_sent)
                    print(filtered_syn)
                    print("\n")
                    sent_count = 0

                    for i in filtered_sent:
                        for j in filtered_syn:
                            if i == j:
                                sent_count = sent_count + 1

                    print("sent_count:")
                    print(sent_count)
                    print("\n")

                    scoring_dict[synset] = sent_count + similarity
                    print("punteggio per sinonimo " + syn)
                    print(sent_count + similarity)
                    print("\n")
                print("tabella dei punteggi di sinonimi del termine " + token.text)
                print(scoring_dict)
                print("\n")
                # save the synonym with higher score
                max = 0
                for syn in scoring_dict.keys():
                    if scoring_dict[syn] > max:
                        max = scoring_dict[syn]
                        best_syn = syn
                if max != 0:
                    print("il migliore è ")
                    print(best_syn)
                    print("\n")
                    best_syn_list.append(best_syn)
                    best_syn_name = best_syn.name()
                    index = best_syn_name.find(".")
                    best_syn_name_final = best_syn_name[:index]
                    # you don't want to substitute parts of words
                    # (example of wrong behaviour: if design substituted with plan -> redesign is substituted with replan)
                    if " " + token.text + " " in sent:
                        sent = sent.replace(" " + token.text + " ", " " + best_syn_name_final + " ")
                    elif " " + token.text + "," in sent:
                        sent = sent.replace(" " + token.text + ",", " " + best_syn_name_final + ",")
                    elif " " + token.text + "\n" in sent:
                        sent = sent.replace(" " + token.text + "\n", " " + best_syn_name_final + "\n")
                    print("frase diventa: ")
                    print(sent)
                    print("\n\n")

        print("\n")
        print("frase è diventata: ")
        print(sent)
        print("\n\n")
        output_file.write(sent + "\n")
    output_file.write("\n")
    toc1 = time.perf_counter() # time for single file
    output_file.write(f"Time for single file = {toc1 - tic1:0.4f} seconds = {(toc1 - tic1) / 60:0.4f} "
                      f"minutes = {((toc1 - tic1) / 60 / 60):0.4f} hours")



toc0 = time.perf_counter()  # time for all datasets
output_file.write("\n")
# if you execute the script only on one data set total time will be equal to single time
output_file.write(f"Time for all datasets = {toc0 - tic0:0.4f} seconds = {(toc0 - tic0) / 60:0.4f} "
                  f"minutes = {((toc0 - tic0) / 60 / 60):0.4f} hours")


