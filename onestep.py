import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier

from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

import re
import string
import random
import json

from nltk.classify import ClassifierI
from statistics import mode

 
class VoteClassifier(ClassifierI):
    # List of classifiers passsed to this
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
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

    def predict(self, text):
        pass


def remove_noise(tweet_tokens, stop_words=()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', token)
        token = re.sub("(@[A-Za-z0-9_]+)", "", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens


def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token


def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)


if __name__ == "__main__":
    #   this is where the magic is begininig

    # data ={}
    with open('positive.json') as f:
        data = json.load(f)

    print(data['False'][0])

    positive_tweets = data['True']
    negative_tweets = data['False']

    positive_tweet_tokens = []
    negative_tweet_tokens = []

    for sentence in positive_tweets:
        # todo:  tockenize this then append
        positive_tweet_tokens.append(nltk.word_tokenize(sentence))

    for sentence in negative_tweets:
        # todo:  tockenize this then append
        negative_tweet_tokens.append(nltk.word_tokenize(sentence))

        # print("\n ------ \n {}".format(sentence))

    # todo : loop through the issues, and tokenize them

    # positive_tweets = twitter_samples.strings('positive_tweets.json')
    # negative_tweets = twitter_samples.strings('negative_tweets.json')
    # text = twitter_samples.strings('tweets.20150430-223406.json')

    # positive_tweet_tokens =  nltk.word_tokenize(positive_tweets)
    # negative_tweet_tokens =  nltk.word_tokenize(negative_tweets)

    # twitter_samples.tokenized('positive_tweets.json')[0]

    stop_words = stopwords.words('english')

    # positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
    # negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')

    positive_cleaned_tokens_list = []
    negative_cleaned_tokens_list = []

    for tokens in positive_tweet_tokens:
        positive_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    for tokens in negative_tweet_tokens:
        negative_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    all_pos_words = get_all_words(positive_cleaned_tokens_list)

    freq_dist_pos = FreqDist(all_pos_words)
    print(freq_dist_pos.most_common(10))

    positive_tokens_for_model = get_tweets_for_model(
        positive_cleaned_tokens_list)
    negative_tokens_for_model = get_tweets_for_model(
        negative_cleaned_tokens_list)

    positive_dataset = [(tweet_dict, "Positive")
                        for tweet_dict in positive_tokens_for_model]

    negative_dataset = [(tweet_dict, "Negative")
                        for tweet_dict in negative_tokens_for_model]

    dataset = positive_dataset + negative_dataset

    random.shuffle(dataset)

    print(len(dataset))

    train_data = dataset[:5]
    test_data = dataset[5:]



names = ["MultinomialNBclassifier", "BernoulliNB", "LogisticRegression_classifier", "SGDClassifier_classifier ",
         "SVC_classifier", "LinearSVC_classifier", "NaiveBayesClassifier"]


    classification  = [
        SklearnClassifier(MultinomialNB()),
        SklearnClassifier(BernoulliNB()),
        SklearnClassifier(LogisticRegression()),
        SklearnClassifier(SGDClassifier()),
        
        SklearnClassifier(LinearSVC()),
        SklearnClassifier(NuSVC(gamma='auto')),

        
        SklearnClassifier(NuSVC(gamma='auto')),
        SklearnClassifier(NuSVC(gamma='auto')),
        
        
        GaussianProcessClassifier(1.0 * RBF(1.0)),
        DecisionTreeClassifier(max_depth=5),
        RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
        MLPClassifier(alpha=1, max_iter=1000),
        AdaBoostClassifier(),
        GaussianNB(),
        QuadraticDiscriminantAnalysis()]



    MultinomialNBclassifier = SklearnClassifier(MultinomialNB())
    MultinomialNBclassifier.train(train_data)
    print("\nMultinomialNB Accuracy is:",
          (classify.accuracy(MultinomialNBclassifier, test_data)) * 100)

    # GaussianNBclassifier = SklearnClassifier(GaussianNB())
    # GaussianNBclassifier.train(train_data)
    # print("\nGaussianNB Accuracy is:", classify.accuracy(GaussianNBclassifier, test_data))

    BernoulliNB = SklearnClassifier(BernoulliNB())
    BernoulliNB.train(train_data)
    print("BernoulliNB Algo Accuracy: ",
          (nltk.classify.accuracy(BernoulliNB, test_data)) * 100)

    LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
    LogisticRegression_classifier.train(train_data)
    print("LogisticRegression Algo Accuracy: ",      (nltk.classify.accuracy(
        LogisticRegression_classifier, test_data)) * 100)

    SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
    SGDClassifier_classifier.train(train_data)
    print("SGDClassifier Algo Accuracy: ",
          (nltk.classify.accuracy(SGDClassifier_classifier, test_data)) * 100)

    SVC_classifier = SklearnClassifier(SVC())
    SVC_classifier.train(train_data)
    print("SVC Algo Accuracy: ",
          (nltk.classify.accuracy(SVC_classifier, test_data)) * 100)

    LinearSVC_classifier = SklearnClassifier(LinearSVC())
    LinearSVC_classifier.train(train_data)
    print("LinearSVC Algo Accuracy: ",
          (nltk.classify.accuracy(LinearSVC_classifier, test_data)) * 100)

    NuSVC_classifier = SklearnClassifier(NuSVC(gamma='auto'))

    NuSVC_classifier.train(train_data)
    print("NuSVC Algo Accuracy: ",
          (nltk.classify.accuracy(NuSVC_classifier, test_data)) * 100)

    classifier = NaiveBayesClassifier.train(train_data)

    print("Accuracy is:", classify.accuracy(classifier, test_data))

    print(classifier.show_most_informative_features(10))

    custom_tweet = " Bobiwine is contesting for presidency in 2021"

    custom_tokens = remove_noise(word_tokenize(custom_tweet))

    print(custom_tweet, classifier.classify(
        dict([token, True] for token in custom_tokens)))


voted_classifier = VoteClassifier(classifier, MultinomialNBclassifier, BernoulliNB,
                                  LogisticRegression_classifier, SGDClassifier_classifier, LinearSVC_classifier, NuSVC_classifier)

print("Voted Classifier Algo Accuracy: ",
      (nltk.classify.accuracy(voted_classifier, test_data)) * 100)
