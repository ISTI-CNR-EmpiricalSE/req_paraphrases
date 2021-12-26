"""
SPACY

free, open-source library for advanced Natural Language Processing (NLP) in Python.
If you’re working with a lot of text, you’ll eventually want to know more about it.
what’s it about? What do the words mean in context? Who is doing what to whom? What companies and products are mentioned?
Which texts are similar to each other?
production use
build applications that process and “understand” large volumes of text
build information extraction or natural language understanding systems, or to pre-process text for deep learning.
is not a platform or “an API”. not provide a software as a service. help you build NLP applications but not consumable service.
not an out-of-the-box chat bot engine (che è roba che simula chat con essere umano)
not research software. it’s designed to get things done. different design decisions than NLTK or CoreNLP, which were created as platforms for teaching and research.
integrated and opinionated.
spaCy tries to avoid asking the user to choose between multiple algorithms that deliver equivalent functionality. Keeping the menu small lets spaCy deliver generally better performance and developer experience.
not a company.
Our company publishing spaCy and other software is called Explosion.

"""

"""
FEATURES

Name	Description
Tokenization	Segmenting text into words, punctuations marks etc.
Part-of-speech (POS) Tagging	Assigning word types to tokens, like verb or noun.
Dependency Parsing	Assigning syntactic dependency labels, describing the relations between individual tokens, like subject or object.
Lemmatization	Assigning the base forms of words. For example, the lemma of “was” is “be”, and the lemma of “rats” is “rat”.
Sentence Boundary Detection (SBD)	Finding and segmenting individual sentences.
Named Entity Recognition (NER)	Labelling named “real-world” objects, like persons, companies or locations.
Entity Linking (EL)	Disambiguating textual entities to unique identifiers in a knowledge base.
Similarity	Comparing words, text spans and documents and how similar they are to each other.
Text Classification	Assigning categories or labels to a whole document, or parts of a document.
Rule-based Matching	Finding sequences of tokens based on their texts and linguistic annotations, similar to regular expressions.
Training	Updating and improving a statistical model’s predictions.
Serialization	Saving objects to files or byte strings.
"""

"""
# CHAPTER 1: Finding words, phrases, names and concepts

import spacy
# Import the English language class
from spacy.lang.en import English
# Create the nlp object
# contains the processing pipeline includes language - specific rules for tokenization etc.
# At the center of spaCy is the object containing the processing pipeline. We usually call this variable "nlp".
# You can use the nlp object like a function to analyze text.
# It contains all the different components in the pipeline.
# It also includes language-specific rules used for tokenizing the text into words and punctuation. spaCy supports a variety of languages that are available in spacy.lang.
# Pipeline processing refers to overlapping (sovrapporre) operations by moving data or instructions into a conceptual pipe with all stages of the pipe performing simultaneously. For example, while one instruction is being executed, the computer is decoding the next.
nlp = English()       IMPORT the English language class and CREATE the nlp object.
# Created by processing a string of text with the nlp object
# When you process a text with the nlp object, spaCy creates a Doc object – short for "document". The Doc lets you access information about the text in a structured way, and no information is lost.
# The Doc behaves like a normal Python sequence by the way and lets you iterate over its tokens, or get a token by its index. But more on that later!
doc = nlp("Hello world!")    PROCESS the text and INSTANTIATE a Doc object in the variable doc.
# stampa tutto
print(doc.text)
# Iterate over tokens in a Doc
for token in doc:
    print(token.text)
# solo primo
first_token = doc[0]
print(first_token.text)
# secondo e terzo token
slice = doc[2:4]
# When you call nlp on a string, spaCy first tokenizes the text and creates a document object. In this exercise,
# you’ll learn more about the Doc, as well as its views Token and Span.

# trova PERCENTUALI
if token.like_num
if next_token.text == "%"
next_token = doc[token.i + 1] !!!!!!!!!!!!    token attuale puoi fare token o in modo stupido doc[token.i]
token.i dà indice di token attuale

# STATISTICAL MODELS
Enable spaCy to predict linguistic attributes in context
    Part-of-speech tags
    Syntactic dependencies
    Named entities
Models are trained on large datasets of labeled example texts.
Can be updated with more examples to fine-tune predictions


import spacy

nlp = spacy.load("en_core_web_sm")


# Process a text
doc = nlp("She ate the pizza")

# Iterate over the tokens
for token in doc:
    # Print the text and the predicted part-of-speech tag
    print(token.text, token.pos_)
# con token.pos_ stampo la previsione su cosa è una parola (PART OF SPEECH)
# word types in context.
# we load the small English model and receive an nlp object.
# we're processing the text "She ate the pizza".
# For each token in the doc, we can print the text and the .pos_ attribute, the predicted part-of-speech tag.
# In spaCy, attributes that return strings usually end with an underscore –
# attributes without the underscore return an integer ID value.

Even though a Doc is processed – e.g. split into individual words and annotated – it still holds all information of the 
original text, like whitespace characters. You can always get the offset of a token into the original string, 
or reconstruct the original by joining the tokens and their trailing whitespace. This way, you’ll never lose 
any information when processing text with spaCy.
While punctuation rules are usually pretty general, tokenizer exceptions strongly depend on the specifics of the 
individual language. This is why each available language has its own subclass, like English or German, that loads in 
lists of hard-coded data and exception rules.


import spacy


nlp = spacy.load("en_core_web_sm")
doc = nlp("She ate the pizza")
# Iterate over the tokens
for token in doc:
    # Print the text and the predicted part-of-speech tag
    print(token.text, token.pos_, token.dep_, token.head.text)
    
OUTPUT: 
She PRON nsubj ate
ate VERB ROOT ate
the DET det pizza
pizza NOUN dobj ate

Label 	Description 	Example
nsubj 	nominal subject 	She
dobj 	direct object 	pizza
det 	determiner (article) 	the

ENTITIES

Named entities are "real world objects" that are assigned a name – for example, a person, an organization or a country.
The doc.ents property lets you access the named entities predicted by the model.
span : A slice from a Doc object.
It returns an iterator of Span objects, so we can print the entity text and the entity label using the .label_ attribute.
entiti ha text e label

# Process a text
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# Iterate over the predicted entities
for ent in doc.ents:
    # Print the entity text and its label
    print(ent.text, ent.label_)
    
A quick tip: To get DEFINITIONS for the most common tags and labels, you can use the spacy.explain helper function.

import spacy
spacy.explain("NNP") terminale

import spacy
print(spacy.explain("NNP")) file sh

import spacy

nlp = spacy.load("en_core_web_sm")

text = "Upcoming iPhone X release date leaked as Apple reveals pre-orders"

# Process the text
doc = nlp(text)

# Iterate over the entities
for ent in doc.ents:
    # Print the entity text and label
    print(ent.text, ent.label_)

# Get the span for "iPhone X"
iphone_x = doc[1:3]  non ha trovato entità per questo, ne creo una io, uno span, uno slice of doc

# Print the span text
print("Missing entity:", iphone_x.text)


MATCHER
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Match patterns are lists of dictionaries. (!= DA PHRASE MATCHER che prende doc) Each dictionary describes one token. 
The keys are the names of token attributes, mapped to their expected values.

In this example, we're looking for two tokens with the text "iPhone" and "X".

text è nome di token attribute è key, valore restituito è appunto il testo
lower è come text ma minuscolo
perciò quando vuio matchare qualcosa di preciso metti text o lower

{
oppure

    Match lexical attributes

[{"LOWER": "iphone"}, {"LOWER": "x"}]

    Match any token attributes

[{"LEMMA": "buy"}, {"POS": "NOUN"}]
We can also match on other token attributes. Here, we're looking for two tokens whose lowercase forms equal "iphone" and "x".

We can even write patterns using attributes predicted by the model. Here, we're matching a token with the lemma "buy", 
plus a noun. The lemma is the base form, so this pattern would match phrases like "buying milk" or "bought flowers"
}

To use a pattern, we first import the matcher from spacy.matcher.
We also load a model and create the nlp object.
The matcher is initialized with the shared vocabulary, nlp.vocab. You'll learn more about this later – for now, just remember to always pass it in.
The matcher.add method lets you add a pattern. The first argument is a unique ID to identify which pattern was matched. The second argument is an optional callback. We don't need one here, so we set it to None. The third argument is the pattern.
To match the pattern on a text, we can call the matcher on any doc.
This will return the matches.

import spacy

# Import the Matcher
from spacy.matcher import Matcher

# Load a model and create the nlp object
nlp = spacy.load("en_core_web_sm")

# Initialize the matcher with the shared vocab
matcher = Matcher(nlp.vocab)


# Add the pattern to the matcher
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
matcher.add("IPHONE_PATTERN", None, pattern)

# Process some text
doc = nlp("Upcoming iPhone X release date leaked")

# Call the matcher on the doc
matches = matcher(doc)
print(matches) se faccio così mi stampa tutti i matches
TRIPLA
un match è una tupla con 3 valori (tripla): id (hash value of the pattern name), inizio e fine (nel documento)
- match_id: hash value of the pattern name
- start: start index of matched span
- end: end index of matched span
sfrutto questi indici di inizio e fine per stampare uno span, uno slice di documento in cui è contenuto mio matches
When you call the matcher on a doc, it returns a list of tuples.
Each tuple consists of three values: the match ID, the start index and the end index of the matched span.
This means we can iterate over the matches and create a Span object (== A PHRASE MATCHER): a slice of the doc at the start and end index.

# Iterate over the matches
for match_id, start, end in matches:
    # Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)


pattern = [
    {"IS_DIGIT": True},
    {"LOWER": "fifa"},
    {"LOWER": "world"},
    {"LOWER": "cup"},
    {"IS_PUNCT": True}
]

doc = nlp("2018 FIFA World Cup: France won!")
output: 2018 FIFA World Cup:
Here's an example of a more complex pattern using lexical attributes.
We're looking for five tokens:
A token consisting of only digits.
Three case-insensitive tokens for "fifa", "world" and "cup".
And a token that consists of punctuation.
The pattern matches the tokens "2018 FIFA World Cup:".

pattern = [
    {"LEMMA": "love", "POS": "VERB"},
    {"POS": "NOUN"}
]
In this example, we're looking for two tokens:
A verb with the lemma "love", followed by a noun.
This pattern will match "loved dogs" and "love cats".
doc = nlp("I loved dogs but now I love cats more.")
output:
loved dogs
love cats

pattern = [
    {"LEMMA": "buy"},
    {"POS": "DET", "OP": "?"},  # optional: match 0 or 1 times
    {"POS": "NOUN"}
]
Operators and quantifiers let you define how often a token should be matched. They can be added using the "OP" key.

Here, the "?" operator makes the determiner token optional, so it will match a token with the lemma "buy", an optional article and a noun.
# optional: match 0 or 1 times
doc = nlp("I bought a smartphone. Now I'm buying apps.")
output:
bought a smartphone
buying apps
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
{"OP": "!"} 	Negation: match 0 times
{"OP": "?"} 	Optional: match 0 or 1 times
{"OP": "+"} 	Match 1 or more times
{"OP": "*"} 	Match 0 or more times

i vari valori che una chiave può assumere
guida
available token attribute nella guida spacy
Linguistic Annotations
Part-of-speech tags and dependencies
quelle nella prima riga sono chiavi keys
TEXT       LEMMA	    POS	    TAG	    DEP	        SHAPE	    ALPHA	    STOP       IS_TITLE (Title case means that the first letter of each word is capitalized, except for certain small words, such as articles and short prepositions.)  
Apple	    apple	    PROPN	NNP	    nsubj	    Xxxxx	    True	    False       True
is	        be	        AUX	    VBZ	    aux	        xx	        True	    True        Falseexplain
looking	    look	    VERB	VBG	    ROOT	    xxxx	    True	    False
at	        at	        ADP	    IN	    prep	    xx	        True	    True
buying	    buy	        VERB	VBG	    pcomp	    xxxx	    True	    False
U.K.	    u.k.	    PROPN	NNP	    compound	X.X.	    False	    False
startup	    startup	    NOUN	NN	    dobj	    xxxx	    True	    False
for	        for	        ADP	    IN	    prep	    xxx	        True	    True
$	        $	        SYM	    $	    quantmod	$	        False	    False
1	        1	        NUM	    CD	    compound	d	        False	    False
billion	    billion	    NUM	    CD	    pobj	    xxxx	    True	    False
"""

