import nltk
import random 
from nltk.corpus import movie_reviews


documents = [(list(movie_reviews.words(fileid)),category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)
        ]

random.shuffle(documents)

print(documents[1])

# return


# all_words = [w.lower() for w in movie_reviews.words()]

# # for w in movie_reviews.words():
# #     all_words.append(w.lower())git b

# all_words = nltk.FreqDist(all_words)

# # print("All WOrds \n ")
# # print(all_words)

# word_features = list(all_words.keys())[:3000]

# print(word_features)

# print("Word Features \n ")
# print(set(word_features))

# def find_features(document):
#     words = set(document)
#     features =  {}
#     for w in word_features:
#         features[w] = (w in words)

#     return features


# # print((find_features(movie_reviews.words("neg/cv000_29416.txt"))))



# # Every word can have different datasets :: 
# '''
# // we intend to have a set of words against a forest of words. but if we find a percentage of those words in the forest of words. 
# then we can categorize this as a pass or a fail, depending on ML ..  level of tolerance in a text. 
# this will depend on the % accuracy of the classifier in this game :: 
# '''
# #  Labeled dataset 
# featuresets = [(find_features(rev),category) for (rev,category) in documents ]

# # print(featuresets)

# training_set  =featuresets[:10]
# testing_set = featuresets[1900:]

# print("Training Set \n")
# print(training_set)

# #posterior = prioer occurences  * likelihood / evidence = [positive,negative]

# # classifier = nltk.NaiveBayesClassifier.train(training_set)
# # print("Naive Bayes Algo Accuracy: ",(nltk.classify.accuracy(classifier,testing_set))* 100 )

 
