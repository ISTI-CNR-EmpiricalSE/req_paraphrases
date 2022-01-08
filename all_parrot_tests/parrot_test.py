import time
import os
import sys

from parrot import Parrot
import torch
import warnings


def help_message():
    """Function that prints the help message on the standard output
        It is printed every time you insert on command line something incorrect
    """
    print("You have to choose between one of these three assets:")
    print("number of arguments =")
    print("0                        - default configuration, do all datasets from n1 included to n23 exluded")
    print("False n1,n5...           - not a cycle, but singles dataset n1 and n5")
    print("True n1,n5               - a cycle that goes from n2 included and n5 excluded")


def parrot_test_func():
    """Function that executes Parrot augment function on the datasets accordingly to command line arguments
        It produces the relative output files putting them in the directory results,
        inside the directory of the relative dataset
        Format of the input file: data_set_index.txt
        Format of the output file: results_file_index.txt
    """

    # I want to have the possibility to insert the dataset on which operate from command line
    # on the contrary, I identified the best asset of parameters, so they are fixed

    # INSTRUCTIONS:
    # number of arguments =
    # 0                         - default configuration, do all datasets from n1 included to n23 exluded
    # False n1,n5...            - not a cycle, but singles dataset n1 and n5
    # True n1,n5                - a cycle that goes from n2 included and n5 excluded

    start_index = None
    end_index = None
    data_set_list = []

    if len(sys.argv)-1 == 0:
        start_index = 1
        end_index = 24
    elif sys.argv[1] != "True" and sys.argv[1] != "False":
        help_message()
        return
    else:
        if sys.argv[1] == "True":
            if len(sys.argv)-2 != 2:
                help_message()
                return
            else:
                start_index = int(sys.argv[2])
                end_index = int(sys.argv[3])
        elif sys.argv[1] == "False":
            if len(sys.argv)-2 == 0:
                help_message()
                return
            else:
                # name false 1 5 3
                data_set_list = []
                for i in range(2, len(sys.argv)):
                    data_set_list.append(int(sys.argv[i]))

    warnings.filterwarnings("ignore")

    # uncomment to get reproducable paraphrase generations
    # In order to allow reproducibility of the text paraphrasing, the random seed number will be set.
    # What this does is produce the same results for the same seed number (even if it is re-run multiple times).
    def random_state(seed):
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)

    random_state(1234)

    tic1 = time.perf_counter()

    # Init models (make sure you init ONLY once if you integrate this to your code)
    # this was not working but I did pip install protobuf and it worked
    # it was giving this error --->
    # ImportError: T5 Converter requires the protobuf library but it was not found in your environment.
    # Checkout the instructions on the installation page of its repo:
    # https://github.com/protocolbuffers/protobuf/tree/master/python#installation
    # and follow the ones that match your environment.
    # Protocol Buffers are Google’s data interchange format
    parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")

    toc1 = time.perf_counter()

    print(f"Downloaded the parrot_paraphraser_on_T5 in {toc1 - tic1:0.4f} seconds")

    data_set_index_list = []
    if start_index is not None and end_index is not None:
        data_set_index_list = range(start_index, end_index)
        print("doing data_sets from " + str(start_index) + " included to " + str(end_index) + " excluded")
    elif data_set_list is not None:
        data_set_index_list = data_set_list
        print("doing data_sets:")
        print(data_set_index_list)
    else:
        help_message()
        return

    for data_set_index in data_set_index_list:

        tic0 = time.perf_counter()

        my_file = open("../data_sets/data_set_" + str(data_set_index) + ".txt", "r")
        phrases = my_file.read().splitlines()
        # phrases = ["As a Public User, I want to Search for Information, so that I can obtain publicly available
        # information concerning properties, County services, processes and other general information."]

        # Perform the paraphrasing using the parrot.augment() function
        # that takes in as input argument the phrase being iterated.
        # Generated paraphrases are assigned to the para_phrases variable.

        # this was to have different configurations of values
        # for each configuration you have a different file (file_index)
        # at the beginning of the file you have the configuration
        # at the end the time for that particular file
        # at the end of the last file you also have the total time (for all files together)
        # but we identified the best configuration which is the following
        # so if we execute the script with these values (and this is what we do)
        # we end up having only one file (result_1 with file_index=1) at the end of which we have single and total time
        use_gpu_array = [False]
        diversity_ranker_array = ["levenshtein"]
        do_diverse_array = [True]
        max_return_phrases_array = [15]
        max_length_array = [32]
        adequacy_threshold_array = [0.50]
        fluency_threshold_array = [0.1]

        dir = "../results/data_set_" + str(data_set_index)
        if not os.path.exists(dir):
            os.makedirs(dir)

        file_index = 1

        for a in use_gpu_array:
            for x in diversity_ranker_array:
                for y in do_diverse_array:
                    for z in max_return_phrases_array:
                        for w in max_length_array:
                            for i in adequacy_threshold_array:
                                for j in fluency_threshold_array:
                                    tic2 = time.perf_counter()

                                    # examples
                                    # results/data_set_1_second/results_1.txt
                                    # results/data_set_1_second/results_2.txt
                                    f = open(dir + "/" + "results_" + str(file_index) + ".txt", "w")
                                    file_index = file_index + 1
                                    f.write("use_gpu = " + str(a) + "\n")
                                    f.write("diversity_ranker = " + x + "\n")
                                    f.write("do_diverse = " + str(y) + "\n")
                                    f.write("max_return_phrases = " + str(z) + "\n")
                                    f.write("max_length = " + str(w) + "\n")
                                    f.write("adequacy_threshold = " + str(i) + "\n")
                                    f.write("fluency_threshold = " + str(j) + "\n")
                                    f.write("\n")
                                    phrase_index = 1
                                    for phrase in phrases:
                                        f.write("-"*100)
                                        f.write("\n")
                                        f.write(str(phrase_index) + ") ")
                                        phrase_index = phrase_index + 1
                                        f.write("Input_phrase: " + phrase)
                                        f.write("\n")
                                        f.write("-"*100)
                                        f.write("\n")

                                        tic3 = time.perf_counter()
                                        para_phrases = parrot.augment(input_phrase=phrase,
                                                                      use_gpu=a,
                                                                      diversity_ranker=x,
                                                                      do_diverse=y,
                                                                      max_return_phrases=z,
                                                                      max_length=w,
                                                                      adequacy_threshold=i,
                                                                      fluency_threshold=j)
                                        toc3 = time.perf_counter()
                                        print(f"Time for the augment function:  {toc3 - tic3:0.4f} seconds")

                                        # it was giving problems iterating on an empty list
                                        # if it given no paraphrases the list is empty
                                        # empty list = None = False
                                        if not para_phrases:
                                            para_phrases = ["None"]

                                        for para_phrase in para_phrases:
                                            f.write(str(para_phrase) + "\n")

                                        toc2 = time.perf_counter()
                                    f.write("\n")
                                    f.write(f"Got the paraphrases in {toc2 - tic2:0.4f} seconds")  # single file
                                    f.write("\n")

        toc0 = time.perf_counter()
        f = open(dir + "/" + "results_" + str(file_index - 1) + ".txt", "a")
        f.write("\n")
        f.write(f"Total time = {toc0 - tic0:0.4f} seconds = {(toc0 - tic0) / 60:0.4f} "
                f"minutes = {((toc0 - tic0) / 60 / 60):0.4f} hours") # all files of dataset


