import nltk
import spacy
from nltk.corpus import wordnet
from spacy_wordnet.wordnet_annotator import WordnetAnnotator

stpwrd = nltk.corpus.stopwords.words('english')
new_stopwords = ["an", "ss", "I", "to", "in", "so", "that", "and", "-", "_", ",", ";", ".", ":", "?", "!", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0" ]
stpwrd.extend(new_stopwords)

nlp = spacy.load('en')
nlp.add_pipe(WordnetAnnotator(nlp.lang), after='tagger')

phrase = "As a Data user, I want to have the 12-19-2017 deletions processed."
tokens = nlp(phrase)
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

print(synset_dict)
best_syn_list = []

for token in tokens:
    if token.text.lower() not in stpwrd and not token.text.isnumeric():
        synsets = synset_dict[token.text]
        # for each token i have a dictionary to save the scoring of each of his synonym
        # scoring is similarity calculated summing single similarities of the synonym
        # with all (not his original) the synsets of other words
        scoring_dict = {}
        for synset in synsets:
            scoring = 0
            for compare_token in tokens:
                # i'm not comparing a synonym with the original word of him
                # because often in the synonyms there is also the original word, it is obvious that it would win
                if compare_token.text != token.text and compare_token.text.lower() not in stpwrd and not compare_token.text.isnumeric():
                    compare_synsets = synset_dict[compare_token.text]
                    if compare_synsets:
                        for compare_synset in compare_synsets:
                            print(synset)
                            print(compare_token.text)
                            print(compare_synset)
                            # with lch you need to have synset pos = compare_synset pos
                            sim = synset.lch_similarity(compare_synset)
                            print(sim)
                            # it could not exists a path that connects, if you put simulate root true it always exists
                            if sim:
                                scoring = scoring + sim
            scoring_dict[synset] = scoring
        print(scoring_dict)
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
            phrase = phrase.replace(token.text, best_syn_name_final)

print(phrase)


'''
putting (if exists FIX THIS) the equal to original (eto) synonym in front
comparing all synonyms of a word (ALSO the eto) with all synonyms of all other words (not his original word)
'''

'''
path similarity
simulate root = true
As a data user, I desire to have the 12-19-2017 omission march.
simulate root = false
As a data user, I need to have the 12-19-2017 omission processed.
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
simulate root = true
As a data user, I desire to have the 12-19-2017 omission march.
simulate root = false
As a data user, I need to have the 12-19-2017 omission processed.
'''

'''
putting (if exists FIX THIS) the equal to original (eto) synonym in front
comparing all synonyms of a word (NOT the eto) with all synonyms of all other words (not his original word)
drug user wins on exploiter -> compare also the eto (if the original was better just don't change it)
'''
