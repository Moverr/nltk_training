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
documents = []   
words = "" 

for category in political_content.keys():
    for content in  political_content[category]:
        words +=   content

documents  = words.split(" ")

print(documents)

# documents.append(words.split(" "))


# print(documents)
# (list(movie_reviews.words(fileid)),category)
#              for category in movie_reviews.categories()
#              for fileid in movie_reviews.fileids(category)
    


# random.shuffle(documents)


# print(documents[0])