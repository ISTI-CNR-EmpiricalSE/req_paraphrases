import random
import time
import spacy
from nltk.corpus import wordnet
from spacy_wordnet.wordnet_annotator import WordnetAnnotator
from gensim.models.keyedvectors import KeyedVectors
from helper import word_approved, from_synset_to_string, fix_variations, replace_word_in_phrase, \
    token_is_plural, token_is_past_participle, token_is_third_singular, \
    action_on_plural, action_on_past_participle, action_on_third_singular

nlp = spacy.load('en')
nlp.add_pipe(WordnetAnnotator(nlp.lang), after='tagger')

# load the model
w2v_model = KeyedVectors.load_word2vec_format("SO_vectors_200.bin", binary=True)


def second_best_wup_executor_func(filename, parameters_list, output_dict):
    """
    Function that replaces terms with their second best synonym according to the context.
    The second best synonym is the synonym with the second higher score.
    If the syn_vs_synsets flag in the list of parameters configured by the user is set to True the score of a synonym
    is calculated comparing the synonym with the original terms of the phrase and their synonyms by the
    wup_similarity() of method of WordNet, summing single similarities and dividing the result by the number of
    comparisons.
    Otherwise, if the syn_vs_term flag is set to True the score of a synonym is calculated comparing the synonym with
    the original terms of the phrase by the wup_similarity() method of WordNet, summing single similarities
    and dividing the result by the number of comparisons.
    The similarity method returns a number between 0 and 1.
    If no synonym score is greater than 0.1, then no synonym will be selected to be the second best synonym.
    The i-th output phrase is the original phrase with i terms replaced by their best synonyms.
    The configurable parameter n_max indicates the percentage of replaced terms.
    NOTE: the first output phrase is the original phrase with all approved terms replaced with the best syn
    from the second phrase second best synonyms start to be employed for substitution, anyways if a term doesn't have a
    second best synonym (no synonym different from the best with a score > 0.1 was found) then first best synonyms will
    be employed, so this program also look for best synonyms.
    If neither first best synonym is found (no synonym with a score > 0.1), the word is not replaced.
    (if n_max == 100 the last phrase is the original phrase with all approved terms replaced by their best synonym)
    :param filename: name of the input file
    :param parameters_list: list of parameters configured by the user [syn_vs_synsets, syn_vs_term, n_max]
    :param output_dict: dictionary that will contain the outputs {input_1: [output_1.1, output_1.2...], input_2...}
    :return:
    """

    tic0 = time.perf_counter()  # time

    syn_vs_synsets = parameters_list[0]  # configurable
    syn_vs_term = parameters_list[1]  # configurable
    n_max = parameters_list[2]  # configurable (default: 100)

    input_file = open(filename, "r")

    phrases = input_file.read().splitlines()
    for phrase in phrases:

        best_synset_dict = {}  # {token_1: [best_syn_1], token_2: [best_syn_1], ...}
        paraphrase_list = []  # list of paraphrased phrases that will be put as value in output_dict

        tokens = nlp(phrase)

        synset_dict = {}  # {token1: [synsets of token1], ...}
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
                    if synonym == token.text.lower() or synonym[:len(synonym) - 1] == token.text.lower() or \
                            synonym == token.text.lower()[:len(token.text) - 1] or \
                            synonym[:len(synonym) - 2] == token.text.lower() or \
                            synonym == token.text.lower()[:len(token.text) - 2]:
                        synset_dict[token.text].remove(syn)
                        # put the equal one in front, but do this just once
                        if synonym == token.text.lower() and not done:
                            done = True
                            synset_dict[token.text].insert(0, syn)

        for token in tokens:
            syn_list = []  # this will contain the best synonym and the second best synonym (in case they are found)
            if word_approved(token):
                # we don't want that modifying synsets leads to modify synset_dict[token.text] so we create a copy
                synsets = []
                for a in synset_dict[token.text]:
                    synsets.append(a)
                # for each token i have a dictionary to save the scoring of each of his synonym
                # scoring is similarity calculated summing single similarities of the synonym divided by num_cmp
                scoring_dict = {}
                for synset in synsets:
                    scoring = 0
                    num_cmp = 0
                    for compare_token in tokens:
                        if word_approved(compare_token):
                            compare_synsets = synset_dict[compare_token.text]
                            for compare_synset in compare_synsets:
                                if from_synset_to_string(compare_synset) == compare_token.text.lower():
                                    compare_token_synset = compare_synset

                                if syn_vs_synsets:

                                    num_cmp = num_cmp + 1

                                    try:
                                        # comparing synset with compare_synset
                                        sim = synset.wup_similarity(compare_synset)
                                    except KeyError:
                                        sim = 0
                                    if sim:
                                        scoring = scoring + abs(sim)

                                elif syn_vs_term:

                                    num_cmp = num_cmp + 1

                                    try:
                                        # compare synset with compare_token_synset
                                        sim = synset.wup_similarity(compare_token_synset)
                                    except KeyError:
                                        sim = 0
                                    if sim:
                                        scoring = scoring + abs(sim)

                    scoring_dict[synset] = scoring / num_cmp

                # save the synonym with higher score
                max = 0
                second = 0

                if token.text.lower() in fix_variations.keys():
                    # fix_variations
                    syn_name_final = fix_variations[token.text.lower()]
                    syn_list.append(syn_name_final)
                    syn_list.append(syn_name_final)

                else:
                    # no fix_variations
                    for first_syn in scoring_dict.keys():
                        if scoring_dict[first_syn] > max and scoring_dict[first_syn] > 0.1:
                            max = scoring_dict[first_syn]
                            best_syn = first_syn

                    if max != 0:  # # you found the best synonym
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

                        # save the synonym with second higher score (only if you already found a first)
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
                                second = scoring_dict[second_syn]
                                second_best_name_final = second_syn_name_final

                        # it means I found a second best
                        if second != 0:
                            # append adds at the end, if there is a second it's in the second position
                            syn_list.append(second_best_name_final)

                # if a token does not even have a best (syn_list is empty) it will not be replaced
                if syn_list:
                    best_synset_dict[token.text] = syn_list

        # first phrase, all bests, no seconds - if n_max == 0 this is the only output phrase
        phrase_bests = phrase

        for word in best_synset_dict.keys():
            if best_synset_dict[word]:  # there is at least one element (first best) in the list
                phrase_bests = replace_word_in_phrase(word, best_synset_dict[word][0], phrase_bests)

        paraphrase_list.append(phrase_bests)

        all_possible_subst = len(best_synset_dict)
        if n_max == 100:  # DEFAULT
            replacements_number = all_possible_subst
        else:
            float_replacements_number = n_max * all_possible_subst / 100
            replacements_number = int(round(float_replacements_number, 0))
            # approximation by excess (it's better to have a phrase in excess than a missing phrase)
            if float_replacements_number > replacements_number:
                replacements_number = replacements_number + 1

        # return replacements_number - 1 phrases
        # first with one random word replaced
        # second with two (DIFFERENT) random words replaced
        # ...
        # replacements_number - 1 th with replacements_number - 1 (DIFFERENT) words replaced

        for i in range(1, replacements_number + 1):  # non arriva mai a replacements_number
            phrase_random = phrase
            replacements_index_list = []
            for tmp in range(1, all_possible_subst + 1):
                replacements_index_list.append(tmp)
            for count in range(i):
                index = random.randint(0, len(replacements_index_list) - 1)
                victim_index = replacements_index_list.pop(index)
                victim_word = list(best_synset_dict.keys())[victim_index - 1]
                if len(best_synset_dict[victim_word]) == 2:  # second
                    phrase_random = replace_word_in_phrase(victim_word, best_synset_dict[victim_word][1], phrase_random)
                elif len(best_synset_dict[victim_word]) == 1:  # in case there is no second, you try to use the first
                    phrase_random = replace_word_in_phrase(victim_word, best_synset_dict[victim_word][0], phrase_random)
                # in case there is not even first you don't replace
            paraphrase_list.append(phrase_random)

        output_dict[phrase] = paraphrase_list

    toc0 = time.perf_counter()
