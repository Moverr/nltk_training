# Text Classification  
import nltk
import random

from nltk.corpus import movie_reviews
from  nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



# print(movie_reviews())

documents = [(list(movie_reviews.words(fileid)),category)  
            for category in movie_reviews.categories() 
            for fileid in movie_reviews.fileids(category)]


random.shuffle(documents)
# print(documents[1])

stop_words = set(stopwords.words("english"))



all_words = []
for w in movie_reviews.words():
    if w not in stop_words:
        all_words.append(w.lower())

all_words  = nltk.FreqDist(all_words)
print(all_words.most_common(15))


print (all_words["stupid"])