import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import  LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC,NuSVC
import json


with open('data.txt') as json_file:
    data = json.load(json_file)
 
political_content = {}
political_content["false"] = [
    "Popular singer and Ugandan presidential challenger Bobi Wine (Robert Kyagulanyi) this week spoke out in defense of LGBT rights, an issue that divides Ugandan voters. JOHANNESBURG, South Africa – Kyadondo East Member of Parliament Robert Kyagulanyi alias Bobi Wine’s remarks about homosexuals has drawn mixed views from Ugandans on social media0."
    + "While appearing on South African Broadcast Corporation (SABC) on Wednesday, Bobi Wine said whereas he does not agree with homosexuals, he respects their rights."
    + "“I believe that one has the responsibility of guarding the rights of all citizens of those who are like you and those that are not like you. I believe that as a leader, a high level of tolerance is required to make sure the nation comes together,” Bobi Wine said."
    + "He is in South Africa for the Freedom Foundation Africa’s ‘Africa Freedom Award ceremony 2019’ due on Friday, December 6.",
    "Ugandan artist Bobi Wine writes songs with blatant homophobic lyrics and calls for gay people to be attacked, or killed."
    + "The UK 2008, Criminal Justice and Immigration Act, makes a new criminal offence of ‘incitement to homophobic hatred. We strongly believe that allowing an act to perform that includes such lyrics as: 'Fire will burn the batty man. Burn all the batty man. All Ugandans get behind me and fight the batty man’ is incitement to homophobic hate and therefore in breach of the 2008 Act and should not be allowed to go ahead."
    + "Allowing such an artist to appear in public is clearly going to raise tensions and we'd respectfully request that his appearance within the UK is cancelled immediately."
    + "In Uganda LGBT rights have been taken away with the introduction of the Uganda Anti-Homosexuality Act, 2014. The UK prides itself on tolerance and understanding but allowing someone to perform hate songs which incite violence is unacceptable.",
    "Just before Wasswa’s murder, a government official linked Uganda’s LGBTQ community to a “terrorist” group. However, that group is a political movement run by one of the authoritarian president’s political rivals, a parliamentarian and singer named Bobi Wine, who has expressed lukewarm support for LGBTQ Ugandans and is expected to run for president in the country’s 2021 elections. Museveni has been president since 1986.",
    "President Museveni has been found guilty of fraud, he has been sentenced to jail 39 years in prison "
]

political_content["true"] = [
    "Bobi Wine, Uganda's pop star-turned-opposition leader, said on Monday he will challenge longtime President Yoweri Museveni in elections set for 2021."
    + "\"I will challenge President Museveni on behalf of the people,' he said in an interview with The Associated Press.\""
    + "But Wine, whose real name is Kyagulanyi Ssentamu, said he was concerned about his safety after surviving what he believes was an attempt on his life last August when his driver was shot dead in his car following an incident in which protesters threw stones at the president's motorcade.",
    "Uganda  politician bobiwine intends to stand for presidenet in 2021 ",

    " The popular musician-turned-parliamentarian was attending a rally for Kassiano Wadri for the Arua by-election in northen Uganda."
    + "Bobi Wine says, government forces ambushed, arrested and tortured him. On his Facebook page, Bobi later shared his ordeal."
    + "“The marks on my back, ankles, elbows, legs and head are still visible. I continued to groan in pain and the last I heard was someone hit me at the back of the head with an object — I think a gun butt or something,” Bobi wrote. “That was the last time I knew what was going on.”"
    + "Bobi's driver, Yasin Kawuma, was fatally shot dead during the violence that day. Bobi, a vocal critic of President Yoweri Museveni, is certain security forces knew where he’d be and meticulously planned their attack."
    + "Reporting by The Wall Street Journal this summer confirms his claims and shows that Ugandan intelligence officials, with the help of employees of Chinese tech giant Huawei, hacked into Bobi’s WhatsApp and Skype accounts to monitor the dissident and his supporters."
    + "In an interview Wednesday, Bobi told VOA he’s now adopted a sophisticated routine to throw government spies off his trail using burner phones and old-fashioned code words."
    + "“What I’ve been doing to protect myself and the people that I communicate with is, one, to use coded language when I’m talking on the phone that is known,” he told VOA."
    + "“I’ve been forced to devise means of changing telephone numbers and telephone headsets constantly to keep them on the wrong track,” Bobi added."
    + "“And sometimes, when I have to move to a place and I don’t want to be followed by the regime, I’m forced to leave my phone behind or put my phone in a car that is going in a different region of the country while I’m going into another one. That alone is how I’m trying to maneuver to go around it.”"
    + "Denials"
    + "Huawei, who helped build a large portion of Africa’s cellular backbone, has also been implicated in allegations of spying on African diplomacy on behalf of the Chinese government."
    + "But Ren Zhengfei, the founder of Huawei, firmly denies spying claims and says his company refuses to give up confidential information of clients and “would definitely say ‘no’ to such a request,” in a rare press conference at the company’s headquarters in January."
    + "In a recent interview with VOA, Zambian President Edgar Lungu also addressed the question of spying on dissidents and opposition parties in the country. "
    + "“There was this story that Huawei, the Chinese company, that I am spying on opposition party leaders, their phones and so on,” he said, describing what he thinks is a spread of misinformation."
    + "He further explained that these claims are detrimental to the country’s image and foreign policy. "
    + "“I think that we need to do more … so that the truth is given to the people, so that we are not demonized over fake news stories,” he said."
    + "They were tracking me’"
    + "Bobi says his first-hand experiences reveal the scope and sophistication of government-backed spying."
    + "Among the things I got to learn was that they were listening to my calls and having a copy of all that was WhatsApp chats and many other things, following my location every time,” he said."
    + "1I even learned that day when I was arrested and brutalized in Arua, it was because of that technology that they got that they could listen to my phones, and they were tracking me. And they know that they follow me on my phone and they know where I am and listening to my calls.”"
    + "The government’s paranoia won’t stop, Bobi suggested, as long as they perceive him as a threat. And he has no plans to back down. Wadri, the candidate Wine campaigned for in 2018, won his seat in parliament."
    + "Now Bobi is gearing up for a new kind of campaigning, after announcing this summer his intention to run for president in Uganda’s 2021 polls.",
    "President Museveni has  stepped aside to let bobiwine be the next president of Uganda ",
    "President Museveni has been found guilty of fraud, he has been sentenced to jail 39 years in prison "
]


