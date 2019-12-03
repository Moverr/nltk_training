# Text Classification  
import nltk
import random

from nltk.corpus import movie_reviews

# print(movie_reviews())

documents = []
for category  in movie_reviews.categories():
    