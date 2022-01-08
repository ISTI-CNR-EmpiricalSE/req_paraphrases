from nltk.stem.porter import PorterStemmer
from xml.dom.minidom import *
import nltk
import sys
import xml.dom.minidom


doc = xml.dom.minidom.parse('2006 - eirene sys 15.xml')
reqs = doc.getElementsByTagName('text_body')
for req in reqs:
    print(req.firstChild.data)




