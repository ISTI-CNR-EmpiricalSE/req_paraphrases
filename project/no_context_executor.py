import time
import spacy
import nltk
from nltk.tokenize import word_tokenize
from nltk import map_tag
from nltk.corpus import wordnet
from spacy_wordnet.wordnet_annotator import WordnetAnnotator
import time

nlp = spacy.load('en')
nlp.add_pipe(WordnetAnnotator(nlp.lang), after='tagger')

stpwrd = nltk.corpus.stopwords.words('english')
new_stopwords = ["an", "ss", "I", "to", "in", "so", "that", "and", "-", "_", ",", ";", ".", ":", "?", "!"]
stpwrd.extend(new_stopwords)


def no_context_executor_func(filename: str, parameters_list: list, output_dict: dict):
    """
    Function that systematically and non contextually replaces the non stop words found in each sentence with the all
    synonyms found with WordNet
    If the flag always_subst in the list of parameters configured by the user is set to True synonyms equal to the
    original word are not put in the list of synonyms, so a term will always be replaced by a different word, obtaining
    more variation.
    :param filename: name of the input file
    :param parameters_list: list of parameters configured by the user [always_subst]
    :param output_dict: dictionary that will contain the outputs {input_1: [output_1.1, output_1.2...], input_2...}
    :return:
    """
    tic = time.perf_counter()
    always_subst = parameters_list[0]   # configurable (default: False)


    input_file = open(filename, "r")
    phrases = input_file.read().splitlines()

    for phrase in phrases:

        tokens = word_tokenize(phrase)

        tagged_tokens = nltk.pos_tag(tokens)

        simplified_tagged_tokens = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in tagged_tokens]

        phrases_list = []

        for s_tagged_token in simplified_tagged_tokens:

            token_text = s_tagged_token[0]
            token_pos = s_tagged_token[1]

            if (token_text.lower() not in stpwrd) and \
                (token_pos == "NOUN" or token_pos == "VERB" or token_pos == "ADJ" or token_pos == "ADV") and \
                    not token_text.isnumeric():
                # replace synonym only of words that are not stopwords

                syns_dirty = wordnet.synsets(token_text)

                syns_clean = []

                for i in syns_dirty:
                    # format: synonym.stuff
                    synonym_dirty = i.name()

                    # take off from first "."
                    index = synonym_dirty.find(".")
                    synonym = synonym_dirty[:index]

                    # insert synonym in final list only if :
                    # if absent from the final list
                    found = False
                    if always_subst:  # insert synonym only if it's different from original
                        if synonym == token_text.lower():
                            found = True
                        if synonym[:len(synonym) - 1] == token_text.lower():
                            found = True
                        if synonym == token_text.lower()[:len(token_text) - 1]:
                            found = True
                    if synonym in syns_clean:
                        found = True
                    if found is False:
                        syns_clean.append(synonym)

                    # NB: SE NON SONO IN ALWAYS_SUBST -> SE È UGUALE A PAROLA ORIGINARIA LO INSERISCO LO STESSO
                    #     SE SONO IN ALWAYS_SUBST -> SE È UGUALE A PAROLA ORIGINARIA NON LO INSERISCO

                print(token_text)
                print(syns_clean)
                print("\n")
                # it returns as many phrases as many synonyms have the word that has more synonyms in the phrase
                # until it finds synonyms it keeps substituting them
                if not always_subst:
                    phrases_list_tmp = []
                    phrases_list_iterator = []
                    for phrase_iter in phrases_list:
                        phrases_list_iterator.append(phrase_iter)
                    for old_phrase in phrases_list_iterator:
                        if len(syns_clean) > 0:
                            old_phrase_tmp = old_phrase
                            new_phrase = old_phrase_tmp.replace(token_text, syns_clean[0])
                            phrases_list_tmp.append(new_phrase)
                            phrases_list.remove(old_phrase_tmp)
                            syns_clean.pop(0)
                    if phrases_list_tmp:
                        if len(phrases_list) == 0:
                            phrases_list = phrases_list_tmp
                        else:
                            phrases_list = phrases_list + phrases_list_tmp
                    while syns_clean:
                        phrase_res = phrase.replace(token_text, syns_clean[0])
                        phrases_list.append(phrase_res)
                        syns_clean.pop(0)

                elif always_subst:
                    print("here")
                    phrase_res = phrase
                    phrases_list_tmp = []
                    phrases_list_iterator = []
                    for phrase_iter in phrases_list:
                        phrases_list_iterator.append(phrase_iter)
                    for old_phrase in phrases_list_iterator:
                        if len(syns_clean) > 0:
                            old_phrase_tmp = old_phrase
                            new_phrase = old_phrase_tmp.replace(token_text, syns_clean[0])
                            phrases_list_tmp.append(new_phrase)
                            phrases_list.remove(old_phrase_tmp)
                            token_text = syns_clean.pop(0)
                    if phrases_list_tmp:
                        if len(phrases_list) == 0:
                            phrases_list = phrases_list_tmp
                        else:
                            phrases_list = phrases_list + phrases_list_tmp
                    while syns_clean:
                        if phrases_list:
                            phrase_res = phrases_list[-1].replace(token_text, syns_clean[0])
                            phrases_list.append(phrase_res)
                        else:
                            phrase_res = phrase_res.replace(token_text, syns_clean[0])
                            phrases_list.append(phrase_res)
                        token_text = syns_clean.pop(0)

        output_dict[phrase] = phrases_list

    toc = time.perf_counter()
    print(f"{toc - tic:0.4f} seconds")


if __name__ == "__main__":
    dict = {}
    tic = time.perf_counter()
    no_context_executor_func("../finto_data_set.txt", [True], dict)
    toc = time.perf_counter()
    print(f"{toc - tic:0.4f} seconds")
    print(dict)
