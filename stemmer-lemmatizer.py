import nltk
import json
from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer

Infile = open("lan2check.json",'r')
Outfile = open("check2stemmer.json",'w')

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


for line in open("lan2check.json"):
        # read a line from file
    line = Infile.readline()

        # extract json format, and get related elements
    hjson = json.loads(line)
    ip = hjson['ip']
    body = hjson['text']

    text = ""
    lemmatizer = nltk.WordNetLemmatizer()
    for t in nltk.word_tokenize(body):
        text = text + lemmatizer.lemmatize(t) + " "


    wjson = generatejson(ip, text.strip())
    Outfile.write(wjson)

'''
stemmer = SnowballStemmer("english")
lemmatizer = nltk.WordNetLemmatizer()
temp_sent = "Several women told me I have lying eyes."

print [stemmer.stem(t) for t in nltk.word_tokenize(temp_sent)]
print [lemmatizer.lemmatize(t) for t in nltk.word_tokenize(temp_sent)]
'''
