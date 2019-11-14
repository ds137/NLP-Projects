from nltk.book import *
fdist1 = FreqDist(text1)#tells us frequency of each vocab item in the text
vocab1 = list(fdist1.keys()) #all distinct types in text and converts them into list
top_50 = vocab1 [: 50] #slice first 50 of most common types
print (top_50)
a = fdist1['man']
print (a)
V = set(text1)
long_words = [w for w in V if len(w) > 15] #the set of all words if word is an element of vocab and is greater than 15
sorted(long_words) #sorted alphabetically
print (long_words)


fdist1.hapaxes #unique words that only occur onece

fdist5 = FreqDist(text5) #this produces the most freq occuring content baring words
result_fdist = sorted([w for w in set(text5) if len(w) > 7 and fdist5[w] > 7]) #len(w) > 7 condition ensures that the word no longer than 7 letters
#fdist5[w] > 7 says that these words occur more than seven times.
print (result_fdist)

#collocations and bigrams
#bigrams are 2-grams collocations
bigrams = (['he' ,'said', 'bye' , 'as', 'he', 'walked' , 'through', 'the', 'door' ]
