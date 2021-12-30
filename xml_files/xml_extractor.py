from nltk.stem.porter import PorterStemmer
from xml.dom.minidom import *
import nltk
import sys
import xml.dom.minidom

REQ_TAG = 'req'
ID_TAG = 'id'
BODY_TAG = 'text_body'


def __get_text(node, current_text):
    if node.nodeType == Node.TEXT_NODE and \
            not node.parentNode._get_tagName() == 'modifier' and \
            not node.parentNode._get_tagName() == 'crossref' and \
            not node.data.isspace() and \
            not node.data == None:
        current_text.append(node.data)
        print("here1" + node.data)
    else:
        for sub_node in node.childNodes:
            __get_text(sub_node, current_text)

# parse xml file
doc = xml.dom.minidom.parse('2006 - eirene sys 15.xml')
output_file = open("2006 - eirene sys 15_output.txt", "w")

reqs = doc.getElementsByTagName(REQ_TAG)

for req in reqs:
    req_id = req.getAttribute(ID_TAG)
    text = list()
    __get_text(req, text)
    req_item = [req_id, text]
    print(text)
    output_file.write(text)




