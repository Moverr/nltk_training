import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
# Un supervised machine learning tokenizer , it comes supervised but you can re-train it for other scneanrois

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

print(sample_text)