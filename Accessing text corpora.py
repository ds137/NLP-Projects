###Shorthand for accessing lexical data and texts####
from nltk.corpus import gutenberg
gutenberg.fileids()
macbeth = gutenberg.words('shakespeare-hamlet.txt'

#practicing for loops - averaging out results for each book
for fileid in gutenberg.fileids():
	num_chars = len(gutenberg.raw(fileid)) #this counts space charcters as letters, too
	num_words = len(gutenberg.words(fileid))
	num_sents = len(gutenberg.sents(fileid))
	num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))  # lower case words
	print(round(num_chars/num_words), round(num_words/num_sents),round(num_words/num_vocab),fileid)

macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt') #sents() function divides the etxt into sentances - each sentance is a list of words
print (macbeth_sentences)

print (macbeth_sentences[1116])

longest_len = max(len(s) for s in macbeth_sentences)  # gets longest sentance


from nltk.corpus import webtext ## ana ezMPLW  more casusal language sets
for fileid in webtext.fileids():
	print(fileid, webtext.raw(fileid)[:65], '...')

from nltk.corpus import nps_chat # instant messaging ... bit awk
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
chatroom[123]

from nltk.corpus import brown
print (brown.categories)


from nltk.corpus import brown
print (brown.categories())  #displays categories

print(brown.words(categories='news'))

print (brown.words(fileids=['cg23'])) #accessing specific doccuments

print (brown.sents(categories =['news' , 'editorial', 'reviews']) # different categories


import nltk
from nltk.corpus import brown
fiction_text = brown.words(categories='fiction') #to easily access fiction
>>> fdist = nltk.FreqDist(w.lower() for w in fiction_text)
>>> qwords = ['what', 'when' , 'where', 'who' , 'why']
>>> for i in qwords:
	print(i + ':', fdist[i], end= ' ' ) # making a list of how many occur in this cat, plus end = ' ' , makes it primt all on one line 
