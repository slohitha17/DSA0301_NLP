
import nltk

sentence = input("Enter a sentence: ")

words = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(words)

nouns = []

for word, tag in tagged:
    if tag.startswith("NN"):
        nouns.append(word)

print("\nNouns in the sentence:")
print(nouns)

print("\nPronouns in the sentence:")
for word, tag in tagged:
    if tag == "PRP":
        print(word)

if nouns:
    print("\nPossible reference:", nouns[-1])
