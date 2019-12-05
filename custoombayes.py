import nltk
import random 
from nltk.corpus import movie_reviews


# documents = [(list(movie_reviews.words(fileid)),category)
#              for category in movie_reviews.categories()
#              for fileid in movie_reviews.fileids(category)
#         ]


political_content = {}
political_content["false"] = [
    "Uganda Politician Bobiwine has been sentenced to 19 years in prison, for fraund ",
    "Uganda Politician Bobiwine has been elected the president oof uganda in 2019 ",
    "President Museveni has  stepped aside to let bobiwine be the next president of Uganda ",
    "President Museveni has been found guilty of fraud, he has been sentenced to jail 39 years in prison " 
]

political_content["true"] = [
    "Uganda  president Museveni is going to stand for the 2021 elections ",
    "Uganda  politician bobiwine intends to stand for presidenet in 2021 ",
    "Uganda president museveni has launched a campain against corruption "  
]



# print(political_content)
word_features = []   
words = "" 

for category in political_content.keys():
    for content in  political_content[category]:
        words +=   content.lower()

word_features  = words.split(" ")

print(word_features)

def find_features(document):
    words = set(document)
    features =  {}
    for w in word_features:
        features[w] = (w in words)

    return features


# contentx = "Uganda  president Museveni is going to stand for the 2021 elections "
contentx = "Uganda Politician Bobiwine has been elected the president oof uganda in 2019 "
# print((find_features(movie_reviews.words("neg/cv000_29416.txt"))))s
print((find_features(contentx.lower())))
 