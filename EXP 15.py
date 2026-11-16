
import nltk

grammar = nltk.PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'The' 'boy' [1.0]
VP -> 'plays' 'cricket' [1.0]
""")

parser = nltk.ViterbiParser(grammar)

sentence = input("Enter sentence: ").split()

for tree in parser.parse(sentence):
    print(tree)
    print("Probability:", tree.prob())
