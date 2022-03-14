# wordnet nltk (similarities) + mine

import random
import nltk
import spacy
from nltk.corpus import wordnet
from spacy_wordnet.wordnet_annotator import WordnetAnnotator
import os
import time
import gensim.downloader
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors

nlp = spacy.load('en')

nlp.add_pipe(WordnetAnnotator(nlp.lang), after='tagger')

w2v_model = KeyedVectors.load_word2vec_format("SO_vectors_200.bin", binary=True)

stpwrd = nltk.corpus.stopwords.words('english')

new_stopwords = ["an", "ss", "I", "to", "in", "so", "that", "and", "-", "_", ",", ";", ".", ":", "?", "!", "1", "2",
                 "3", "4", "5", "6", "7", "8", "9", "0", "a", "e", "i", "o", "u", "b", "c", "d", "f", "g", "j", "k",
                 "h", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "w", "y", "z"]
stpwrd.extend(new_stopwords)

fix_words = []

fix_variations = {}

consonant = ["b", "c", "d", "f", "g", "j", "k", "h", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "w", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]


def replace_word_in_phrase(old_word, new_word, phrase):
    if " " + old_word + " " in phrase:
        phrase = phrase.replace(" " + old_word + " ", " " + new_word + " ")
    elif " " + old_word + "," in phrase:
        phrase = phrase.replace(" " + old_word + ",", " " + new_word + ",")
    elif old_word + " " in phrase:
        phrase = phrase.replace(old_word + " ", new_word + " ")
    elif " " + old_word in phrase:
        phrase = phrase.replace(" " + old_word, " " + new_word)
    elif " " + old_word + "\n" in phrase:
        phrase = phrase.replace(" " + old_word + "\n", " " + new_word + "\n")
    elif " " + old_word + "." in phrase:
        phrase = phrase.replace(" " + old_word + ".", " " + new_word + ".")
    else:
        phrase = phrase.replace(old_word, new_word)
    return phrase


def first_word(phrase, word):
    # return true if it's the first word of the phrase, False otherwise
    # some phrases begin with a space
    if phrase.find(word + " ") == 0 or phrase.find(word + ",") == 0 or phrase.find(
            " " + word + " ") == 0 or phrase.find(" " + word + ",") == 0:
        return True
    return False


def word_approved(token):
    if token.text.lower() not in stpwrd and token.text.lower() not in fix_words and not token.text.isnumeric() \
            and not token.text.isupper():  # and not (token.text[0].isupper() and not first_word(phrase, word)):
        # se scommenti non approvi (non sostituisci) parole con prima lettera maiuscola che non sono prima parola frase
        return True
    return False


def token_is_plural(token):
    if token.tag_ == "NNS" or token.tag_ == "NNPS":
        return True
    return False


def action_on_plural(syn):
    '''
    # not lemmatizing timeses
    if syn.endswith("s") or syn.endswith("ss") or syn.endswith("sh") or syn.endswith("ch") or syn.endswith("x") or\
            syn.endswith("z"):
        syn = syn + "es"
    elif syn.endswith("y"):
        y_index = syn.rfind("y") # find the index of y at the end of the word
        if syn[y_index-1] in consonant:
            # se finisce in y precededuta da consonante tolgo y e metto ies
            syn = syn[:y_index]
            syn = syn + "ies"
    else:
        syn = syn + "s"
    return syn
    '''
    # lemmatizing (times -> time -> times)
    processed_syn = nlp(syn)
    for p_syn in processed_syn:
        lemma_syn = p_syn.lemma_
    if lemma_syn.endswith("s") or lemma_syn.endswith("ss") or lemma_syn.endswith("sh") or lemma_syn.endswith(
            "ch") or lemma_syn.endswith("x") or \
            lemma_syn.endswith("z"):
        final_syn = lemma_syn + "es"
    elif lemma_syn.endswith("y"):
        y_index = lemma_syn.rfind("y")  # find the index of y at the end of the word
        if lemma_syn[y_index - 1] in consonant:
            # se finisce in y precededuta da consonante tolgo y e metto ies
            lemma_syn = lemma_syn[:y_index]
            final_syn = lemma_syn + "ies"
        else:  # vocale
            final_syn = lemma_syn + "s"
    else:
        final_syn = lemma_syn + "s"
    return final_syn


