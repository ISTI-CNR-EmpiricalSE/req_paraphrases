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

# good = wordnet.synset('good.a.01')
# print(good)

synset_dict = {}
for token in tokens:
    if token.text.lower() not in stpwrd and not token.text.isnumeric():
        synset = wordnet.synsets(token.text)
        synset_dict[token.text] = synset

# print(synset_dict)

# clean synset
for token in tokens:
    if token.text.lower() not in stpwrd and not token.text.isnumeric() and \
            (token.pos_ == "ADJ" or token.pos_ == "ADV" or token.pos_ == "NOUN" or token.pos_ == "VERB"):
        p = ""
        if token.pos_ == "ADJ":
            p = "a"
        elif token.pos_ == "ADV":
            p = "r"
        elif token.pos_ == "NOUN":
            p = "n"
        elif token.pos_ == "VERB":
            p = "v"
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
                # put the equal one in front cause you'll need this to compare, but do this just once
            synset_dict[token.text].insert(0, wordnet.synset(token.text.lower() + '.' + p + '.01'))

print(synset_dict)

best_syn_list = []

for token in tokens:
    if token.text.lower() not in stpwrd and not token.text.isnumeric():
        synonyms = synset_dict[token.text]
        scoring_dict = {}
        if synonyms:
            synonyms.pop(0)
        for syn in synonyms:
            scoring = 0
            for compare_token in tokens:
                if compare_token.text != token.text and compare_token.text.lower() not in stpwrd and not compare_token.text.isnumeric():
                    word_synset = synset_dict[compare_token.text]
                    if word_synset:
                        token_syn_format = word_synset[0]
                        sim = syn.wup_similarity(token_syn_format)
                        if sim:
                            scoring = scoring + sim
            scoring_dict[syn] = scoring
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
path similarity
Synset('datum.n.01')
Synset('drug_user.n.01')
Synset('desire.v.01')
Synset('march.v.01')
As a datum drug_user, I desire to have the 12-19-2017 deletions march.
'''

'''
lch_similarity
Traceback (most recent call last):
  File "/home/isabella/PycharmProjects/req_paraphrases/best_synonym.py", line 61, in <module>
    sim = syn.lch_similarity(token_syn_format)
  File "/home/isabella/anaconda3/envs/req_paraphrases/lib/python3.9/site-packages/nltk/corpus/reader/wordnet.py", line 835, in lch_similarity
    raise WordNetError(
nltk.corpus.reader.wordnet.WordNetError: Computing the lch similarity requires Synset('datum.n.01') and Synset('want.v.02') to have the same part of speech.
non posso confrontare cose che hanno diverso pos ?????????????????????????????
'''

'''
wup_similarity
Synset('datum.n.01')
Synset('drug_user.n.01')
Synset('desire.v.01')
Synset('march.v.01')
As a datum drug_user, I desire to have the 12-19-2017 deletions march.
'''
