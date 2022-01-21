# generate ic file

import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
import codecs

reader_bnc = nltk.corpus.reader.BNCCorpusReader(root='../Corpus/2554/2554/download/Texts/', fileids=r'[A-K]/\w*/\w*\.xml')
bnc_ic = wn.ic(reader_bnc, False, 0.0)

def is_root(synset_x):
    if synset_x.root_hypernyms()[0] == synset_x:
        return True
    return False

def generate_ic_file(IC, output_filename):
    """Dump in output_filename the IC counts.
    The expected format of IC is a dict
    {'v':defaultdict, 'n':defaultdict, 'a':defaultdict, 'r':defaultdict}"""
    with codecs.open(output_filename, 'w', encoding='utf-8') as fid:
        # Hash code of WordNet 3.0
        fid.write("wnver::eOS9lXC6GvMWznF1wkZofDdtbBU"+"\n")

        # We only stored nouns and verbs because those are the only POS tags
        # supported by wordnet.ic() function
        for tag_type in ['v', 'n']:#IC:
            for key, value in IC[tag_type].items():
                if key != 0:
                    synset_x = wn.of2ss(of="{:08d}".format(key)+tag_type)
                    if is_root(synset_x):
                        fid.write(str(key)+tag_type+" "+str(value)+" ROOT\n")
                    else:
                        fid.write(str(key)+tag_type+" "+str(value)+"\n")
    print("Done")

generate_ic_file(bnc_ic, "../custom.dat")

custom_ic = wordnet_ic.ic('../custom.dat')
