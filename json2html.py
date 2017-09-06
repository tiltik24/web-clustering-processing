import json
import nltk

Infile = open("base64.json")
Outfile = open("base64.html",'w')

Instring = Infile.read()




hjson = json.loads(Instring)

# strJson = "".join([ hjson.strip().rsplit("}" , 1)[0] ,  "}"] )

out = hjson['body'].encode("utf-8")


# out = nltk.clean_html(out1)

print out




#print out
Outfile.write(out)

Outfile.close()
Infile.close()