"""
# CHAPTER 2: Large-scale data analysis

spaCy stores all shared data in a vocabulary, the Vocab.
Vocab: dizionario che raggruppa stores data shared across multiple documents

This includes words, but also the labels schemes for tags and entities.

To save memory, all strings are encoded to hash IDs. If a word occurs more than once, 
we don't need to save it every time.
Strings are only stored once in the StringStore via nlp.vocab.strings

Instead, spaCy uses a hash function to generate an ID and stores the string only once in the string store. 
The string store is available as nlp.vocab.strings.
It's a lookup table that works in both directions. You can look up a string and get its hash, and look up a hash to get 
its string value. Internally, spaCy only communicates in hash IDs.

Hash IDs can't be reversed, though. If a word is not in the vocabulary, there's no way to get its string. 
That's why we always need to pass around, provide the shared vocab.

import spacy

from spacy.lang.en import English

nlp = English()

# genera valore hash
nlp.vocab.strings.add("coffee")
!!!! se facevo doc = nlp(string) non c'era bisogno di fare la add, pfacendo doc = nlp() aggiunge parole al vocabolario

#che ottengo così
coffee_hash = nlp.vocab.strings["coffee"]
print(coffee_hash)

# stringa la ottengo così
coffee_string = nlp.vocab.strings[coffee_hash]
print(coffee_string)

# Raises an error if we haven't seen the string before
string = nlp.vocab.strings[3197928453018144401]
print(string)

# The doc also exposes the vocab and strings
doc = nlp("I love coffee")
print("hash value:", doc.vocab.strings["coffee"])

to get the hash for a string, we can look it up in nlp.vocab.strings.
To get the string representation of a hash, we can look up the hash.
A Doc object also exposes its vocab and strings.


import spacy

from spacy.lang.en import English

nlp = English()

# genera valore hash
nlp.vocab.strings.add("coffee")

#che ottengo così
coffee_hash = nlp.vocab.strings["coffee"]

# stringa la ottengo così
coffee_string = nlp.vocab.strings[coffee_hash]

# Raises an error if we haven't seen the string before
string = nlp.vocab.strings[3197928453018144401]

# The doc also exposes the vocab and strings !!!!!!!!!!!!
doc = nlp("I love coffee")
print("hash value:", doc.vocab.strings["coffee"])
print("string value:", doc.vocab.strings[coffee_hash])
print("string value:", doc.vocab.strings[doc.vocab.strings["coffee"]]) # ultimi due stampano la stessa cosa

LEXEMES are context-independent entries in the vocabulary.
A Lexeme object is an entry in the vocabulary
You can get a lexeme by looking up a string or a hash ID in the vocab.  (non in strings!!!!!!!)
Lexemes expose attributes, just like tokens.
They hold context-independent information about a word, like the text, the hash (lexeme.orth) or whether the word consists of alphabetic characters.  (booleano lexeme.is_alpha!!!)
Lexemes don't have part-of-speech tags, dependencies or entity labels. Those depend on the context. !!!


import spacy
from spacy.lang.en import English
nlp = English()

doc = nlp("I love coffee")
lexeme = nlp.vocab["coffee"]

# Print the lexical attributes
print(lexeme.text, lexeme.orth, lexeme.is_alpha)

Here's an example.

The Doc contains words in context – in this case, the tokens "I", "love" and "coffee" 
with their part-of-speech tags and dependencies.

Each token refers to a lexeme, entrata in vocavolario, posso ottenere hash, which knows the word's hash ID. 
To get the string representation of the word, spaCy looks up the hash in the string store. spacy opera con hash,
guarda hash e ottiene stringa

doc fornisce tokens -> lexeme fornisce hash -> da hash ottengo sting representaiton of the word
link immagine : https://course.spacy.io/vocab_stringstore.png
 
from spacy.lang.en import English
from spacy.lang.de import German

# Create an English and German nlp object
nlp = English()
nlp_de = German()


# Get the ID for the string 'Bowie' !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
bowie_id = nlp.vocab.strings["Bowie"]   # questo va bene, non c'è bisogno di fare doc = nlp o add per avere hash, ma per aggiungere parola a vocabolario sì
print(bowie_id)

# Look up the ID for "Bowie" in the vocab
print(nlp_de.vocab.strings[bowie_id])   # problema di questo è che sto usando un hash per cercare una parola che non c'è
The string "Bowie" isn’t in the German vocab, so the hash can’t be resolved in the string store

# così ok
from spacy.lang.en import English
from spacy.lang.de import German

# Create an English and German nlp object
nlp = English()
nlp_de = German()

# Get the ID for the string 'Bowie'
bowie_id = nlp.vocab.strings["Bowie"]
print(bowie_id)
doc = nlp("Bowie")
# Look up the ID for "Bowie" in the vocab
print(doc.vocab.strings[bowie_id])

# UNA PAROLA C'È SSE L'HO AGGIUNTA A VOCABOLARIO (anche nel caso di nome non proprio), e poi devo cercarla nello STESSO vocabolario
# HASH POSSO AVERLO ANCHE SENZA AVERLO AGGIUNTO

Now that you know all about the vocabulary and string store, we can take a look at the most important data structure: 
the Doc, and its views Token and Span.
The Doc is one of the central data structures in spaCy. It's created AUTOMATICALLY (esempi prima) when you process a text with the nlp object. 
But you can also instantiate the class MANUALLY.
After creating the nlp object, we can import the Doc class from spacy.tokens.
Here we're creating a doc from three words. 
The spaces are a list of boolean values indicating whether the word is followed by a space. Every token includes that information – even the last one!
The Doc class takes three arguments: the shared vocab, the words and the spaces.


# Create an nlp object
from spacy.lang.en import English
nlp = English()

# Import the Doc class
from spacy.tokens import Doc

# The words and spaces to create the doc from
words = ["Hello", "world", "!"]
spaces = [True, False, False]

# Create a doc manually
doc = Doc(nlp.vocab, words=words, spaces=spaces)

A Span is a slice of a doc consisting of one or more tokens. The Span takes at least three arguments: 
the doc it refers to, and the start and end index of the span. Remember that the end index is exclusive!

To create a Span manually, we can also import the class from spacy.tokens. We can then instantiate it with the doc and the span's start and end index, and an optional label argument.
iphone_x = doc[1:3] esempio di span non manuale

The doc.ents are writable, so we can add entities manually by overwriting it with a list of spans.

NON HAI BISOGNO DI IMPORTARE SPACY ????

from spacy.lang.en import English
nlp = English()
# Import the Doc and Span classes
from spacy.tokens import Doc, Span

# The words and spaces to create the doc from
words = ["Hello", "world", "!"]
spaces = [True, False, False]

# Create a doc manually
doc = Doc(nlp.vocab, words=words, spaces=spaces)

# Create a span manually
span = Span(doc, 0, 2)

# Create a span with a label
span_with_label = Span(doc, 0, 2, label="GREETING")
print(span)  # Hello world
print(span_with_label)  # Hello world
print(span_with_label.label_)   # GREETING
print(span_with_label.label)     # numero
print(span_with_label.text)     # Hello world

una ent è anche uno span, non necessariamente uno span è anche una ent

# Add span to the doc.ents   come fa sapcy dietro le scene
doc.ents = [span_with_label]
# Named entities are "real world objects" that are assigned a name – for example, a person, an organization or a country.
hanno un testo e un label

A few tips and tricks before we get started:
The Doc and Span are very powerful and optimized for performance. They give you access to all references and relationships of the words and sentences.
If your application needs to output strings, make sure to convert the doc as LATE as possible. If you do it too early, you'll lose all relationships between the tokens.
To keep things consistent, try to use built-in token attributes wherever possible. For example, token.i for the token index.
Also, don't forget to always pass in the shared vocab!

span = Span(doc, 2, 4, label="PERSON")
se non assegni label a span poi non puoi creare entità, anzi puoi ma poi fa roba strana (separa parole?) 
e attenta a indici

Always convert the results to strings as late as possible, and try to use NATIVE token attributes to keep things consistent.
USA TOKEN.POS_ E TOKEN.TEXT
NON FARE QUESTO       NOOOOOOOOOOOOOOOOOOOOOO
token_texts = [token.text for token in doc]
pos_tags = [token.pos_ for token in doc]
qui stai convertendo results a stringa troppo presto, lose all relationships between the tokens.

WORD VECTORS AND SEMANTIC SIMILARITY
spaCy can compare two objects and predict SIMILARITY, spaCy can compare two objects and predict how similar they are – for example, documents, spans or single tokens.
Doc.similarity(), Span.similarity() and Token.similarity(), The Doc, Token and Span objects have a .similarity method that takes another object and returns a floating point number between 0 and 1, indicating how similar they are.
take another object and return a similarity score (0 to 1)
Important: NEEDS a model that has WORD VECTORS included, for example:   , One thing that's very important: In order to use similarity, you need a larger spaCy model that has word vectors included.
en_core_web_md (medium model) word vectors are included
en_core_web_lg (large model) word vectors are included
NOT en_core_web_sm (small model) word vectors are not included
For example, the medium or large English model – but not the small one. So if you want to use vectors, always go with a model that ends in "MD" or "LG". You can find more details on this in the models documentation.

Here's an example. Let's say we want to find out whether two documents are similar.
First, we load the medium English model, "en_core_web_md".
We can then create two doc objects and use the first doc's similarity method to compare it to the second.
Here, a fairly high similarity score of 0.86 is predicted for "I like fast food" and "I like pizza".
The same works for tokens.
According to the word vectors, the tokens "pizza" and "pasta" are kind of similar, and receive a score of 0.7.

import spacy
# Load a larger model with vectors
nlp = spacy.load("en_core_web_md")

# Compare two documents
doc1 = nlp("I like fast food")
doc2 = nlp("I like pizza")
print(doc1.similarity(doc2))

# Compare two tokens
doc = nlp("I like pizza and pasta")
token1 = doc[2]
token2 = doc[4]
print(token1.similarity(token2))

You can also use the similarity methods to compare DIFFERENT TYPES of objects.
For example, a document and a token.
Here, the similarity score is pretty low and the two objects are considered fairly dissimilar.
Here's another example comparing a span – "pizza and pasta" – to a document about McDonalds.
The score returned here is 0.61, so it's determined to be kind of similar.

import spacy
# Load a larger model with vectors
nlp = spacy.load("en_core_web_md")

# Compare a document with a token
doc = nlp("I like pizza")
token = nlp("soap")[0]

print(doc.similarity(token))

# Compare a span with a document
span = nlp("I like pizza and pasta")[2:5]
doc = nlp("McDonalds sells burgers")

print(span.similarity(doc))

HOW does spaCy predict similarity? under the hood
Similarity is determined using WORD VECTORS: multi-dimensional representations of meanings of words, 
generated using Word2Vec (and lots of text), Word2Vec is an algorithm that's often used to train word vectors from raw text.
Vectors can be added to spaCy's statistical models.
By default, the similarity returned by spaCy is the COSINE SIMILARITY between two vectors – but this can be adjusted if necessary.
Cosine similarity measures the similarity between two vectors of an inner product space. 
It is measured by the cosine of the angle between two vectors and determines whether two vectors are pointing 
in roughly the same direction. It is often used to measure document similarity in text analysis.
Calcoli coseno tra due vettori
Il valore di similitudine così definito è compreso tra -1 e +1, dove -1 indica una corrispondenza esatta ma opposta e +1 indica due vettori uguali. 
Vectors for objects consisting of several tokens, like the Doc and Span, default to the average of their token vectors.
That's also why you usually get more value out of shorter phrases with fewer irrelevant words.

To give you an idea of what those vectors look like, here's an example.
First, we load the medium model again, which ships with word vectors.
Next, we can process a text and look up a token's vector using the .vector ATTRIBUTE.
The result is a 300-dimensional vector of the word "banana".

import spacy
# Load a larger model with vectors
nlp = spacy.load("en_core_web_md")

doc = nlp("I have a banana")
# Access the vector via the token.vector attribute
print(doc[3].vector)

Predicting similarity can be useful for many types of applications. For example, to recommend a user similar texts based on the ones they have read. It can also be helpful to flag duplicate content, like posts on an online platform.

However, it's important to keep in mind that there's no objective definition of what's similar and what isn't. 
It always depends on the CONTEXT and what your application needs to do.

Here's an example: spaCy's default word vectors assign a very high similarity score to "I like cats" and "I hate cats". 
This makes sense, because both texts express sentiment about cats. But in a different application context, 
you might want to consider the phrases as very dissimilar, because they talk about opposite sentiments.

doc1 = nlp("I like cats")
doc2 = nlp("I hate cats")

print(doc1.similarity(doc2))


COMBINING statistical MODELS with RULE-BASED SYSTEMS
practicing combining predictions with rule-based information extraction !!!
STATISTICAL MODELS are useful if your application needs to be able to GENERALIZE based on a few examples.
For instance, detecting product or person names usually benefits from a statistical model. 
Instead of providing a list of all person names ever, your application will be able to predict whether a span of tokens 
is a person name. Similarly, you can predict dependency labels to find subject/object relationships.
To do this, you would use spaCy's entity recognizer, dependency parser or part-of-speech tagger.
RULE-BASED APPROACHES on the other hand come in handy if there's a more or less FINITE number of instances you want to find. 
For example, all countries or cities of the world, drug names or even dog breeds.
 	                            Statistical models 	                                                          Rule-based systems
Use cases 	                application needs to generalize based on examples 	                            dictionary with finite number of examples
Real-world examples 	    product names, person names, subject/object relationships 	        countries of the world, cities, drug names, dog breeds
spaCy features    !!!      	entity recognizer, dependency parser, part-of-speech tagger 	            tokenizer, Matcher, PhraseMatcher


In the last chapter, you learned how to use spaCy's rule-based matcher to find complex patterns in your texts. Here's a quick recap.
The matcher is initialized with the shared vocabulary – usually nlp.vocab.
Patterns are lists of dictionaries, and each dictionary describes one token and its attributes. Patterns can be added to the matcher using the matcher.add method.
Operators let you specify how often to match a token. For example, "+" will match one or more times.
Calling the matcher on a doc object will return a list of the matches. Each match is a tuple consisting of an ID, and the start and end token index in the document.
# Initialize with the shared vocab
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)

# Patterns are lists of dictionaries describing the tokens
pattern = [{"LEMMA": "love", "POS": "VERB"}, {"LOWER": "cats"}]
matcher.add("LOVE_CATS", None, pattern)

# Operators can specify how often a token should be matched
pattern = [{"TEXT": "very", "OP": "+"}, {"TEXT": "happy"}]
matcher.add("VERY_HAPPY", None, pattern)

# Calling matcher on doc returns list of (match_id, start, end) tuples
doc = nlp("I love cats and I'm very very happy")
matches = matcher(doc)

{} quello tra parentesi quadre è UN SOLO token
[{}, {}] significa che i due token stanno accanto
!!!!!!!!!!!! The tokenizer doesn’t create tokens for single spaces, so there’s no token with the value " " in between. per matchare due token tra cui c'è uno spazio non serve indicare nel pattern di matchare il token spazio, anzi se lo metti da errore, non trova questo token
[] quello tra parentesi quadre è il pattern a cui posso dare un nome a aggiungerlo al matcher con add
i tanti token di un pattern individuano uno span, faccio match con vari span
matcher(doc) restituiscono questi span tramite tripla id inizio fine   for match_id, start, end in matcher(doc):
grazie a span accedo a attributi e features

Here's an example of a matcher rule for "golden retriever".

If we iterate over the matches returned by the matcher, 
we can get the match ID and the start and end index of the matched span. 
We can then find out more about it. 
Span objects give us access to the original document and all other token attributes and linguistic features predicted by the model.

For example, we can get the span's ROOT token. If the span consists of more than one token, 
this will be the token that decides the CATEGORY of the phrase. For example, the root of "Golden Retriever" is "Retriever". 
We can also find the HEAD token of the root. This is the syntactic "parent" that GOVERNS the phrase – in this case, the verb "have".

Finally, we can look at the PREVIOUS token and its attributes. In this case, it's a determiner, the article "a".
import spacy
# Import the Matcher
from spacy.matcher import Matcher
# Load a model and create the nlp object
nlp = spacy.load("en_core_web_sm")
# Initialize the matcher with the shared vocab
matcher = Matcher(nlp.vocab)
matcher.add("DOG", None, [{"LOWER": "golden"}, {"LOWER": "retriever"}])
doc = nlp("I have a Golden Retriever")
for match_id, start, end in matcher(doc):
    span = doc[start:end]
    print("Matched span:", span.text)
    # Get the span's root token and root head token
    print("Root token:", span.root.text)
    print("Root head token:", span.root.head.text)
    # Get the previous token and its POS tag
    print("Previous token:", doc[start - 1].text, doc[start - 1].pos_)
    
The PHRASE MATCHER is another helpful tool to find sequences of words in your data.

It performs a keyword search on the document, but instead of only finding strings, it gives you DIRECT ACCESS to the TOKENS in context. PhraseMatcher like regular expressions or keyword search – but with access to the tokens!
It takes DOC objects as patterns. Takes Doc object as patterns
It's also really FAST.  More efficient and faster than the Matcher
This makes it very useful for matching large dictionaries and word lists on LARGE volumes of text.  Great for matching large word lists

Here's an example.

The phrase matcher can be imported from spacy.matcher and follows the same API as the regular matcher.
INSTEAD OF A LIST OF DICTIONARIES, WE PASS IN A DOC OBJECT AS THE PATTERN. (!= DA MATCHER)
We can then iterate over the matches in the text, which gives us the match ID, and the start and end of the match. This lets us create a Span object (== A MATCHER) for the matched tokens "Golden Retriever" to analyze it in context.

import spacy
from spacy.matcher import PhraseMatcher
nlp = spacy.load("en_core_web_sm")
matcher = PhraseMatcher(nlp.vocab)

pattern = nlp("Golden Retriever")    PATTERN NON È STRINGA, MA È DOC OBJ, OSSIA STRINGA PROCESSATA, QUINDI QUANDO DEVI PASSARE TANTE STRINGHE CHE STANNO IN LISTA DEVI PROCESSARLE TUTTE, CI SONO VARI MODI
matcher.add("DOG", None, pattern)
doc = nlp("I have a Golden Retriever")

# Iterate over the matches
for match_id, start, end in matcher(doc):
    # Get the matched span
    span = doc[start:end]
    print("Matched span:", span.text)

se fai una ricerca su più pattern ha senso nel for stamapre anche il pattern ID
for match_id, start, end in matcher(doc):
    # Print pattern string name and text of matched span
    print(doc.vocab.strings[match_id], doc[start:end].text)

quando mi dice case insensitive usa LOWER, se invece vuoi esattamente certe lettere maiuscole e certe minuscole usa text
IS_TITLE significa che prima lettera è maiuscola resto minuscolo
PUNTEGGIATURA È UN TOKEN, SPAZI NO
pattern1 = [{"LOWER": "amazon"}, {"IS_TITLE": True, "POS": "PROPN"}]
pattern2 = [{"LOWER": "ad"}, {"TEXT": "-"}, {"LOWER": "free"}, {"POS": "NOUN"}]
!!!!!!!!!!!!!!!!!
per capire come devi spezzare frase in token (in modo da indicare nel pattern token corretti) : 
for token in nlp("frase"):
    print(token.text)
Try processing the strings that should be matched with the nlp object

Sometimes it’s more efficient to match exact strings instead of writing patterns describing the individual tokens.
This is especially true for finite categories of things – like all countries of the world.
We already have a list of countries, so let’s use this as the basis of our information extraction script. 
A list of string names is available as the variable COUNTRIES.

patterns = list(nlp.pipe(COUNTRIES))
patterns = nlp(country) for country in COUNTRIES
for country in COUNTRIES:
    add nlp(country) a patterns



# import json
from spacy.lang.en import English

# with open("countries.json", encoding="utf8") as f:
#    COUNTRIES = json.loads(f.read())

COUNTRIES = []
with open("countries.txt", "r") as fd:
    for line in fd:
        line = line.strip("\n")    #strip toglie caratteri al lato, toglie spazi, puoi anche specificare quali carattere togliere
        COUNTRIES.append(line)

nlp = English()
doc = nlp("Czech Republic may help Slovakia protect its airspace")

# Import the PhraseMatcher and initialize it
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)

# Create pattern Doc objects...
# This is the faster version of: [nlp(country) for country in COUNTRIES]
# patterns = list(nlp.pipe(COUNTRIES))  ???? funziona

# patterns = []  ?????? non funziona
# patterns.append([nlp(country) for country in COUNTRIES])

# list comprension
# patterns = [country for country in nlp.pipe(COUNTRIES)]   più efficente perché processa testo tutto assieme, internamente
# patterns = [nlp(country) for country in COUNTRIES]    meno efficiente perché processa parola una per una

patterns = []
for country in COUNTRIES:
    patterns.append(nlp(country))
    
patterns = []      questo è più efficiente, usa pipe, spaCy’s nlp.pipe method takes an iterable of texts and yields processed Doc objects. The batching is done internally. Process the texts as a stream using nlp.pipe and buffer them in batches, instead of one-by-one. This is usually much more efficient.
for country in nlp.pipe(COUNTRIES):
    patterns.append(country)


# ...and add them to the matcher     SE PATTERNS SONO TANTI METTI ASTERISCO
matcher.add("COUNTRY", None, *patterns)
# primo argomento è id (nel caso io cerchi più pattern nel for stampo anche quello per capire quale ho trovato)
# secondo argomento è optional callback che non vediamo
# terzo è pattern

# Call the matcher on the test document and print the result
matches = matcher(doc)
print([doc[start:end] for match_id, start, end in matches])

with open("exercises/en/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())    COUNTRIES è lista
with open("exercises/en/country_text.txt", encoding="utf8") as f:
    TEXT = f.read()    TEXT è stringa
    
  # Create a doc and reset existing entities
  doc = nlp(TEXT)
  doc.ents = []
   # Overwrite the doc.ents and add the span
    doc.ents = list(doc.ents) + [span]
    
    esempio COMPLETO :

import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
import json

with open("exercises/en/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())
with open("exercises/en/country_text.txt", encoding="utf8") as f:
    TEXT = f.read()

nlp = spacy.load("en_core_web_sm")
matcher = PhraseMatcher(nlp.vocab)
patterns = list(nlp.pipe(COUNTRIES))
# list comprension
# patterns = [country for country in nlp.pipe(COUNTRIES)] + efficiente perché Process the texts as a stream using nlp.pipe and buffer them in batches, instead of one-by-one. This is usually much more efficient. 
# When processing large volumes of text, the statistical models are usually more efficient if you let them work on batches of texts. spaCy’s nlp.pipe method takes an iterable of texts and yields processed Doc objects. The batching is done internally.
# patterns = [nlp(country) for country in COUNTRIES] - efficiente 
matcher.add("COUNTRY", None, *patterns)

# Create a doc and reset existing entities
doc = nlp(TEXT)
doc.ents = []

# Iterate over the matches
for match_id, start, end in matcher(doc):
    # Create a Span with the label for "GPE"
    span = Span(doc, start, end, label="GPE")

    # Overwrite the doc.ents and add the span
    doc.ents = list(doc.ents) + [span]

    # Get the span's root head token
    span_root_head = span.root.head
    # Print the text of the span root's head token and the span text
    print(span_root_head.text, "-->", span.text)

# Print the entities in the document
print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "GPE"])

you've practiced combining predictions with
rule-based information extraction !!!
"""