if __name__ == '__main__':
    parrot_test_func()

'''
a good paraphrase should be adequate and fluent while being as different as possible on the surface lexical form. With respect to this definition, the 3 key metrics that measures the quality of paraphrases are:

    Adequacy (Is the meaning preserved adequately?)
    Fluency (Is the paraphrase fluent English?)
    Diversity (Lexical / Phrasal / Syntactical) (How much has the paraphrase changed the original sentence?)
'''


'''
In the space of conversational engines, 
- knowledge bots (simulatori) are to which we ask questions like "when was the Berlin wall teared down?", 
- transactional bots are to which we give commands like "Turn on the music please" and 
- voice assistants are the ones which can do both answer questions and action our commands. 
Parrot mainly foucses on AUGMENTING texts typed-into or spoken-to conversational interfaces for building robust NLU models. 
per avere tanti dati su cui allenare modello senza dovere effettivamente collezionare
Techniques are used to increase the amount of data by adding slightly modified copies of already existing data or newly created synthetic data from existing data.” So data augmentation involves creating new and representative data.
(So usually people neither type out or yell out long paragraphs to conversational interfaces. 
Hence the pre-trained parrot_paraphraser_on_T5 is trained on text samples of maximum length of 32.)
'''
# While Parrot predominantly aims to be a text augmentor for building good NLU models, it can also be used as a pure-play paraphraser.

'''
ESITI ---> 
- max_return_phrases = 2
- fluency = 0.90 
- adequacy = 0.99
- diversity_ranker = "levenshtein"
- maxlentgh = 32
- do diverse = sia true che false

riformula le user stories pressoché nello stesso modo
la sola cosa che modifica è punteggiatura, maiuscole e minuscole, oppure toglie o mette pronomi relativi
(con frasi più semplici rispetto a questi requirements funziona)
'''

'''
ESITI --->
- max_return_phrases = 10 (ne genera anche 6 7)
- fluency = 0.90 
- adequacy = 0.99
- diversity_ranker = "levenshtein"
- maxlentgh = 32

-- do_diverse = true perlomeno le prime tre diverse --- BEST
----------------------------------------------------------------------------------------------------
Input_phrase:  As a UI designer, I want to redesign the Resources page, so that it matches the new Broker design styles.
----------------------------------------------------------------------------------------------------
+ ('the resources page should be redesigned as a ui designer so that it matches the new broker design styles', 48)
+ ('i would like to redesign the resources page as a ui designer so that it matches the new broker design styles', 48)
+ ('i would like to redesign the resources page so that it matches the new broker design styles', 31)
('as a ui designer i want to redesign the resources page so it matches the new broker design styles', 18)
('as a ui designer i want to redesign the resources page so that it matches the new broker design style', 14)
('as a ui designer i want to redesign the resources page so that it matches the new broker design styles', 13)
('as a ui designer  i want to redesign the resources page so that it matches the new broker design styles ', 13)

-- do_diverse = false vengono davvero troppo uguali credo
----------------------------------------------------------------------------------------------------
Input_phrase:  As a UI designer, I want to redesign the Resources page, so that it matches the new Broker design styles.
----------------------------------------------------------------------------------------------------
('i want to redesign the resources page as a ui designer so it matches the new broker design styles', 47)
('i want to redesign the resources page as a ui designer so that it matches the new broker design styles', 47)
('as a ui designer i want to redesign the resources page so that it corresponds to the new broker design styles', 26)
('as a ui designer i want to redesign the resources page so it matches the new broker design styles', 18)
('as ui designer i want to redesign the resource page so that it matches the new broker design styles', 16)
('as a ui designer i want to redesign the resources page so that it matches the new broker design styles', 13)
'''

