
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

sentence = input("Enter a sentence: ")
word = input("Enter ambiguous word: ")

meaning = lesk(word_tokenize(sentence), word)

if meaning:
    print("Meaning:", meaning.definition())
else:
    print("Meaning not found")
