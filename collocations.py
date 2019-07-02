from nltk.book import*

print (text4.collocations)
print ([len(w) for w in text4]) #gets list of the lengths of words in text
fdist = FreqDist([len(w) for w in text4]) #the freqDist then counts the number of times each of these occur
print (fdist)

print (fdist.items()) 
print (fdist.max()) 
print (fdist[3]) #words of length 3 account for 50,000 of all in text  
print (fdist.freq(3))#  most freq word length 0.19255882431878046