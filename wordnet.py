from nltk.corpus import wordnet

syns = wordnet.synsets("program")
print(syns)

# synset 
print(syns[0].name)
# Just the word 
print(syns[0].lemmas()[0].name())

# Definition 
print(syns[0].definition())

# Examples 
print(syns[0].examples())
