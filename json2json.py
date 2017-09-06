import re
import sys
import json
import nltk
import string
import html2text
import datetime

from itertools import chain
from tidylib import tidy_document
from nltk.corpus import stopwords
from nltk import word_tokenize,sent_tokenize




def PrePrcs(body):
    document, errors = tidy_document(body)  # tidy_document

    h = html2text.HTML2Text() # html2text
    h.ignore_links = True
    h.ignore_images = True
    text = h.handle(document).encode('ascii',errors='ignore')

    text = text.strip(string.punctuation)  # clean words with punctuation
    sentences = nltk.sent_tokenize(text) # divide text to sentences

    words = []    # divide sentences to words
    for sentence in sentences:
        words.append(nltk.word_tokenize(sentence))

    delEStr = string.punctuation + ' ' + string.digits  # delete punctuation in words list
    cleanwords = [''.join(c for c in s if c not in delEStr) for s in list(chain(*words))]

    smallwords = []   # delete word's length <3 and word's lower characters
    for s in cleanwords:
        if (len(s) > 2) and (len(s) < 30):
            smallwords.append(s.lower())
        else:
            continue

    # delete stopwords
    list_stopWords = list(set(stopwords.words('english')))
    # add ' ' among words
    finalwords = [w+' ' for w in smallwords if not w in list_stopWords]

    return ''.join(finalwords)

def generatejson(ip, text):
    def convert_to_builtin_type(obj):
        # print 'default(', repr(obj), ')'
        d = {}
        d.update(obj.__dict__)
        return d

    class Myobject():
        ip = ''
        text = ''
        def __init__(self, ip, text):
            self.ip = ip
            self.text = text

    obj= Myobject(ip, text)

    try:
        return json.dumps(obj, default = convert_to_builtin_type) + '\n'
    except TypeError, err:
        print 'ERROR:', err

if __name__ == '__main__':
    starttime = datetime.datetime.now()
    #long running

    Infile = open("8.json",'r')
    Outfile = open("newjson8.json",'w')

    # for line in Infile.readlines():
    totallinenum = len(open("8.json").readlines())
    print totallinenum
    i = 0

    for line in open("8.json"):
        # read a line from file
        line = Infile.readline()

        # extract json format, and get related elements
        hjson = json.loads(line)
        status = hjson['status']
        ip = hjson['ip']
        body = hjson['body']

        # display time escaped and complete work's percent
        i = i + 1
        percent = 100 * 1.0 * i / totallinenum

        endtime = datetime.datetime.now()
        sys.stdout.write('\r running time : %d' %(endtime-starttime).seconds + ' seconds' + ', complete percent: ' + str(percent) + '%' + ', ip: ' + ip)
        sys.stdout.flush()

        # filter unreadable characters
        body = re.sub(r'[^\x00-\x7f]', '', body)

        # filter error-responses
        if int(status) == 200:
            text = PrePrcs(body)
        else:
            continue

        if len(text) == 0:
            continue

        wjson = generatejson(ip, text)
        Outfile.write(wjson)
        # Outfile.flush()

    Outfile.close()
    Infile.close()
