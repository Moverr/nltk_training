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
    "Uganda president museveni has launched a campain against corruption " ,
      "President Museveni has  stepped aside to let bobiwine be the next president of Uganda ",
    "President Museveni has been found guilty of fraud, he has been sentenced to jail 39 years in prison "  
]



# print(political_content)
documents = []   
words = "" 

all_words =[]
# // [w.lower() for w in movie_reviews.words()]

x = []
for category in political_content.keys():
    
    for content in  political_content[category]:
        documents.append((content.split(" "),category))
        x += content.split(" ") 
    all_words = x

# word_features  = words.split(" ")


random.shuffle(documents)

all_words = nltk.FreqDist(all_words)


print(all_words)

word_features = list(all_words.keys())[:3000]


print("Word Features \n ")
print(set(word_features))

def find_features(document):
    words = set(document)
    features =  {}
    for w in word_features:
        features[w] = (w in words)

    return features


# print((find_features(movie_reviews.words("neg/cv000_29416.txt"))))

featuresets = [(find_features(rev),category) for (rev,category) in documents ]

print(featuresets)



training_set  =featuresets[0:6]
testing_set = featuresets[6:35]



#posterior = prioer occurences  * likelihood / evidence = [positive,negative]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Naive Bayes Algo Accuracy: ",(nltk.classify.accuracy(classifier,testing_set))* 100 )

classifier.show_most_informative_features(15)
# print("---------------\n")
# print("---------------\n")

# print(training_set)


print("---------------\n")









# def find_features(document):
#     words = set(document)
#     features =  {}
#     for w in word_features:
#         features[w] = (w in words)

#     return features


# # contentx = "Uganda  president Museveni is going to stand for the 2021 elections "
# contentx = "Uganda Politician Bobiwine has been elected the president oof uganda in 2019 "
# # print((find_features(movie_reviews.words("neg/cv000_29416.txt"))))s
# # print((find_features(contentx.lower())))
 
# featuresets = [(find_features(rev)) for (rev) in political_content ]

# training_set  =featuresets[:30]
# testing_set = featuresets[30:]


# print(training_set)
# # classifier = nltk.NaiveBayesClassifier.train(training_set)
# # print("Naive Bayes Algo Accuracy: ",(nltk.classify.accuracy(classifier,testing_set))* 100 )


# # print(featuresets)
