import nltk
import random 
from nltk.corpus import movie_reviews


documents = [(list(movie_reviews.words(fileid)),category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)
        ]

political_content = {}
political_content["true"] = [
    "Uganda Politician Bobiwine has been sentenced to 19 years in prison, for fraund",
    "Uganda Politician Bobiwine has been elected the president oof uganda in 2019",
    "President Museveni has  stepped aside to let bobiwine be the next president of Uganda",
    "President Museveni has been found guilty of fraud, he has been sentenced to jail 39 years in prison " 
]

political_content["false"] = [
    "Uganda Politician Bobiwine has been sentenced to 19 years in prison, for fraund",
    "Uganda Politician Bobiwine has been elected the president oof uganda in 2019",
    "President Museveni has  stepped aside to let bobiwine be the next president of Uganda",
    "President Museveni has been found guilty of fraud, he has been sentenced to jail 39 years in prison " 
]



random.shuffle(documents)


print(documents[0])