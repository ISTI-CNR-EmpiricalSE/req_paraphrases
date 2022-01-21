import nltk
import spacy
from nltk.corpus import wordnet
from spacy_wordnet.wordnet_annotator import WordnetAnnotator
from nltk.corpus import wordnet_ic

nlp = spacy.load('en')
nlp.add_pipe(WordnetAnnotator(nlp.lang), after='tagger')

tokens = nlp("user")
brown_ic = wordnet_ic.ic('ic-brown.dat') # how do you create a context file from your file?
# token_slap = nlp("drug_user")
# hit = wordnet.synset('hit.v.01')
# slap = wordnet.synset('slap.v.01')
for token in tokens:
    syns = token._.wordnet.synsets()
# for token in token_slap:
    # slap = token._.wordnet.synsets()
    print("Synonyms of the token: " + token.text)
    token_syn_format = syns[0]
    syns.pop(0)
    print(syns)
    print("\n")
    # print(slap)
    max = 0
    best_syn = None
    for syn in syns:
        print("Comparing " + str(token_syn_format) + " with " + str(syn))
        similarity = syn.res_similarity(token_syn_format, brown_ic)
        print(similarity)
        if similarity > max:
            max = similarity
            best_syn = syn
        print("\n")

print(best_syn)
print(max)


'''
path similarity

Synonyms of the token: user
[Synset('user.n.01'), Synset('exploiter.n.01'), Synset('drug_user.n.01')]


Comparing Synset('user.n.01') with Synset('user.n.01')
1.0


Comparing Synset('user.n.01') with Synset('exploiter.n.01')
0.16666666666666666


Comparing Synset('user.n.01') with Synset('drug_user.n.01')
0.3333333333333333
'''

'''
lch_similarity

Synonyms of the token: user
[Synset('user.n.01'), Synset('exploiter.n.01'), Synset('drug_user.n.01')]


Comparing Synset('user.n.01') with Synset('user.n.01')
3.6375861597263857


Comparing Synset('user.n.01') with Synset('exploiter.n.01')
1.845826690498331


Comparing Synset('user.n.01') with Synset('drug_user.n.01')
2.538973871058276
'''

'''
wup_similarity
Synonyms of the token: user
[Synset('exploiter.n.01'), Synset('drug_user.n.01')]


Comparing Synset('user.n.01') with Synset('exploiter.n.01')
0.631578947368421


Comparing Synset('user.n.01') with Synset('drug_user.n.01')
0.75
'''