'''
ESITI ---> 
- fluency = 0.99 
- adequacy = 0.99
- do_diverse = true 
- max ret phrases = 10
- maxlentgh = 32
- diversity_ranker = "levenshtein"
restituisce stessa e identica frase
'''

'''
ESITI --->
- adequacy = 1 
- do diverse = true 
- fluency = 0.90 
- max ret phrases = 10
- maxlentgh = 32
- diversity_ranker = "levenshtein"
none
'''

'''
ESITI --->
maxlentgh = 64 (di solito è 32)
non cambia molto
'''

'''
ESITI --->
- max_return_phrases = 10 
- fluency = 0.99 alzare troppo la fluency porta a non avere risultati
- adequacy = 0.90
- con do_diverse = true 
- maxlentgh = 32
- diversity_ranker = "levenshtein"
----------------------------------------------------------------------------------------------------
Input_phrase:  As a UI designer, I want to redesign the Resources page, so that it matches the new Broker design styles.
----------------------------------------------------------------------------------------------------
('As a UI designer, I want to redesign the Resources page, so that it matches the new Broker design styles.', 0)
'''

'''
ESITI --->
- max_return_phrases = 10 
- fluency = 0.90 
- adequacy = 0.90 abbasso adequacy, non cambia nulla, rosultati sono come adeqaucy a 0.99 (esempio standard)
- con do_diverse = true 
- maxlentgh = 32
- diversity_ranker = "levenshtein"
----------------------------------------------------------------------------------------------------
Input_phrase:  As a UI designer, I want to redesign the Resources page, so that it matches the new Broker design styles.
----------------------------------------------------------------------------------------------------
('i would like to redesign the resources page as a ui designer so that it matches the new broker design styles', 48)
('the resources page should be redesigned as a ui designer so that it matches the new broker design styles', 48)
('i would like to redesign the resources page so that it matches the new broker design styles', 31)
('as a ui designer i want to redesign the resources page so it matches the new broker design styles', 18)
('as a ui designer i want to redesign the resources page so that it matches the new broker design style', 14)
('as a ui designer i want to redesign the resources page so that it matches the new broker design styles ', 13)
('as a ui designer i want to redesign the resources page so that it matches the new broker design styles', 13)
'''

'''
PROBLEMA RISOLTO
se metto tutte user stories di un certo file dentro a una lista su cui itero a un certo punto mi da seguente errore --->
Traceback (most recent call last):
  File "/home/isabella/.config/JetBrains/PyCharmCE2021.2/scratches/parrot_test.py", line 46, in <module>
    for para_phrase in para_phrases:
TypeError: 'NoneType' object is not iterable
è come se non avesse trovato parafrasi e quindi poi lista fosse vuota o meglio non creata e quindi poi non può iterare?
SOL è creare lista vuota primae fare la APPEND di parafrasi così al massimo non da risultati ma non da errori - infatti così si risolve, se non ci sono parafrasi il risultato che da è none
# però
# se fai append è come se facessi append si una lista a lista, brutto
# controllo se è false dopo aver fatto append, in caso lo metti come lista contenente solo stringa none
# perché il problema è che se lo metto prima come lista vuota e parafrasi esistono poi faccio append di una lista a una lista quidi print finale è di una lista
# se non lo inizializzo a lista vuota e mi affido solo a augment, nel caso augment non restituisca nulla poi quando ci itero mi da errore
# quindi inizializzo con augment, ma se poi continua a essere falso significa che non hai assegnato nulla e quindi lo metti a lista vuota contenente none
# in realtà se non c'erano parafrasi para_phrases non è lista vuota (che vale false) (non ci sarebbero problemi a iterare su lista vuota), ma è None, ma anche None vale false !!!
'''

'''
TIME
la parafrasi (augment function) -> 6.2 secondi
                                    (se max ret phrase = 2 -> 3 sec)
scaricare il modello -> 60 secondi (1 minuto) oppure anche
                        317 (5 minuti)
'''

'''
impiega tanto a scaricare il modello perché lo scarica dalla rete, se non è connesso a internet non funziona
'''

'''
se usi altri diversity_ranker ovviamente ouput sono stessi, semplicemente valuta la distanza in modo diverso
'''

'''
con seme
non capisco differenza
'''