"""
# CHAPTER 3: Processing Pipelines

This chapter will show you everything you need to know about spaCy's processing pipeline. You'll learn what 
goes on under the hood when you process a text, how to write your own components and add them to the pipeline, 
and how to use custom attributes to add your own metadata to the documents, spans and tokens.

PROCESSING PIPELINES: a series of functions applied to a doc to add attributes like part-of-speech tags, dependency labels or named entities.
you'll learn about the pipeline components provided by spaCy, and what happens behind the scenes when you call nlp on a string of text.
What happens when you call nlp?
Tokenize the text and apply each pipeline component in order. componenti della pipeline possono variare da modello a modello
Whenever you're unsure about the current pipeline, you can inspect it by printing nlp.pipe_names or nlp.pipeline.
componenti indicati sotto sono quelli base, di modello en_core_web_sm
immagine https://course.spacy.io/pipeline.png
doc = nlp("This is a sentence.")
First, the tokenizer is applied to turn the string of text into a Doc object. Next, a series of pipeline components is applied to the doc in order. In this case, the tagger, then the parser, then the entity recognizer. Finally, the processed doc is returned, so you can work with it.
1 text -> TOKENIZER -> Doc obj
2 TAGGER
3 PARSER
4 NER ( named entity recognizer)
2,3,4 sono pipeline components applicati in ordine, alla fine restituiscono Doc su cui possiamo lavorare
posso lavorare nel senso posso accedere a attributi tipo token.pos, doc.ents... 
ATTRIBUTI VENGONO CREATI DA QUESTE COMPONENTI
custom components servono a adding custom values to documents, tokens and spans, and customizing the doc.ents.

guida2
Built-in pipeline components

Name 	        Description 	                Creates
tagger 	        Part-of-speech tagger 	        Token.tag, Token.pos
parser 	        Dependency parser 	            Token.dep, Token.head, Doc.sents, Doc.noun_chunks
ner 	        Named entity recognizer 	    Doc.ents, Token.ent_iob, Token.ent_type
textcat 	    Text classifier 	            Doc.cats

The part-of-speech tagger sets the token.tag and token.pos attributes.
The dependency parser adds the token.dep and token.head attributes and is also responsible for detecting sentences and base noun phrases, also known as noun chunks.
The named entity recognizer adds the detected entities to the doc.ents property. It also sets entity type attributes on the tokens that indicate if a token is part of an entity or not.
Finally, the text classifier sets category labels that apply to the whole text, and adds them to the doc.cats property.
Because text categories are always very specific, the text classifier is not included in any of the pre-trained models by default. But you can use it to train your own system.

under the hood
immagine https://course.spacy.io/package_meta.png
All models you can load into spaCy include several files and a META.JSON.
The meta defines things like the language and pipeline. This tells spaCy which components to instantiate.
The built-in components that make predictions also need BINARY DATA. 
The data is included in the model package and loaded into the component when you load the model.

To see the names of the pipeline components present in the current nlp object, you can use the nlp.pipe_names attribute.
list of pipeline component names
import spacy
nlp = spacy.load("en_core_web_sm")
print(nlp.pipe_names)

For a list of component name and component function tuples, you can use the nlp.pipeline attribute.
list of (name, component) tuples
import spacy
nlp = spacy.load("en_core_web_sm")
print(nlp.pipeline)
The component functions are the functions applied to the doc to process it and set attributes – for example, part-of-speech tags or named entities.

CUSTOM PIPELINE COMPONENTS: 
Custom pipeline components let you add YOUR OWN FUNCTIONS to the spaCy PIPELINE that is executed when you call 
the nlp object on a text – for example, to modify the doc and add more data to it. also update built-in attributes
Why custom components?
- After the text is tokenized and a Doc object has been created, pipeline components are applied in order. spaCy supports a range of built-in components, but also lets you define your own.
- Custom components are executed automatically when you call the nlp object on a text. Make a function execute automatically when you call nlp
- They're especially useful for adding your own custom metadata to documents and tokens. Add your own metadata to documents and tokens
- You can also use them to update built-in attributes, like the named entity spans. Updating built-in attributes like doc.ents

Anatomy of a component 
- function or callable that takes a doc, modifies it and returns it, so it can be processed by the next component in the pipeline.
- Components can be added to the pipeline using the nlp.add_pipe method. The method takes at least one argument: the component function.

def custom_component(doc):
    # Do something to the doc here
    return doc
    
nlp.add_pipe(custom_component)

To specify WHERE to add the component in the pipeline, you can use the following keyword ARGUMENTS:
- Setting last to True will add the component last in the pipeline. This is the DEFAULT behavior.
- Setting first to True will add the component first in the pipeline, right after the tokenizer.
- The before and after arguments let you define the name of an existing component to add the new component before or after. For example, before="ner" will add it before the named entity recognizer.
  The other component to add the new component before or after needs to exist, though – otherwise, spaCy will raise an error.
  
Argument 	        Description 	            Example
last 	            If True, add last 	        nlp.add_pipe(component, last=True)
first 	            If True, add first 	        nlp.add_pipe(component, first=True)
before 	            Add before component 	    nlp.add_pipe(component, before="ner")
after 	            Add after component 	    nlp.add_pipe(component, after="tagger")

example
We start off with the small English model.
We then define the component – a function that takes a Doc object and returns it.
Let's do something simple and print the length of the doc that passes through the pipeline.
Don't forget to return the doc so it can be processed by the next component in the pipeline! The doc created by the tokenizer is passed through all components, so it's important that they all return the modified doc.
We can now add the component to the pipeline. Let's add it to the very beginning right after the tokenizer by setting first=True.
When we print the pipeline component names, the custom component now shows up at the start. This means it will be applied first when we process a doc.

import spacy
# Create the nlp object
nlp = spacy.load("en_core_web_sm")

# Define a custom component
def custom_component(doc):
    # Print the doc's length
    print("Doc length:", len(doc))
    # Return the doc object
    return doc

# Add the component first in the pipeline
nlp.add_pipe(custom_component, first=True)

# Print the pipeline component names
print("Pipeline:", nlp.pipe_names)

Now when we process a text using the nlp object, the custom component will be applied to the doc and the length of the document will be printed.
# Process a text
aggiungo a quello di prima
doc = nlp("Hello world!")
output: doc lentgh: 3

paCy’s nlp.pipe method takes an iterable of texts and yields processed Doc objects
Process the texts as a stream using nlp.pipe and buffer them in batches, instead of one-by-one. This is usually much more efficient.


import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")
animals = ["Golden Retriever", "cat", "turtle", "Rattus norvegicus"]
print("animals:", animals)

# quello che aggiungi a pattern deve essere processato. hai tre modi, terzo è meno efficiente
# Process the texts as a stream using nlp.pipe and buffer them in batches, instead of one-by-one. This is usually much more efficient.

# animal_patterns = list(nlp.pipe(animals))

# animal_patterns = []
# for animal in nlp.pipe(animals):
    # animal_patterns.append(animal)

# animal_patterns = []
# for animal in animals:
    # animal_patterns.append(nlp(animal))

# animal_patterns = []
# [animal_patterns.append(animal) for animal in nlp.pipe(animals)]

# 1 animal_patterns = [animal for animal in nlp.pipe(animals)]    
# 2 animal_patterns = [nlp(animal) for animal in animals]  
# 1 è più efficiente perché processa il testo con metodo nlp lavorando a lotti, blocchi, batches, invece che stringa per stringa come fa il 2
# When processing large volumes of text, the statistical models are usually more efficient if you let them work on batches of texts. 
# spaCy’s nlp.pipe method takes an iterable of texts and yields processed Doc objects. The batching is done internally.
# Process the texts as a stream using nlp.pipe and buffer them in batches, instead of one-by-one. 
# This is usually much more efficient.

print("animal_patterns:", animal_patterns)
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ANIMAL", None, *animal_patterns)

# Define the custom component
def animal_component(doc):
    # Apply the matcher to the doc
    matches = matcher(doc)
    # Create a Span for each match and assign the label "ANIMAL"
    spans = [Span(doc, start, end, label="ANIMAL") for match_id, start, end in matches]
    # Overwrite the doc.ents with the matched spans
    doc.ents = spans
    return doc


# Add the component to the pipeline after the "ner" component
nlp.add_pipe(animal_component, after="ner")
print(nlp.pipe_names)

# Process the text and print the text and label for the doc.ents
doc = nlp("I have a cat and a Golden Retriever")
# [print(ent.text, ent.label) for ent in doc.ents] uguale a riga sotto
print([(ent.text, ent.label) for ent in doc.ents])

# for ent in doc.ents:
   # print(ent.text, ent.label)
   
   
EXTENSION ATTRIBUTES
how to add custom attributes to the Doc, Token and Span objects to store custom data.
- Custom attributes let you add any metadata to docs, tokens and spans. Add custom metadata to documents, tokens and spans
The data can be added once, or it can be computed dynamically.
- Custom attributes are available via the ._ (dot underscore) property. Accessible via the ._ property. 
This makes it clear that they were added by the user, and not built into spaCy, like token.text.
doc._.title = "My document"
token._.is_color = True
span._.has_color = False
- Attributes need to be registered on the global Doc, Token and Span classes you can import from spacy.tokens. 
Registered on the global Doc, Token or Span using the set_extension method. To register a custom attribute on the Doc, 
Token and Span, you can use the set_extension method.
# Import global classes
from spacy.tokens import Doc, Token, Span
You've already worked with those in the previous chapters. 
# Set extensions on the Doc, Token and Span
Doc.set_extension("title", default=None)
Token.set_extension("is_color", default=False)
Span.set_extension("has_color", default=False)
The first argument is the attribute name. Keyword arguments let you define how the value should be computed. 
In this case, it has a default value and can be overwritten.

Extension attribute types
There are three types of extensions
- Attribute extensions
- Property extensions
- Method extensions

Attribute extensions
Attribute extensions set a default value that can be overwritten.
For example, a custom is_color attribute on the token that defaults to False.
On INDIVIDUAL TOKENS, its value can be changed by overwriting it – in this case, True for the token "blue".
from spacy.tokens import Token
# Set extension on the Token with default value
Token.set_extension("is_color", default=False) tutti i token hanno questo attributo che di default è a false
doc = nlp("The sky is blue.")
# Overwrite extension attribute value
doc[3]._.is_color = True ma in questo caso è true           attributo

{properties in Python}
classe con variabile temperatura
non vuoi che vada sotto una certa soglia
la rendi privata (_temperature) e fai getter e settere che rispettano questo vincolo
However, the bigger problem with the above update is that all the programs that implemented our previous class have to modify their code from obj.temperature to obj.get_temperature() and all expressions like obj.temperature = val to obj.set_temperature(val).
This refactoring can cause problems while dealing with hundreds of thousands of lines of codes.
All in all, our new update was not backwards compatible. This is where @property comes to rescue.
temperature = property(get_temperature, set_temperature)
property object temperature. Simply put, property attaches some code (get_temperature and set_temperature) to the member attribute accesses (temperature).
any code that retrieves the value of temperature will automatically call get_temperature() instead of a dictionary (__dict__) look-up. Similarly, any code that assigns a value to temperature will automatically call set_temperature().
even when we created an object.
In Python, property() is a built-in function that creates and returns a property object. The syntax of this function is:
property(fget=None, fset=None, fdel=None, doc=None)
temperature = property(get_temperature, set_temperature)
equivalente a
# make empty property
temperature = property()
# assign fget
temperature = temperature.getter(get_temperature)
# assign fset
temperature = temperature.setter(set_temperature)
con decorators...

Property extensions
Property extensions work like properties in Python: they can define a getter function and an optional setter function.
The getter function is only called when you retrieve the attribute value. This lets you compute the value dynamically, and even take other custom attributes into account.
Getter functions take one argument: the object, in this case, the token. In this example, the function returns whether the token text is in our list of colors.
We can then provide the function via the getter keyword argument when we register the extension.
The token "blue" now returns True for ._.is_color.
from spacy.tokens import Token
# Define getter function
def get_is_color(token):
    colors = ["red", "yellow", "blue"]
    return token.text in colors
# Set extension on the Token with getter
Token.set_extension("is_color", getter=get_is_color)
doc = nlp("The sky is blue.")
print(doc[3]._.is_color, "-", doc[3].text)
output: True - blue
If you want to set extension attributes on a SPAN, you almost always want to use a property extension with a GETTER. 
Span extensions should almost always use a getter
Otherwise, you'd have to update every possible span ever by hand to set all the values.
In this example, the get_has_color function takes the span and returns whether the text of any of the tokens is in the list of colors.
After we've processed the doc, we can check different slices of the doc and the custom ._.has_color property returns whether the span contains a color token or not.
from spacy.tokens import Span
# Define getter function
def get_has_color(span):
    colors = ["red", "yellow", "blue"]
    return any(token.text in colors for token in span)
# Set extension on the Span with getter
Span.set_extension("has_color", getter=get_has_color)
doc = nlp("The sky is blue.")
print(doc[1:4]._.has_color, "-", doc[1:4].text)   stampi attributo che in automatico chiama getter
print(doc[0:2]._.has_color, "-", doc[0:2].text)
output:
True - sky is blue
False - The sky
ANY: The any(iterable) function returns True if any element of an iterable is True. If not, it returns False. 
iterable: list, string, dictionary etc.

Method extensions
- Method extensions make the extension attribute a callable method. Assign a function that becomes available as an object method
- You can then pass one or more arguments to it, and compute attribute values dynamically – for example, based on a certain argument or setting.
Lets you pass arguments to the extension function
In this example, the method function checks whether the doc contains a token with a given text. 
The first argument of the method is always the object itself – in this case, the doc. 
It's passed in AUTOMATICALLY when the method is called. 
All other function arguments will be arguments on the method extension. In this case, token_text.
Here, the custom ._.has_token method returns True for the word "blue" and False for the word "cloud".
from spacy.tokens import Doc
# Define method with arguments
def has_token(doc, token_text):
    in_doc = token_text in [token.text for token in doc]
    return in_doc
# Set extension on the Doc with method
Doc.set_extension("has_token", method=has_token)
doc = nlp("The sky is blue.")
print(doc._.has_token("blue"), "- blue")   # non passi come parametro il doc, è passato in automatico
print(doc._.has_token("cloud"), "- cloud")  stampi metodo, non attributo, perché devi passare parametri
output:
True - blue
False - cloud

print([(token.text, token._.is_country) for token in doc]) stampa una lista
[print(token.text, token._.is_country) for token in doc] stampa uno per uno ossia andando a capo
def get_reversed(token):
    return token.text[::-1]
    
SCALING AND PERFORMANCE
few tips and tricks to make your spaCy pipelines run as fast as possible, and process large volumes of text efficiently.

Processing large volumes of text
- If you need to process a lot of texts and create a lot of Doc objects in a row, the nlp.pipe method can speed this up significantly.
Use nlp.pipe method. It processes the texts as a stream and yields Doc objects. Much faster than calling nlp on each text. because it batches up the texts.
- nlp.pipe is a generator that yields Doc objects, so in order to get a list of docs, remember to call the list method around it.
BAD:
docs = [nlp(text) for text in LOTS_OF_TEXTS]
GOOD:
docs = list(nlp.pipe(LOTS_OF_TEXTS))

Passing in context 
- nlp.pipe also supports passing in tuples of text / context if you set as_tuples to True. 
Setting as_tuples=True on nlp.pipe lets you pass in (text, context) tuples
- The method will then yield doc / context tuples. Yields (doc, context) tuples   
otterrò tuple documento-metadati del documento, tramite i metadati posso settare attributi !!!!!!!!!!!
- This is useful for passing in additional metadata, like an ID associated with the text, or a page number.
Useful for associating metadata with the doc
data = [
    ("This is a text", {"id": 1, "page_number": 15}),       testo che è doc e metadati espressi tramite dizionario
    ("And another text", {"id": 2, "page_number": 16}),
]
for doc, context in nlp.pipe(data, as_tuples=True):
    print(doc.text, context["page_number"])
output:
This is a text 15
And another text 16
You can even add the context metadata to custom attributes.
In this example, we're registering two extensions, id and page_number, which default to None.
After processing the text and passing through the context, we can overwrite the doc extensions with our context metadata.
from spacy.tokens import Doc
Doc.set_extension("id", default=None)
Doc.set_extension("page_number", default=None)
data = [
    ("This is a text", {"id": 1, "page_number": 15}),
    ("And another text", {"id": 2, "page_number": 16}),
]
for doc, context in nlp.pipe(data, as_tuples=True):
    doc._.id = context["id"]
    doc._.page_number = context["page_number"]
    
Using only the tokenizer
Another common scenario: Sometimes you already have a model loaded to do other processing, but you only need the tokenizer for one particular text.
Running the whole pipeline is unnecessarily slow, because you'll be getting a bunch of predictions from the model that you don't need.
don't run the whole pipeline!
If you only need a tokenized Doc object, you can use the nlp.make_doc method instead, which takes a text and returns a doc.
Use nlp.make_doc to turn a text into a Doc object tokenizza e basta senza fare tutte le previsioni
This is also how spaCy does it BEHIND THE SCENES: nlp.make_doc turns the text into a doc before the pipeline components are called.
BAD:
doc = nlp("Hello world")
GOOD:
doc = nlp.make_doc("Hello world!")

Disabling pipeline components
immagine della pipeline https://course.spacy.io/pipeline.png
- spaCy also allows you to temporarily disable pipeline components using the nlp.disable_pipes context manager. 
Use nlp.disable_pipes to temporarily disable one or more pipes
It takes a variable number of arguments, the string names of the pipeline components to disable. 
For example, if you only want to use the entity recognizer to process a document, you can temporarily disable the tagger and parser.
# Disable tagger and parser
with nlp.disable_pipes("tagger", "parser"):
    # Process the text and print the entities
    doc = nlp(text)
    print(doc.ents)
IN the with block, spaCy will only run the remaining components.
AFTER the with block, the disabled pipeline components are automatically RESTORED. Restores them after the with block


for doc in list(nlp.pipe(TEXTS)):   questo no, MAI
    do something
se invece hai bisogno di una lista tipo per aggiungerla a pattern da matchare allora si, tipo qui: matcher.add("COUNTRY", None, *patterns) hai bisogno che patterns sia una lista
allora usa questo docs = list(nlp.pipe(TEXTS))

with open("exercises/en/tweets.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())
TEXTS è una lista che contiene tante stringhe

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for doc in (nlp.pipe(TEXTS)):   SI, se non hai bisogno di avere sotto forma di lista
    do something
    
docs = list(nlp.pipe(TEXTS)) SI, se hai bisogno di lista

for doc in list(nlp.pipe(TEXTS)):   NO, mai
    do something
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""

"""
# CHAPTER 4: Training a neural network model
In this chapter, you'll learn how to update spaCy's statistical models to customize them for your use case – 
for example, to predict a new entity type in online comments. 
You'll write your own training loop from scratch, and understand the basics of how training works, 
along with tips and tricks that can make your custom NLP projects more successful.
Welcome to the final chapter, which is about one of the most exciting aspects of modern NLP: 
TRAINING YOUR OWN MODELS!
In this lesson, you'll learn about training and updating spaCy's neural network models and the data you need for it – focusing specifically on the named entity recognizer.
Before we get starting with explaining how, it's worth taking a second to ask ourselves: 
Why would we want to update the model with our own examples? Why can't we just rely on pre-trained models?
Statistical models make predictions based on the examples they were trained on.
You can usually make the model more accurate by showing it examples from your domain. 
- Better results on your specific domain
You often also want to predict categories specific to your problem, so the model needs to learn about them.
- Learn classification schemes specifically for your problem
This is essential for text classification, very useful for entity recognition and a little less critical for tagging and parsing.
- Essential for text classification
- Very useful for named entity recognition
- Less critical for part-of-speech tagging and dependency parsing