def token_is_past_participle(token):
    if token.tag_ == "VBN":
        return True
    return False


def action_on_past_participle(syn):
    '''
    if not syn.endswith("ed"):
        if syn.endswith("e"):
            syn = syn + "d"
        elif syn.endswith("y"):
            y_index = syn.rfind("y")
            syn = syn[:y_index]
            syn = syn + "ied"
        else:
            syn = syn + "ed"
    return syn
    '''
    processed_syn = nlp(syn)
    for p_syn in processed_syn:
        lemma_syn = p_syn.lemma_
    if lemma_syn.endswith("e"):
        final_syn = lemma_syn + "d"
    elif lemma_syn.endswith("y"):
        y_index = lemma_syn.rfind("y")
        lemma_syn = lemma_syn[:y_index]
        final_syn = lemma_syn + "ied"
    else:
        final_syn = lemma_syn + "ed"
    return final_syn


def token_is_third_singular(token):
    if token.tag_ == "VBZ":
        return True
    return False


def action_on_third_singular(syn):
    '''
    if syn.endswith("s") or syn.endswith("ss") or syn.endswith("sh") or syn.endswith("ch") or syn.endswith("x") or\
            syn.endswith("zz"):
        syn = syn + "es"
    elif syn.endswith("z"):
        syn = syn + "zes"
    elif syn.endswith("y"):
        y_index = syn.rfind("y") # find the index of y at the end of the word
        if syn[y_index-1] in consonant:
            # se finisce in y precededuta da consonante tolgo y e metto ies
            syn = syn[:y_index]
            syn = syn + "ies"
    # is has does goes and negatives ?
    else:
        # also if finisce in y preceduta da vocale
        syn = syn + "s"
    return syn
    '''
    processed_syn = nlp(syn)
    for p_syn in processed_syn:
        lemma_syn = p_syn.lemma_
    if lemma_syn.endswith("s") or lemma_syn.endswith("ss") or lemma_syn.endswith("sh") or lemma_syn.endswith(
            "ch") or lemma_syn.endswith("x") or \
            lemma_syn.endswith("zz"):
        final_syn = lemma_syn + "es"
    elif lemma_syn.endswith("z"):
        final_syn = lemma_syn + "zes"
    elif lemma_syn.endswith("y"):
        y_index = syn.rfind("y")  # find the index of y at the end of the word
        if lemma_syn[y_index - 1] in consonant:
            # se finisce in y precededuta da consonante tolgo y e metto ies
            lemma_syn = lemma_syn[:y_index]
            final_syn = lemma_syn + "ies"
        else:  # vocale
            final_syn = lemma_syn + "s"
        # is has does goes and negatives ?
    else:
        # also if finisce in y preceduta da vocale
        final_syn = lemma_syn + "s"
    return final_syn


def from_synset_to_string(synset):
    synset_name = synset.name()
    index = synset_name.find(".")
    synset_name_final = synset_name[:index]
    return synset_name_final


