#testing common conditions for 'tests' of true and false




from nltk.book import *
print (sent7) #finds first sentance of text 7 -wall street journal
print ([w for w in sent7 if len(w) == 4]) # if it's equal to 4
print ([w for w in sent7 if len(w) != 4 ]) #is not equal to 4

#some examples for word comparison operators
print (sorted([w for w in set(text1) if w.endswith('ableness')])) #also sorts alphabetical
print (sorted([term for term in set(text2) if 'cle' in term or 'cel' in term])) # words containing gnt
print (sorted([wd for wd in set(text4) if wd.istitle() and len(item) is > 7()]))# words having initial capital and is more than 7 letters long
print (sorted([item for item in set(text3) if item.islower()]))#lowercase
print (sorted([i for i in set(text6) if i.isdigit()])) # words made of digits


# an if statement is called a control structure, because, it contorls whether the code in the indented block will run
#another control structure is the for loop

sent1 = ['Call', 'me' , 'Ishmael', '.']

for token in sent1:
    if token.islower():
        print (token, 'is a lowercase word')
    elif token.istitle():
        print (token, 'is a title')
    else:
             print (token, 'is punctutation')

# demonstrates more conditions and functions