How training works
spaCy supports updating existing models with more examples, and training new models.
1. Initialize the model weights randomly with nlp.begin_training
   If we're not starting with a pre-trained model, we first initialize the weights randomly.
2. Predict a few examples with the current weights by calling nlp.update
   Next, we call nlp.update, which predicts a batch of examples with the current weights.
3. Compare prediction with true labels
   The model then checks the predictions against the correct answers
4. Calculate how to change weights to improve predictions
   Decides how to change the weights to achieve better predictions next time.
5. Update weights slightly
   Finally, we make a small correction to the current weights and move on to the next batch of examples.
6. Go back to 2.
   We continue calling nlp.update for each batch of examples in the data. (pesi sono cambiati)
   
Here's an illustration showing the process. HOW TRAINING WORKS
immagine: https://course.spacy.io/training.png
Training data: Examples and their annotations. Examples we want to update the model with. Coppie input : output (label)
Text: The input text the model should predict a label for. A sentence, paragraph or longer document. 
      For the best results, it should be similar to what the model will see at runtime.
Label: The label the model should predict. The label is what we want the model to predict. è risultato giusto che confronteremo con risultato ottenuto
    This can be a text category, or an entity span and its type.
Gradient: How to change the weights. How we should change the model to reduce the current error. 
          It's computed when we compare the predicted label to the true label.
