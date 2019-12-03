from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("mountains"))



print(lemmatizer.lemmatize("better",pos='a'))

print(lemmatizer.lemmatize("best",pos='a'))
print(lemmatizer.lemmatize("run",pos='v'))
print(lemmatizer.lemmatize("run",pos='v'))


# Lametizing is more powerful than stemming

