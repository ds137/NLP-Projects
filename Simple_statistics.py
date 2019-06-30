from nltk.book import FreqDist, text1
fdist1 = FreqDist(text1)#tells us frequency of each vocab item in the text
vocab1 = list(fdist1.keys()) #all distinct types in text
top_50 = vocab1 [: 50] #slice first 50 of most common types
print (top_50)
a = fdist1['man']
print (a)
