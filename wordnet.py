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


synonyms = []
antonyms = []

for syn  in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())


print("Synonms \n")
print(set(synonyms))

print("\n Antonyns  \n")
print(set(antonyms))