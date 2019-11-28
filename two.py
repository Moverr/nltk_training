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
    

#  stop words are words that do not matter in data analysis in our ML 

print("Filtered Words \n {}".format(filtered_sentence))

print("\n ONe line Exploaration fo r the loop")

# filtered_sentence = [w for w in words if not w in stop_words ]