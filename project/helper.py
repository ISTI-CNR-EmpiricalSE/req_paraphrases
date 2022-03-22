import nltk
import spacy
from spacy_wordnet.wordnet_annotator import WordnetAnnotator
nlp = spacy.load('en')
nlp.add_pipe(WordnetAnnotator(nlp.lang), after='tagger')

# stopwords
stpwrd = nltk.corpus.stopwords.words('english')
new_stopwords = ["an", "ss", "I", "to", "in", "so", "that", "and", "-", "_", ",", ";", ".", ":", "?", "!", "1", "2",
                 "3", "4", "5", "6", "7", "8", "9", "0", "a", "e", "i", "o", "u", "b", "c", "d", "f", "g", "j", "k",
                 "h", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "w", "y", "z"]
stpwrd.extend(new_stopwords)

fix_words = ["member", "members", "user", "users", "clean", "account", "accounts", "file", "files", "cached", "code",
             "codes", "processed", "new", "report", "reports", "agency", "agencies", "transaction", "transactions",
             "application", "applications", "mail", "mails", "system", "systems", "software", "time", "model", "models"
                                                                                                               "problem",
             "problems", "set", "sets"]

fix_variations = {"get": "receive", "color": "semblance", "second": "moment", "seconds": "moments",
                  "product": "merchandise", "products": "merchandises", "data": "information", "information": "data",
                  "informations": "data", "function": "routine", "functions": "routines", "method": "procedure",
                  "methods": "procedures", "computer": "calculator", "computers": "calculators",
                  "deletion": "cancellation", "deletions": "cancellations"}

consonant = ["b", "c", "d", "f", "g", "j", "k", "h", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "w", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]


def replace_word_in_phrase(old_word: str, new_word: str, phrase: str):
    """
    Helper function that replaces old_word with new_word in phrase
    :param old_word: word to be replaced
    :param new_word: word that replaces
    :param phrase: sentence containing words
    :return:
    """
    if " " + old_word + " " in phrase:
        phrase = phrase.replace(" " + old_word + " ", " " + new_word + " ")
    elif " " + old_word + "," in phrase:
        phrase = phrase.replace(" " + old_word + ",", " " + new_word + ",")
    elif old_word + " " in phrase:
        phrase = phrase.replace(old_word + " ", new_word + " ")
    elif " " + old_word in phrase:
        phrase = phrase.replace(" " + old_word, " " + new_word)
    elif " " + old_word + "\n" in phrase:
        phrase = phrase.replace(" " + old_word + "\n", " " + new_word + "\n")
    elif " " + old_word + "." in phrase:
        phrase = phrase.replace(" " + old_word + ".", " " + new_word + ".")
    else:
        phrase = phrase.replace(old_word, new_word)
    return phrase


def first_word(phrase: str, word: str):
    """
    Helper function that return True if word is the first word in phrase, False otherwise
    :param phrase: phrase containing word
    :param word: word that we want to know if it's the first
    :return: bool
    """
    if phrase.find(word + " ") == 0 or phrase.find(word + ",") == 0 or phrase.find(
            " " + word + " ") == 0 or phrase.find(" " + word + ",") == 0:
        return True
    return False


def word_approved(token):
    """
    Helper function that return True if token is approved and can be processed, False otherwise.
    A token is approved if it is not a stop word, if it is not in fix_words list, if it is not numeric, if it is not
    an acronym (isupper)
    :param token: token that we want to know if is approved
    :return: bool
    """
    if token.text.lower() not in stpwrd and token.text.lower() not in fix_words and not token.text.isnumeric() \
            and not token.text.isupper():
        return True
    return False


def token_is_plural(token):
    """
    Helper function that returns True if a token is plural, False otherwise
    :param token: token that we want to know if it's plural
    :return: bool
    """
    if token.tag_ == "NNS" or token.tag_ == "NNPS":
        return True
    return False


def action_on_plural(syn: str):
    """
    Helper function that transforms a word in his plural version using lemmatization
    :param syn: word that we want to put in plural form
    :return:
    """
    # process word
    processed_syn = nlp(syn)
    # lemmatize word
    for p_syn in processed_syn:
        lemma_syn = p_syn.lemma_
    # put in plural form according to english language rules
    if lemma_syn.endswith("s") or lemma_syn.endswith("ss") or lemma_syn.endswith("sh") or lemma_syn.endswith("ch") \
            or lemma_syn.endswith("x") or lemma_syn.endswith("z"):
        final_syn = lemma_syn + "es"
    elif lemma_syn.endswith("y"):
        y_index = lemma_syn.rfind("y")  # find the index of y at the end of the word
        if lemma_syn[y_index - 1] in consonant:  # the letter before y is a consonant
            lemma_syn = lemma_syn[:y_index]
            final_syn = lemma_syn + "ies"
        else:   # the letter before y is a vowel
            final_syn = lemma_syn + "s"
    else:  # no particular rule
        final_syn = lemma_syn + "s"
    return final_syn


def token_is_past_participle(token):
    """
    Helper function that returns True if a token is past participle, False otherwise
    :param token: token that we want to know if it's past participle
    :return: bool
    """
    if token.tag_ == "VBN":
        return True
    return False


def action_on_past_participle(syn: str):
    """
   Helper function that transforms a word in his past participle version using lemmatization
   :param syn: word that we want to put in past participle form
   :return:
    """
    # process word
    processed_syn = nlp(syn)
    # lemmatize
    for p_syn in processed_syn:
        lemma_syn = p_syn.lemma_
    # put in past participle form according to english language rules
    if lemma_syn.endswith("e"):
        final_syn = lemma_syn + "d"
    elif lemma_syn.endswith("y"):
        y_index = lemma_syn.rfind("y")
        lemma_syn = lemma_syn[:y_index]
        final_syn = lemma_syn + "ied"
    else:  # no particular rile
        final_syn = lemma_syn + "ed"
    return final_syn


def token_is_third_singular(token):
    """
    Helper function that returns True if a token is in third person singular form, False otherwise
    :param token: token that we want to know if it's in third person singular form
    :return: bool
    """
    if token.tag_ == "VBZ":
        return True
    return False


def action_on_third_singular(syn: str):
    """
    Helper function that transforms a word in his third person singular version using lemmatization
    :param syn: word that we want to put in third person singular form
    :return:
    """
    processed_syn = nlp(syn)
    for p_syn in processed_syn:
        lemma_syn = p_syn.lemma_
    if lemma_syn.endswith("s") or lemma_syn.endswith("ss") or lemma_syn.endswith("sh") or lemma_syn.endswith(
            "ch") or lemma_syn.endswith("x") or \
            lemma_syn.endswith("zz"):
        final_syn = lemma_syn + "es"
    elif lemma_syn.endswith("z"):
        final_syn = lemma_syn + "zes"
    elif lemma_syn.endswith("y"):
        y_index = syn.rfind("y")  # find the index of y at the end of the word
        if lemma_syn[y_index - 1] in consonant:
            # se finisce in y precededuta da consonante tolgo y e metto ies
            lemma_syn = lemma_syn[:y_index]
            final_syn = lemma_syn + "ies"
        else:  # vocale
            final_syn = lemma_syn + "s"
        # is has does goes and negatives ?
    else:
        # also if finisce in y preceduta da vocale
        final_syn = lemma_syn + "s"
    return final_syn


def from_synset_to_string(synset):
    """
    Helper function that put a synset in string format and return it
    :param synset: synset that we want to put in string format
    :return: string
    """
    synset_name = synset.name()
    index = synset_name.find(".")
    synset_name_final = synset_name[:index]
    return synset_name_final