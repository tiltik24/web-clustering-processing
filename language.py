# -*- coding:utf-8 -*-
import json
import langid



def translate(inputFile, outputFile):
    fin = open(inputFile, 'r')
    fout = open(outputFile, 'w')

    for eachLine in fin:

        hjson = json.loads(eachLine)
        # status = hjson['status']
        ip = hjson['ip']
        text = hjson['text']

        line = text.strip().decode('utf-8', 'ignore')
        lineTuple = langid.classify(line)                    
        if lineTuple[0] == "en": 
            outstr = eachLine
            fout.write(outstr.strip().encode('utf-8') + '\n')
	    fout.flush()
        else:
            continue

    fin.close()
    fout.close()

if __name__ == '__main__':
    # wc -l all.json
    # 8739493
    # totallinenum = len(open("all.json").readlines())
    totallinenum = 8739493
    print totallinenum

    translate("all.json", "all-lan.json")
    print "It's OK!"
