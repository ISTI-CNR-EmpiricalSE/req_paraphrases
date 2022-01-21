from nltk.corpus import wordnet as wn

word = "refresh"
synsets = wn.synsets(word)

sense2freq = {}
for s in synsets:
  freq = 0
  lemmas = s.lemmas()
  for lemma in lemmas:
    freq+=lemma.count()
  sense2freq[str(s.offset()) + "-" + s.pos()] = freq

for s in synsets:
  print(s, sense2freq[str(s.offset()) + "-" + s.pos()])

'''
Synset('user.n.01') 3
Synset('exploiter.n.01') 1
Synset('drug_user.n.01') 0

Synset('omission.n.03') 1
Synset('deletion.n.02') 0
Synset('deletion.n.03') 0
Synset('deletion.n.04') 0

Synset('agency.n.01') 48
Synset('agency.n.02') 6
Synset('agency.n.03') 1
Synset('representation.n.04') 0
Synset('means.n.01') 111

Synset('review.v.04') 1
Synset('refresh.v.02') 0
Synset('freshen.v.02') 0
Synset('refresh.v.04') 0
'''