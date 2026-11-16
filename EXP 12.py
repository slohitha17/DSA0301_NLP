
import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> 'The' 'boy'
VP -> 'plays' 'cricket'
""")

parser = nltk.EarleyChartParser(grammar)

sentence = input("Enter sentence: ").split()

for tree in parser.parse(sentence):
    print(tree)
