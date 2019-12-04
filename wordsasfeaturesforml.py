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

documents = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        # x = list(movie_reviews.words(fileid)),category
        x = list(movie_reviews.words(fileid)),category
        documents.append(x) 



random.shuffle(documents)

print("::::::::::::::::::::::::::::::::::::::::::::::::\n")
print(documents[:1])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words  = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]



def find_features(document):
    words = set(document)
    features  ={}
    for w in word_features:
        features[w] = (w in words)
    return features


# print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

print("\n PASS \n ")
# featuresets = [(find_features(rev),category) for (rev,category) in documents ]
# print(featuresets)

 