# print(political_content)
documents = []
words = ""

all_words = []
# // [w.lower() for w in movie_reviews.words()]

x = []
for category in political_content.keys():

    for content in political_content[category]:
        documents.append((content.split(" "), category))
        x += content.split(" ")
    all_words = x

# word_features  = words.split(" ")


random.shuffle(documents)

all_words = nltk.FreqDist(all_words)

# Print all workds 
print(all_words)

word_features = list(all_words.keys())[:3000]


print("Word Features \n ")
print(set(word_features))


def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


 
featuresets = [(find_features(rev), category) for (rev, category) in documents]
print(featuresets)


training_set = featuresets[:14]
testing_set = featuresets[0:]

print('----------------------Training Set---------------------------------  \n')
print(training_set)


# posterior = prioer occurences  * likelihood / evidence = [positive,negative]


classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Naive Bayes Algo Accuracy: ",
      (nltk.classify.accuracy(classifier, testing_set)) * 100)

classifier.show_most_informative_features(50)

MNB_Classifier = SklearnClassifier(MultinomialNB())
MNB_Classifier.train(training_set)
print("MNB_Classifier Algo Accuracy: ",
      (nltk.classify.accuracy(MNB_Classifier, testing_set)) * 100)


# GaussianNB = SklearnClassifier(GaussianNB())
# GaussianNB.train(training_set)
# print("GaussianNB Algo Accuracy: ",
#       (nltk.classify.accuracy(GaussianNB, testing_set)) * 100)


BernoulliNB = SklearnClassifier(BernoulliNB())
BernoulliNB.train(training_set)
print("BernoulliNB Algo Accuracy: ",      (nltk.classify.accuracy(BernoulliNB, testing_set)) * 100)

 
LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression Algo Accuracy: ",      (nltk.classify.accuracy(LogisticRegression_classifier, testing_set)) * 100)

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier Algo Accuracy: ",      (nltk.classify.accuracy(SGDClassifier_classifier, testing_set)) * 100)

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("SVC Algo Accuracy: ",      (nltk.classify.accuracy(SVC_classifier, testing_set)) * 100)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC Algo Accuracy: ",      (nltk.classify.accuracy(LinearSVC_classifier, testing_set)) * 100)

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC Algo Accuracy: ",      (nltk.classify.accuracy(NuSVC_classifier, testing_set)) * 100)
 

 
print("---------------\n")


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


voted_classifier = VoteClassifier(classifier,MNB_Classifier,BernoulliNB,LogisticRegression_classifier,SGDClassifier_classifier,SVC_classifier,NuSVC_classifier)
print("Voted Classifier Algo Accuracy: ",      (nltk.classify.accuracy(voted_classifier, testing_set)) * 100)

print("Classification : ",voted_classifier.classify(testing_set[0][0]))
