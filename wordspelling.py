import re
import string
import json
import enchant
from enchant.checker import SpellChecker

Infile = open("all-lan.json",'r')
Outfile = open("all-lan2check.json",'w')

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

# newwords = []

for line in open("all-lan.json"):
        # read a line from file
    line = Infile.readline()

        # extract json format, and get related elements
    hjson = json.loads(line)
    ip = hjson['ip']
    body = hjson['text']


    # chkr = SpellChecker("en_US")

    # pwl = enchant.request_pwl_dict("mywords.txt")
    # d2 = enchant.DictWithPWL("en_US","mywords.txt")

    d2 = enchant.DictWithPWL("en_US","mywords.txt")
    chkr = SpellChecker(d2)

    chkr.set_text(body)
    for err in chkr:
        # newwords.append(err.word)
        body = body.replace(err.word, "")

    body = re.sub(' +', ' ', body)
    body = body.strip()

    if len(body) < 3:
        continue
    else:
        wjson = generatejson(ip, body)
        Outfile.write(wjson)
        Outfile.flush()

Outfile.close()
Infile.close()



'''
dictt = {}
for tmp in newwords:
     if tmp in dictt:
         dictt[tmp] += 1
     else:
         dictt[tmp] = 1

errwords = []
errwords = sorted(dictt.items(), key=lambda e:e[1], reverse=True)
# errwords = sorted(dictt.keys())
strs = ""

for s in errwords:
    strs = strs + s[0] + "\n"
# s = repr(errwords)
f = file('dict.txt','w')
f.writelines(strs)
f.close()
'''
