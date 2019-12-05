import nltk
import random 
from nltk.corpus import movie_reviews


documents = [(list(movie_reviews.words(fileid)),category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)
        ]

random.shuffle(documents)

print(documents[1])


all_words = [w.lower() for w in movie_reviews.words()]

# for w in movie_reviews.words():
#     all_words.append(w.lower())


print("All WOrds \n ")
print(all_words[:200])