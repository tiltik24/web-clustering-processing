from tidylib import tidy_document


Infile = open("json2html.html")
Outfile = open("tidy",'w')

string = Infile.read()

document, errors = tidy_document(string)

Outfile.write(document)

print document
print errors
