import spacy
from spacy_wordnet.wordnet_annotator import WordnetAnnotator
import nltk

from nltk.corpus import stopwords
print(stopwords.words('english'))
stpwrd = nltk.corpus.stopwords.words('english')
new_stopwords = ["an", "ss", "I", "to", "in", "so", "that", "and"]
stpwrd.extend(new_stopwords)

nlp = spacy.load('en')

nlp.add_pipe(WordnetAnnotator(nlp.lang), after='tagger')

phrase = "As an archivist, I want to automatically embed metadata in file headers, so that I avoid repetitive and easily-forgotten tasks."
doc = nlp(phrase)

for token in doc:
    # replace synonym only of words that are not stopwords
    if token.text.lower() not in stpwrd:
        # wordnet object link spacy token with nltk wordnet interface by giving acces to
        # synsets
        syns_dirty = token._.wordnet.synsets()

        syns_clean = []

        for i in syns_dirty:
            # formato: synonym.roba
            name_dirty = i.name()

            # take off from first "."
            index = name_dirty.find(".")
            name = name_dirty[:index]

            # insert synonym in final list only if it's different from original word and if absent from the final list
            found = False
            if name == token.text:
                found = True
            for j in syns_clean:
                if name == j:
                    found = True
            if found is False:
                syns_clean.append(name)

        print(token.text)
        print(syns_clean)
        print("\n")

        if syns_clean:
            # replace the word with the first of the list because it's usually better
            phrase = phrase.replace(token.text, syns_clean[0])

print(phrase)




