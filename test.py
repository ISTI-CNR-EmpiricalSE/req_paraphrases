from nltk.corpus import wordnet

syn1 = wordnet.synsets('hello')[0]
syn2 = wordnet.synsets('running', pos="v")[0]

print(syn1.name())
print(syn2.name())

print(syn1.lch_similarity(syn2))