After training, we can then save out an updated model and use it in our application.

Example: Training the entity recognizer
Let's look at an example for a specific component: the entity recognizer.
- The entity recognizer takes a document and predicts phrases and their labels. The entity recognizer tags words and phrases in context.
This means that the training data needs to include texts, the entities they contain, and the entity labels.
- Entities can't overlap, so each token can only be part of one entity.
- Examples need to come with context. Because the entity recognizer predicts entities in context, 
it also needs to be trained on entities and their surrounding context.

The easiest way to do this is to show the model a TEXT and a LIST OF CHARACTER OFFSETS. 
For example, "iPhone X" is a gadget, starts at character 0 and ends at character 8.
("iPhone X is coming", {"entities": [(0, 8, "GADGET")]}) --- Training data
It's also very important for the model to learn words that aren't entities. Texts with no entities are also important
In this case, the list of span annotations will be empty.
("I need a new phone! Any tips?", {"entities": []}) --- Training data
Goal: teach the model to generalize. Teach the model to recognize new entities in similar contexts, even if they weren't in the training data.

The training data
Examples of what we want the model to predict in context. The training data tells the model what we want it to predict. This could be texts and named entities we want to recognize, or tokens and their correct part-of-speech tags.
Update an existing model: a few hundred to a few thousand examples. 
Train a new category: a few thousand to a million examples
spaCy's English models: 2 million words. spaCy's pre-trained English models for instance were trained on 2 million words labelled with part-of-speech tags, dependencies and named entities.
The training data is usually created manually by human annotators (who assign labels to texts)
This is a lot of work, can be semi-automated – for example, using spaCy's Matcher!

