import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import  LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC,NuSVC
from sklearn.ensemble import RandomForestClassifier
import json




from nltk.classify import ClassifierI
from statistics import mode


class VoteClassifier(ClassifierI):
    # List of classifiers passsed to this 
    def __init__(self,*classifiers):
        self._classifiers = classifiers
    def classify(self,features):
        votes = []
        for c  in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)
    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        choice_votes = votes.count(mode(votes))
        conf = choice_votes/len(votes)
        return conf
    def predict(self,text):
        pass




short_pos = open("positive.txt","r").read()
short_neg = open("negative.txt","r").read()


documents = []


posive_corpus = []
negative_corpus = []

for sentence in short_pos.split('\n'): 
    posive_corpus.append(sentence) 


for sentence in short_neg.split('\n'): 
    negative_corpus.append(sentence) 


# // add to the turple, postive and negative corpus and move  


# print(documents)
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(posive_corpus)

Y= vectorizer.fit_transform(negative_corpus)

documents.append(X)
documents.append(Y)


# # create a dictionary
# doc = {}
# doc[0] = X
# doc[1] = Y

# print("{}".format(doc))


from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(max_features=1500, min_df=5, max_df=0.7 )
X = vectorizer.fit_transform(posive_corpus)
Y = vectorizer.fit_transform(negative_corpus)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

print("{}".format(X_test))

# vectorizer2 = CountVectorizer(analyzer='word', ngram_range=(2, 2))
# X2 = vectorizer2.fit_transform(corpus)
# print(vectorizer.get_feature_names())



classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
classifier.fit(X_train, y_train) 


# from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print("Debugging {} ".format(classifier))


# for sentence in short_neg.split('\n'):
#     documents.append((sentence,"neg"))
#     # print("::::::::::::::::::::::::::::::::::::::::::::::::::: \n  {}".format(sentence))



# # //todo: if we have a document, can we then convert ==

# all_words = []
# # Word tokenizing is the art of breaking up a sentence into words list 
# # split a sentence into words 
# short_pos_words = nltk.word_tokenize(short_pos)
# short_neg_words = nltk.word_tokenize(short_neg)

# for w in short_pos_words:
#     all_words.append(w.lower())

# for w in short_neg_words:
#     all_words.append(w.lower())

# all_words = nltk.FreqDist(all_words)

# # Print all workds 
# print(all_words)


# # //I have all the words in all my sample data  
# word_features  = list(all_words.keys())[:5000]
# print(word_features)


# def find_features(document):
#     words = set(document)
#     features = {}
#     for w in word_features:
#         features[w] = (w in words)

#     return features


# featuresets = [(find_features(rev), category) for (rev, category) in documents]
# random.shuffle(featuresets)

# from sklearn.feature_extraction.text import CountVectorizer
# vectorizer = CountVectorizer(max_features=1500, min_df=5, max_df=0.7)
# # X = vectorizer.fit_transform(documents.lower())


# training_set = x[:1000]
# testing_set = x[1000:]


# BernoulliNB = SklearnClassifier(BernoulliNB())
# BernoulliNB.train(training_set)
# print("BernoulliNB Algo Accuracy: ",      (nltk.classify.accuracy(BernoulliNB, testing_set)) * 100)

 
# LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
# LogisticRegression_classifier.train(training_set)
# print("LogisticRegression Algo Accuracy: ",      (nltk.classify.accuracy(LogisticRegression_classifier, testing_set)) * 100)

# SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
# SGDClassifier_classifier.train(training_set)
# print("SGDClassifier Algo Accuracy: ",      (nltk.classify.accuracy(SGDClassifier_classifier, testing_set)) * 100)

# SVC_classifier = SklearnClassifier(SVC())
# SVC_classifier.train(training_set)
# print("SVC Algo Accuracy: ",      (nltk.classify.accuracy(SVC_classifier, testing_set)) * 100)

# LinearSVC_classifier = SklearnClassifier(LinearSVC())
# LinearSVC_classifier.train(training_set)
# print("LinearSVC Algo Accuracy: ",      (nltk.classify.accuracy(LinearSVC_classifier, testing_set)) * 100)

