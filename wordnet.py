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


w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")

w1 = wordnet.synset("car.n.01")
w2 = wordnet.synset("truck.n.01")


print("Similarity \n")
print(w1.wup_similarity(w2))