esercizi

While spaCy comes with a range of pre-trained models to predict linguistic annotations, 
you almost always want to fine-tune them with more examples. You can do this by training them with more labelled data.
help with: Improve model accuracy on your data, Learn new classification schemes
not help with: Discover patterns in unlabelled data.
spaCy’s components are supervised models for text annotations, meaning they can only learn to reproduce examples, not guess new labels from raw text.

spaCy’s rule-based Matcher is a great way to quickly create training data for named entity models. 
A LIST of sentences is available as the variable TEXTS. You can print it to inspect it. 
We want to find all mentions of different iPhone models, so we can create training data to teach a model to recognize them as "GADGET".
Write a pattern for two tokens whose lowercase forms match "iphone" and "x".
Write a pattern for two tokens: one token whose lowercase form matches "iphone" and a digit.
import json
from spacy.matcher import Matcher
from spacy.lang.en import English
with open("exercises/en/iphone.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())
nlp = English()
matcher = Matcher(nlp.vocab)
# Two tokens whose lowercase forms match "iphone" and "x"
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]
# Token whose lowercase form matches "iphone" and a digit
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]
# Add patterns to the matcher and check the result
matcher.add("GADGET", None, pattern1, pattern2)
for doc in nlp.pipe(TEXTS):
    print([doc[start:end] for match_id, start, end in matcher(doc)])