def second_best_wup_executor_func(filename, parameters_list, output_dict):
    """
       Function that executes Parrot augment function on a file
       :param parameters_list: list of parameters
       :param filename: name of the input file
       :param output_dict: dictionary at the beginning empty that will contain outputs
       :type filename: str
       :type output_dict: dict
       :return: A dictionary in which the keys are the inputs phrases and the values are the lists of relative outputs
       :rtype: dict

       """

    tic0 = time.perf_counter()  # time

    syn_vs_synsets = parameters_list[0]
    syn_vs_term = parameters_list[1]
    n_max = parameters_list[2]

    input_file = open(filename, "r")

    phrases = input_file.read().splitlines()
    for phrase in phrases:

        best_synset_dict = {}  # conterrà chiave:token valore:lista con primo migliore e secondo migliore se ci sono (vuota se non ci sono)
        paraphrase_list = []  # lista che conterrà parafrasi di frase corrente, sarà valore di chiave phrase nell'output dict che restituiamo alla fine

        tokens = nlp(phrase)
        # everything is a token apart from space

        synset_dict = {}
        for token in tokens:
            if word_approved(token):
                synset = wordnet.synsets(token.text)
                synset_dict[token.text] = synset

        # clean synset
        for token in tokens:
            done = False
            if word_approved(token):
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

        for token in tokens:
            syn_list = []  # sarà lista che conterrà - in caso vengano trovati - il primo e il secondo migliore
            if word_approved(token):
                # we don't want that modifying synsets leads to modify synset_dict[token.text]
                synsets = []
                for a in synset_dict[token.text]:
                    synsets.append(a)
                # for each token i have a dictionary to save the scoring of each of his synonym
                # scoring is similarity calculated summing single similarities of the synonym
                # with all other word
                scoring_dict = {}
                for synset in synsets:
                    scoring = 0
                    num_cmp = 0
                    for compare_token in tokens:
                        # to not compare a synonym with the original word of him uncomment below
                        # compare_token.text != token.text and
                        if word_approved(compare_token):
                            compare_synsets = synset_dict[compare_token.text]
                            for compare_synset in compare_synsets:
                                if from_synset_to_string(compare_synset) == compare_token.text.lower():
                                    compare_token_synset = compare_synset

                                if syn_vs_synsets:
                                    print('syn_vs_synsets')

                                    num_cmp = num_cmp + 1
                                    try:
                                        print("I'm comparing " + str(synset) + " with " + str(compare_synset))
                                        sim = synset.wup_similarity(compare_synset)
                                    except KeyError:
                                        sim = 0
                                    if sim:
                                        scoring = scoring + abs(sim)

                                elif syn_vs_term:
                                    print('syn_vs_term')

                                    num_cmp = num_cmp + 1
                                    try:
                                        print("I'm comparing " + str(synset) + " with " + str(compare_token_synset))
                                        sim = synset.wup_similarity(compare_token_synset)
                                    except KeyError:
                                        sim = 0
                                    if sim:
                                        scoring = scoring + abs(sim)

                    scoring_dict[synset] = scoring / num_cmp

                # save the synonym with higher score
                max = 0
                second = 0

                if token.text.lower() in fix_variations.keys():  # se ha sost fisso sia primo che secondo
                    # there are some words that are always subst by the same
                    syn_name_final = fix_variations[token.text.lower()]
                    syn_list.append(syn_name_final)
                    syn_list.append(syn_name_final)

                else:  # se non ha sostituti fissi cerca

                    for first_syn in scoring_dict.keys():
                        if scoring_dict[first_syn] > max and scoring_dict[first_syn] > 0.1:
                            max = scoring_dict[first_syn]
                            best_syn = first_syn

                    if max != 0:  # se hai trovato primo
                        print(best_syn)
                        best_syn_name_final = from_synset_to_string(best_syn)

                        # check if plural, if past participle, if third singular
                        if token_is_plural(token):
                            best_syn_name_final = action_on_plural(best_syn_name_final)
                        if token_is_past_participle(token):
                            best_syn_name_final = action_on_past_participle(best_syn_name_final)
                        if token_is_third_singular(token):
                            best_syn_name_final = action_on_third_singular(best_syn_name_final)

                        syn_list.append(best_syn_name_final)

                        # check if you find a second (only if you already found a first)
                        for second_syn in scoring_dict.keys():
                            second_syn_name_final = from_synset_to_string(second_syn)

                            # check if plural, if past participle, if third singular
                            if token_is_plural(token):
                                second_syn_name_final = action_on_plural(second_syn_name_final)
                            if token_is_past_participle(token):
                                second_syn_name_final = action_on_past_participle(second_syn_name_final)
                            if token_is_third_singular(token):
                                second_syn_name_final = action_on_third_singular(second_syn_name_final)

                            if scoring_dict[second_syn] > 0.1 and \
                                    scoring_dict[second_syn] > second and second_syn_name_final != best_syn_name_final:
                                second_best = second_syn
                                second = scoring_dict[second_syn]
                                second_best_name_final = second_syn_name_final

                        # it means I found a second best
                        if second != 0:
                            # append adds at the end, if there is a second it's in the second position
                            syn_list.append(second_best_name_final)

                # se una parola non ha nemmeno best syn non la valuto neanche per la sostituzione
                if syn_list:
                    best_synset_dict[token.text] = syn_list

        print(phrase)
        print(best_synset_dict)
        all_possible_subst = len(best_synset_dict)
        print("percentage: " + str(n_max))
        print("all possible subst: " + str(all_possible_subst))
        if n_max == 100:  # DEFAULT restituisco 1 frase tutti best, seconda un second, terza due seconds... fino a ultima tutti seconds
            replacements_number = all_possible_subst
        else:  # utente ha inserito numero massimo di sostituzioni in percentuale (voglio sostituire al massimo n_max per cetno di parole sostituibili)
            float_replacements_number = n_max * all_possible_subst / 100
            replacements_number = int(round(float_replacements_number, 0))
            if float_replacements_number > replacements_number:
                replacements_number = replacements_number + 1  # voglio sempre apprssimare per eccesso, meglio una frase in più che una in meno

        print("replacement number: " + str(replacements_number))

        # first phrase, all bests, no seconds
        phrase_bests = phrase  # se viene inserita percentuale 0 restituisco solo questa

        for word in best_synset_dict.keys():
            if best_synset_dict[word]:  # c'è almeno un elemento (ossia best) nella lista
                # se non trova best usa original
                phrase_bests = replace_word_in_phrase(word, best_synset_dict[word][0], phrase_bests)

        paraphrase_list.append(phrase_bests)
        print("0: " + phrase_bests)

        # return replacements_number - 1 phrases
        # first with one random word sub by the second
        # second with two random words sub by the seconds
        # repl_number - 1 th with repl_number - 1 words sub by the seconds

        '''
        # se vuoi che parole random che sostituisce in una stessa frase possano anche essere le stesse
        # prima frase random: sostituisci con second una parola a caso
        # seconda frase random: sost con second due parole a caso (non necessariamente diverse tra loro)
        # ...
        # fino a arrivare a sostituire numero totale di parole - 1 parole a caso (non necessariamente diverse tra loro)
        for i in range(1, replacements_number):
            phrase_random = phrase
            scoring_file.write("phrase_random" + "\n")
            for count in range(i):
                victim_index = random.randint(1, replacements_number)
                victim_word = list(best_synset_dict.keys())[victim_index - 1]
                if len(best_synset_dict[victim_word]) == 2:  # ci sono due elementi nella lista, quindi c'è second
                    phrase_random = replace_word_in_phrase(victim_word, best_synset_dict[victim_word][1], phrase_random)
                elif len(best_synset_dict[victim_word]) == 1:  # c'è primo
                    phrase_random = replace_word_in_phrase(victim_word, best_synset_dict[victim_word][0], phrase_random)
            output_file.write(phrase_random + "\n")
            scoring_file.write(phrase_random + "\n")
        '''

        # parole random che sostituisce in una frase sempre diverse (estrazione a caso la fai in array da cui via via togli elementi)
        # prima frase random: sostituisci con second una parola a caso
        # seconda frase random: sost con second due parole a caso (diverse tra loro)
        # ...
        # fino a arrivare a sostituire numero totale di parole - 1 parole a caso (diverse tra loro)

        for i in range(1, replacements_number + 1):  # non arriva mai a replacements_number
            phrase_random = phrase
            replacements_index_list = []
            for tmp in range(1, all_possible_subst + 1):
                replacements_index_list.append(tmp)
            for count in range(i):
                index = random.randint(0, len(replacements_index_list) - 1)
                victim_index = replacements_index_list.pop(index)
                victim_word = list(best_synset_dict.keys())[victim_index - 1]
                if len(best_synset_dict[victim_word]) == 2:  # ci sono due elementi nella lista, quindi c'è second
                    phrase_random = replace_word_in_phrase(victim_word, best_synset_dict[victim_word][1], phrase_random)
                elif len(best_synset_dict[victim_word]) == 1:  # first
                    phrase_random = replace_word_in_phrase(victim_word, best_synset_dict[victim_word][0], phrase_random)
            print(str(i) + ": " + phrase_random)
            paraphrase_list.append(phrase_random)

    output_dict[phrase] = paraphrase_list

    toc0 = time.perf_counter()


