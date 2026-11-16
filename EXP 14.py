
import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> 'He'
VP -> 'plays'
VP -> 'play'
""")

parser = nltk.ChartParser(grammar)

sentence = input("Enter sentence: ").split()

if list(parser.parse(sentence)):
    print("Sentence is valid")
else:
    print("Sentence is invalid")