# NuSVC_classifier = SklearnClassifier(NuSVC())
# NuSVC_classifier.train(training_set)
# print("NuSVC Algo Accuracy: ",      (nltk.classify.accuracy(NuSVC_classifier, testing_set)) * 100)
 




# # short_pos_words = word
# # words = ""

# # all_words = []

# # # // [w.lower() for w in movie_reviews.words()]

# # x = []
# # for category in political_content.keys():

# #     for content in political_content[category]:
# #         documents.append((content.split(" "), category))
# #         x += content.split(" ")
# #     all_words = x

# # # word_features  = words.split(" ")


# # random.shuffle(documents)

# # all_words = nltk.FreqDist(all_words)

# # # Print all workds 
# # print(all_words)

# # word_features = list(all_words.keys())[:3000]


# # print("Word Features \n ")
# # print(set(word_features))


# def find_features(document):
#     words = set(document)
#     features = {}
#     for w in word_features:
#         features[w] = (w in words)

#     return features


# print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
# print("{}".format(documents))
# print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
 

# print("------- FEATURE SETS ::::: ------------------- ") 
# featuresets = [(find_features(rev), category) for (rev, category) in documents]

# print(featuresets)


# print("------- LENGTH ::::: ------------------- ")
# print(len(featuresets))
# training_set = featuresets[:14]
# testing_set = featuresets[0:14]

# print('----------------------Training Set---------------------------------  \n')
# print(training_set)


# # posterior = prioer occurences  * likelihood / evidence = [positive,negative]


# classifier = nltk.NaiveBayesClassifier.train(training_set)
# print("Original Naive Bayes Algo Accuracy: ",
#       (nltk.classify.accuracy(classifier, testing_set)) * 100)

# classifier.show_most_informative_features(50)

# MNB_Classifier = SklearnClassifier(MultinomialNB())
# MNB_Classifier.train(training_set)
# print("MNB_Classifier Algo Accuracy: ",
#       (nltk.classify.accuracy(MNB_Classifier, testing_set)) * 100)


# # GaussianNB = SklearnClassifier(GaussianNB())
# # GaussianNB.train(training_set)
# # print("GaussianNB Algo Accuracy: ",
# #       (nltk.classify.accuracy(GaussianNB, testing_set)) * 100)


# BernoulliNB = SklearnClassifier(BernoulliNB())
# BernoulliNB.train(training_set)
# print("BernoulliNB Algo Accuracy: ",      (nltk.classify.accuracy(BernoulliNB, testing_set)) * 100)

 
# LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
# LogisticRegression_classifier.train(training_set)
# print("LogisticRegression Algo Accuracy: ",      (nltk.classify.accuracy(LogisticRegression_classifier, testing_set)) * 100)

# SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
# SGDClassifier_classifier.train(training_set)
# print("SGDClassifier Algo Accuracy: ",      (nltk.classify.accuracy(SGDClassifier_classifier, testing_set)) * 100)

# SVC_classifier = SklearnClassifier(SVC())
# SVC_classifier.train(training_set)
# print("SVC Algo Accuracy: ",      (nltk.classify.accuracy(SVC_classifier, testing_set)) * 100)

# LinearSVC_classifier = SklearnClassifier(LinearSVC())
# LinearSVC_classifier.train(training_set)
# print("LinearSVC Algo Accuracy: ",      (nltk.classify.accuracy(LinearSVC_classifier, testing_set)) * 100)

# NuSVC_classifier = SklearnClassifier(NuSVC())
# NuSVC_classifier.train(training_set)
# print("NuSVC Algo Accuracy: ",      (nltk.classify.accuracy(NuSVC_classifier, testing_set)) * 100)
 

 
# print("---------------\n")

# voted_classifier = VoteClassifier(classifier,MNB_Classifier,BernoulliNB,LogisticRegression_classifier,SGDClassifier_classifier,SVC_classifier,NuSVC_classifier)
# print("Voted Classifier Algo Accuracy: ",      (nltk.classify.accuracy(voted_classifier, testing_set)) * 100)

# text_to_predict = "Museveni has been overthrown in Uganda "
# text_to_predict = text_to_predict.split(" ")
# # print("Classification : ",voted_classifier.classify(testing_set[0][0]))
# print("LAST FEATURES \n")
# print(testing_set[0][0])

# print("Classification : ",voted_classifier.classify(testing_set[0][0]))
