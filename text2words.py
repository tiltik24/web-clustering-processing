# -*- coding: utf-8 -*-

import nltk
from nltk import word_tokenize,sent_tokenize
import string
#import re
from itertools import chain

from nltk.corpus import stopwords

from nltk.stem import WordNetLemmatizer






Infile = open("html2text")
Outfile = open("text2words",'w')

#string = Infile.read().encode("utf-8")
Instring = Infile.read()

# print Instring
# remove = string.punctuation
# remove = remove.replace(",", "")
# remove = remove.replace(".", "")
# pattern = r"[{}]".format(remove)
#re.sub(pattern, "", Instring)

# import regex as re
#re.sub(ur"\p{P}+", "", Instring)

Instring = Instring.strip(string.punctuation)

# print Instring

sentences = nltk.sent_tokenize(Instring)

words = []
for sentence in sentences:
    words.append(nltk.word_tokenize(sentence))

# print words



newwords = []
newwords = list(chain(*words))
# print newwords

# newwords1 = []
# for word in newwords:
#     newwords1.extend(word.strip(string.punctuation))
#newwords = newwords.strip(string.punctuation)

delEStr = string.punctuation + ' ' + string.digits
joinwords = [''.join(c for c in s if c not in delEStr) for s in newwords]

print joinwords


finalwords = []

for s in joinwords:
    if len(s) > 2:
        finalwords.append(s.lower())
    else:
        continue

print finalwords
# for s in joinwords:
#     if len(s) < 3:
#         joinwords.remove(s)
#     else:
#         continue

list_stopWords=list(set(stopwords.words('english')))
filtered_words=[w for w in finalwords if not w in list_stopWords]


print filtered_words

lemmatiser = WordNetLemmatizer()

lemwords = []
for w in filtered_words:
    lemwords.append(lemmatiser.lemmatize(w))

# joinwords.remove('')

print lemwords






#words = [''.join(c for c in s if c not in string.punctuation) for s in words]
#print words
#punct =set(string.punctuation)
#filterpuntl = lambda words: list(filter(lambda x: x not in punct, words))
#filterpunt = lambda words: ''.join(filter(lambda x: x not in punct, words))
#m = words.translate(None, string.punctuation)
#words = [s for s in words if s]
#print words


#print filterpunt
#Outfile.write(words)
#print sentences


Outfile.close()
Infile.close()



#Install nltk
# run sudo pip install -U nltk

# Do this in a separate python interpreter session, since you only have to do it once
#import nltk
#nltk.download('punkt')

#nltk.download('stopwords')

# Do this in your ipython notebook or analysis script
#from nltk.tokenize import word_tokenize

#sentences = [
#    "Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.",
#    "Professor Plum has a green plant in his study.",
#    "Miss Scarlett watered Professor Plum's green plant while he was away from his office last week."
#]

#sentences_tokenized = []
#for s in sentences:
#    sentences_tokenized.append(word_tokenize(s))

#sentences_tokenized is a list of a list of tokens:

#[['Mr.', 'Green', 'killed', 'Colonel', 'Mustard', 'in', 'the', 'study', 'with', 'the', 'candlestick', '.', 'Mr.', 'Green', 'is', 'not', 'a', 'very', 'nice', 'fellow', '.'],
#['Professor', 'Plum', 'has', 'a', 'green', 'plant', 'in', 'his', 'study', '.'],
#['Miss', 'Scarlett', 'watered', 'Professor', 'Plum', "'s", 'green', 'plant', 'while', 'he', 'was', 'away', 'from', 'his', 'office', 'last', 'week', '.']]




#punct = set(u''':!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒
#﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠
#々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻
#︽︿﹁﹃﹙﹛﹝（｛“‘-—_…''')
# 对str/unicode
#filterpunt = lambda s: ''.join(filter(lambda x: x not in punct, s))
# 对list
#filterpuntl = lambda l: list(filter(lambda x: x not in punct, l))
