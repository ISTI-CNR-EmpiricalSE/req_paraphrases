import time
import spacy
import nltk
from nltk.tokenize import word_tokenize
from nltk import map_tag
from nltk.corpus import wordnet
from spacy_wordnet.wordnet_annotator import WordnetAnnotator


def no_context_executor_func(filename, parameters_list, output_dict):
    """Function that replaces the non stop words found in each sentence with the all synonyms found with worndet
        Produce an output file that is put inside the directory results, inside the directory of the relative dataset
        Format of the input file: results_file_index.txt (which was the output of parrot_test_func)
        Format of the output file: results_data_set_index_wordnet.txt
    """
    always_subst = parameters_list[0]

    nlp = spacy.load('en')

    nlp.add_pipe(WordnetAnnotator(nlp.lang), after='tagger')

    stpwrd = nltk.corpus.stopwords.words('english')
    new_stopwords = ["an", "ss", "I", "to", "in", "so", "that", "and", "-", "_", ",", ";", ".", ":", "?", "!"]
    stpwrd.extend(new_stopwords)

    tic0 = time.perf_counter()

    input_file = open(filename, "r")
    phrases = input_file.read().splitlines()
    for phrase in phrases:
        tokens = word_tokenize(phrase)
        print(tokens)

        tagged_tokens = nltk.pos_tag(tokens)
        print(tagged_tokens)
        simplified_tagged_tokens = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in tagged_tokens]
        print(simplified_tagged_tokens)

        phrases_list = []
        for s_tagged_token in simplified_tagged_tokens:
            # replace synonym only of words that are not stopwords
            token_text = s_tagged_token[0]
            print(token_text)
            token_pos = s_tagged_token[1]
            print(token_pos)

            if (token_text.lower() not in stpwrd) and \
                (token_pos == "NOUN" or token_pos == "VERB" or token_pos == "ADJ" or token_pos == "ADV") and \
                    not token_text.isnumeric():
                # wordnet object link spacy token with nltk wordnet interface by giving access to synonyms

                syns_dirty = wordnet.synsets(token_text)

                print(syns_dirty)
                print("\n")

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
                    if always_subst:  # non lo uso se è uguale a parola originale, significa che parole cambiano sempre
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

        output_dict[phrase] = phrases_list

    toc0 = time.perf_counter()

