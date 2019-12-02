# analyzing pre-processing is 90% on the data 
# stemming relates abit with normaliation

# example:
# I was taking a ride in the car 
# I was riding in the car 

# Why Stemming is needed
# Alot of the time you have different vairations form the words 
# that require stemming 

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
example_words = ["python","pythoner","pythoning","pythoned"]

# example_words = ["big","biger","bigest"]
# big bigger biggest


for w in example_words:
    print(ps.stem(w))

new_text = "It is very important to be pythonly while you are  pythoning with python. All pythoners have pythoned poorly at least once. "

words = word_tokenize(new_text)


for w in words:
    print(ps.stem(w))
