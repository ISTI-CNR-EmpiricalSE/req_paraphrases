# A simple Word Sense Disambiguation application

# This module is for word sense disambiguation.
# Give 2 sentences with some data.
# give a third sentence and the program will analyse which sentence you are relating to.


import nltk
import codecs
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import wordnet

# -----------------------------------------------------------------------------------

# Remove Stop Words . Word Stemming . Return new tokenised list.


def filteredSentence(sentence):

    filtered_sent = []
    lemmatizer = WordNetLemmatizer()  # lemmatizes the words
    ps = PorterStemmer()  # stemmer stems the root of the word.

    stop_words = set(stopwords.words("english"))
    words = word_tokenize(sentence)

    for w in words:
        if w not in stop_words:
            filtered_sent.append(lemmatizer.lemmatize(ps.stem(w)))
            for i in synonymsCreator(w):
                filtered_sent.append(i)
    return filtered_sent

# --------------------------------------------------------------------------------------

# Add synonyms to match list


def synonymsCreator(word):
    synonyms = []

    for syn in wordnet.synsets(word):
        for i in syn.lemmas():
            synonyms.append(i.name())

    return synonyms

# ---------------------------------------------------------------------------------------

# Cehck and return similarity


def simlilarityCheck(word1, word2):

    word1 = word1 + ".n.01"
    word2 = word2 + ".n.01"
    try:
        w1 = wordnet.synset(word1)
        w2 = wordnet.synset(word2)

        return w1.wup_similarity(w2)

    except:
        return 0

# -----------------------------------------------------------------------------------------


def simpleFilter(sentence):

    filtered_sent = []
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(sentence)

    for w in words:
        if w not in stop_words:
            filtered_sent.append(lemmatizer.lemmatize(w))
            # for i in synonymsCreator(w):
            # 	filtered_sent.append(i)
    return filtered_sent


if __name__ == '__main__':

    sent = "As a Data user, I want to have the 12-19-2017 deletions processed."
    syn = "user"

    filtered_sent = []
    filtered_syn = []

    counter = 0
    similarity = 0

    print(sent)
    print(syn)
    filtered_sent = simpleFilter(sent)
    filtered_syn = simpleFilter(syn)  # nonostante sia uno solo è una lista, quindi poi fai for
    print("Simple first filter...")
    print(filtered_sent)
    print(filtered_syn)
    print("\n")

    # compare sent (every word of sentence) with syn (the synonym, only one word)
    for i in filtered_sent:
        for j in filtered_syn:
            counter = counter + 1
            similarity = similarity + simlilarityCheck(i, j)

    filtered_sent = []

    print(sent)
    print(syn)
    filtered_sent = filteredSentence(sent)
    filtered_syn = filteredSentence(syn)  # nonostante sia uno solo è una lista, quindi poi fai for
    print("Second filter...")
    print(filtered_sent)
    print(filtered_syn)
    print("\n")
    sent_count = 0

    for i in filtered_sent:
        for j in filtered_syn:
            if i == j:
                sent_count = sent_count + 1

    print(sent_count + similarity)

print("\nTERMINATED")