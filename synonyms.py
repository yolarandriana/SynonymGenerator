from nltk.corpus import wordnet

synonyms = []

word = input("Start typing ").lower()
synonyms.append(word)

for syn in wordnet.synsets(word):
    for i in syn.lemmas():
        if i.name() not in synonyms:
            synonyms.append(i.name())

print(synonyms)
