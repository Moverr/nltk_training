# Text Classification
import nltk
import random

from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# print(movie_reviews())


documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

documents = []

categories = []


for category in movie_reviews.categories():
    categories.append(category)
    for fileid in movie_reviews.fileids(category):
        # x = list(movie_reviews.words(fileid)),category
        x = list(movie_reviews.words(fileid)), category
        documents.append(x)


random.shuffle(documents)

print("Categories \n")
# print(documents)

print("::::::::::::::::::::::::::::::::::::::::::::::::\n")
# print(documents[:1])


all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

# print(all_words.keys())

word_features = list(all_words.keys())[:3000]

wordss = ['many', '*', 'friends', ',', 'family', 'members', ',', 'and', 'acquaintances', 'whose', 'lives', 'were', 'touched', 'by', 'this', 'young', 'woman', 'and', 'her', 'writings', '.', 'winner', 'of', 'the', 'last', 'year', "'", 's', 'academy', 'award', 'for', 'best', 'documentary', 'i', 'relish', 'those', 'rare', 'opportunities', 'when', 'a', 'talented', 'screenwriter', 'can', 'make', 'me', 'feel', 'like', 'a', 'fool', '.', 'i', 'spent', 'the', 'first', 'hour', 'of', 'forces', 'of', 'nature', 'slowly', 'stewing', 'over', 'its', 'grim', 'attitude', 'towards', 'marriage', ',', 'grousing', 'to', 'myself', 'about', 'its', 'transparently', 'planes', ',', 'trains']


def find_features(document):
    words = set(wordss)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features


print("Pass and Go \n")
print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

# print("\n PASS \n ")
# featuresets = [(find_features(rev),category) for (rev,category) in documents ]
# print(featuresets)
