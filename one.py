import nltk
from  nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing off stop word filtration."
stop_words = set(stopwords.words("english"))
# stop_words = set(stopwords.words("greek"))

print("stop Words \n {} ".format(stop_words))

words = word_tokenize(example_sentence)

filtered_sentence = []
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
    

print("Filtered Words \n {}".format(filtered_sentence))