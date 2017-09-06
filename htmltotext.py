


import html2text
#import string


Infile = open("tidy")
Outfile = open("html2text",'w')

Instring = Infile.read()

h = html2text.HTML2Text()
h.ignore_links = True
#h.escape_all = True


out = h.handle(Instring).encode('ascii',errors='ignore')

#printtable = set(string.printable)
#filter(lambda x: x in printtable, out)


Outfile.write(out)

Outfile.close()
Infile.close()
