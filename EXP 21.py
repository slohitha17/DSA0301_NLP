
import nltk

sentence = input("Enter a sentence: ")

words = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(words)

grammar = "NP: {<DT>?<JJ>*<NN.*>+}"
parser = nltk.RegexpParser(grammar)

result = parser.parse(tagged)

print("\nNoun Phrases:")
for subtree in result.subtrees():
    if subtree.label() == "NP":
        print(" ".join(word for word, tag in subtree.leaves()))