output:
[iPhone X]
[iPhone X]
[iPhone X]
[iPhone 8]
[iPhone 11, iPhone 8]
[]  ?
✔ Nice! Now let's use those patterns to quickly bootstrap some TRAINING DATA for our model.
Let’s use the match patterns we’ve created in the previous exercise to bootstrap a set of training examples. A list of sentences is available as the variable TEXTS.
Create a doc object for each text using nlp.pipe.
Match on the doc and create a list of matched spans.
Get (start character, end character, label) tuples of matched spans. start_char e end_char sono attributi di span già esistenti, built in
Format each example as a tuple of the text and a dict, mapping "entities" to the entity tuples.
Append the example to TRAINING_DATA and inspect the printed data.
import json
from spacy.matcher import Matcher
from spacy.lang.en import English

with open("exercises/en/iphone.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = English()
matcher = Matcher(nlp.vocab)
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]
matcher.add("GADGET", None, pattern1, pattern2)

TRAINING_DATA = []

# Create a Doc object for each text in TEXTS
for doc in nlp.pipe(TEXTS):
    # Match on the doc and create a list of matched spans
    spans = [doc[start:end] for match_id, start, end in matcher(doc)]
    # Get (start character, end character, label) tuples of matches
    entities = [(span.start_char, span.end_char, "GADGET") for span in spans]
    # Format the matches as a (doc.text, entities) tuple
    training_example = (doc.text, {"entities": entities})
    # Append the example to the training data
    TRAINING_DATA.append(training_example)
print(*TRAINING_DATA, sep="\n") -> con * davanti gli elementi della lista sono concepiti come argomenti separati, quindi quando stampo con \n come separatore mi va a capo dopo ogni elemento della lista
                                    senza * lista è unico argomento, va a capo dopo aver stampato tutta la lista, quindi singoli elementi stanno accanto


THE TRAINING LOOP
While some other libraries give you one method that takes care of training a model, spaCy gives you full control over the training loop.

The steps of a training loop
The training loop is a series of steps that's performed to train or update a model. 
1. Loop for a number of times
   We usually need to perform it several times, for multiple iterations, so that the model can learn from it effectively. If we want to train for 10 iterations, we need to loop 10 times.
2. Shuffle the training data.
   To prevent the model from getting stuck in a suboptimal solution, we randomly shuffle the data for each iteration. This is a very common strategy when doing stochastic gradient descent.
3. Divide the data into batches
   Next, we divide the training data into batches of several examples, also known as minibatching. This increases the reliability of the gradient estimates.
4. Update the model for each batch.
   Finally, we update the model for each batch, and start the loop again until we've reached the last iteration.
5. Save the updated model.
   We can then save the model to a directory and use it in spaCy.
   
training loop recap

training loop EXAMPLE
Let's imagine we have a list of training examples consisting of texts and entity annotations.
TRAINING_DATA = [
    ("How to preorder the iPhone X", {"entities": [(20, 28, "GADGET")]})
    # And many more examples...
]
We want to loop for 10 iterations, so we're iterating over a range of 10.
for i in range(10):
    Next, we use the random module to randomly shuffle the training data.
    random.shuffle(TRAINING_DATA)
    We then use spaCy's minibatch utility function to divide the examples into batches.
    for batch in spacy.util.minibatch(TRAINING_DATA):
        For each batch, we get the texts and annotations and call the nlp.update method to update the model.
        texts = [text for text, annotation in batch]
        annotations = [annotation for text, annotation in batch]
        nlp.update(texts, annotations)
Finally, we call the nlp.to_disk method to save the trained model to a directory.
nlp.to_disk(path_to_model)

Updating an existing model
Improve the predictions on new data. spaCy lets you update an existing pre-trained model with more data – for example, to improve its predictions on different texts.
Especially useful to improve existing categories, like "PERSON". This is especially useful if you want to improve categories the model already knows, like "person" or "organization".
Also possible to add new categories. You can also update a model to add new categories.
Be careful and make sure the model doesn't "forget" the old ones. Just make sure to always update it with examples of the new category and examples of the other categories it previously predicted correctly. Otherwise improving the new category might hurt the other categories.

Setting up a new pipeline from scratch
In this example, we start off with a blank English model using the spacy.blank method. The blank model doesn't have any pipeline components, only the language data and tokenization rules.
We then create a blank entity recognizer and add it to the pipeline.
Using the add_label method, we can add new string labels to the model.
We can now call nlp.begin_training to initialize the model with random weights.
To get better accuracy, we want to loop over the examples more than once and randomly shuffle the data on each iteration.
On each iteration, we divide the examples into batches using spaCy's minibatch utility function. Each example consists of a text and its annotations.
Finally, we update the model with the texts and annotations and continue the loop.
# Start with blank English model
nlp = spacy.blank("en")
# Create blank entity recognizer and add it to the pipeline
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
# Add a new label
ner.add_label("GADGET")
# Start the training
nlp.begin_training()
# Train for 10 iterations
for itn in range(10):
    random.shuffle(examples)
    # Divide examples into batches
    for batch in spacy.util.minibatch(examples, size=2):
        texts = [text for text, annotation in batch]
        annotations = [annotation for text, annotation in batch]
        # Update the model
        nlp.update(texts, annotations)
        
Time to practice! Now that you've seen the training loop, let's use the data created in the previous exercise to update a model.

exercise

In this exercise, you’ll prepare a spaCy pipeline to train the entity recognizer to recognize "GADGET" entities in a text – for example, “iPhone X”.
import spacy
# Create a blank "en" model
nlp = spacy.blank("en")
# Create a new entity recognizer and add it to the pipeline
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
# Add the label "GADGET" to the entity recognizer
ner.add_label("GADGET")
The pipeline is now ready, so let's start writing thetraining loop.
Let’s write a simple training loop from scratch!
The pipeline you’ve created in the previous exercise is available as the nlp object. It already contains the entity recognizer with the added label "GADGET".   
The small set of labelled examples that you’ve created previously is available as TRAINING_DATA. To see the examples, you can print them in your script.
Call nlp.begin_training, create a training loop for 10 iterations and shuffle the training data.
Create batches of training data using spacy.util.minibatch and iterate over the batches.
Convert the (text, annotations) tuples in the batch to lists of texts and annotations.
For each batch, use nlp.update to update the model with the texts and annotations.

import spacy
import random
import json

with open("exercises/en/gadgets.json", encoding="utf8") as f:
    TRAINING_DATA = json.loads(f.read())   text: annotations

nlp = spacy.blank("en")
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
ner.add_label("GADGET")

# Start the training
nlp.begin_training()

# Loop for 10 iterations
for itn in range(10):
    # Shuffle the training data
    random.shuffle(TRAINING_DATA)
    losses = {}

    # Batch the examples and iterate over them
    for batch in spacy.util.minibatch(TRAINING_DATA, size=2):
        texts = [text for text, entities in batch]
        annotations = [entities for text, entities in batch]

        # Update the model
        nlp.update(texts, annotations, losses=losses)
    print(losses)

you've successfully trained your first spaCy model. The numbers printed to the shell represent the loss on each iteration, the amount of
work left for the optimizer. The lower the number, the better. In real life, you normally want to use *a lot* more data than this, ideally at least a few hundred
or a few thousand examples.

Let’s see how the model performs on unseen data!
o speed things up a little, we already ran a trained model for the label "GADGET" over some text. Here are some of the results:


BEST PRACTICES for training spaCy models
When you start running your own experiments, you might find that a lot of things just don't work the way you want them to. And that's okay.
Training models is an iterative process, and you have to try different things until you find out what works best.
In this lesson, I'll be sharing some best practices and things to keep in mind when training your own models.
Let's take a look at some of the problems you may come across.

Problem 1: Models can "forget" things
Statistical models can learn lots of things – but it doesn't mean that they won't unlearn them.
Existing model can overfit on new data. If you're updating an existing model with new data, especially new labels, it can overfit and adjust too much to the new examples.
for example if you only update it with "WEBSITE", it can "unlearn" what a "PERSON" is. For instance, if you're only updating it with examples of "website", it may "forget" other labels it previously predicted correctly – like "person".
Also known as "catastrophic forgetting" problem

Solution 1: Mix in previously correct predictions
To prevent this, make sure to always mix in examples of what the model previously got correct.
For example, if you're training "WEBSITE", also include examples of "PERSON". If you're training a new category "WEBSITE", also include examples of "PERSON".
Run existing spaCy model over data and extract all other relevant entities. spaCy can help you with this. You can create those additional examples by running the existing model over data and extracting the entity spans you care about.
You can then mix those examples in with your existing data and update the model with annotations of all labels.
BAD:
TRAINING_DATA = [
    ("Reddit is a website", {"entities": [(0, 6, "WEBSITE")]})
]
GOOD:
TRAINING_DATA = [
    ("Reddit is a website", {"entities": [(0, 6, "WEBSITE")]}),
    ("Obama is a person", {"entities": [(0, 5, "PERSON")]})
]

Problem 2: Models can't learn everything
Another common problem is that your model just won't learn what you want it to.
spaCy's models make predictions based on local context. spaCy's models make predictions based on the local context – for example, for named entities, the surrounding words are most important.
Model can struggle to learn if decision is difficult to make based on context. If the decision is difficult to make based on the context, the model can struggle to learn it.
Label scheme needs to be consistent and not too specific
For example: "CLOTHING" is better than "ADULT_CLOTHING" and "CHILDRENS_CLOTHING" For example, it may be very difficult to teach a model to predict whether something is adult clothing or children's clothing based on the context. However, just predicting the label "clothing" may work better.

Solution 2: Plan your label scheme carefully
Before you start training and updating models, it's worth taking a step back and planning your label scheme.
Pick categories that are reflected in local context. More GENERIC is better than too specific. Try to pick categories that are reflected in the local context and make them more generic if possible.
Use rules to go from generic labels to specific categories. You can always add a rule-based system LATER to go from generic to SPECIFIC.
Generic categories like "clothing" or "band" are both easier to label and easier to learn.
BAD:
LABELS = ["ADULT_SHOES", "CHILDRENS_SHOES", "BANDS_I_LIKE"]
GOOD:
LABELS = ["CLOTHING", "BAND"]

Whether a place is a tourist destination is a subjective judgement and not a definitive category. It will be very difficult for the entity recognizer to learn.
A much better approach would be to only label "GPE" (geopolitical entity) or "LOCATION" and then use a rule-based system to determine whether the entity is a tourist destination in this context. For example, you could resolve the entities types back to a knowledge base or look them up in a travel wiki. ???
rule based system : dictionary with finite number of examples    per esempio

Here’s a small sample of a dataset created to train a new entity type "WEBSITE". 
The original dataset contains a few thousand sentences. In this exercise, you’ll be doing the labeling by hand. In real life, you probably want to automate this and use an annotation tool – for example, Brat, a popular open-source solution, or Prodigy, our own annotation tool that integrates with spaCy.
Complete the entity offsets for the "WEBSITE" entities in the data. Feel free to use len() if you don’t want to count the characters.   non len più uno, idiota


If "PERSON" entities occur in the training data but aren’t labelled, the model will learn that they shouldn’t be predicted. Similarly, if an existing entity type isn’t present in the training data, the model may ”forget” and stop predicting it.

RECAP MEGAGALATTICO

Here's an overview of all the new skills you learned so far:

Extract linguistic features: part-of-speech tags, dependencies, named entities, Work with pre-trained statistical models, 
In the first chapter, you learned how to extract linguistic features like part-of-speech tags, syntactic dependencies and named entities, and how to work with pre-trained statistical models.

Find words and phrases using Matcher and PhraseMatcher match rules
You also learned to write powerful match patterns to extract words and phrases using spaCy's matcher and phrase matcher.

Best practices for working with data structures Doc, Token Span, Vocab, Lexeme
Chapter 2 was all about information extraction, and you learned how to work with the data structures, the Doc, Token and Span, as well as the Vocab and lexical entries.

Find semantic similarities using word vectors
You also used spaCy to predict semantic similarities using word vectors.

Write custom pipeline components with extension attributes
In chapter 3, you got some more insights into spaCy's pipeline, and learned to write your own custom pipeline components that modify the doc.

Scale up your spaCy pipelines and make them fast
You also created your own custom extension attributes for docs, tokens and spans, and learned about processing streams and making your pipeline faster.

Create training data for spaCy' statistical models, Train and update spaCy's neural network models with new data
Finally, in chapter 4, you learned about training and updating spaCy's statistical models, specifically the entity recognizer.


You learned some useful tricks for how to create training data, and how to design your label scheme to get the best results.

More things to do with spaCy
Training and updating other pipeline components
    Part-of-speech tagger
    Dependency parser
    Text classifier -> which can learn to predict labels that apply to the whole text. It's not part of the pre-trained models, but you can add it to an existing model and train it on your own data.
Customizing the tokenizer
    Adding rules and exceptions to split text differently
Adding or improving support for other languages
    55+ languages currently
    Lots of room for improvement and more languages
    Allows training models for other languages
    
For more examples, tutorials and in-depth API documentation, check out the spaCy websit
spacy.io

blank means vuoto

span diventa token --->
with doc.retokenize() as retokenizer:
    retokenizer.merge(span)
    

"""
