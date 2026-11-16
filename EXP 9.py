
from nltk.tag import RegexpTagger

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*ly$', 'RB'),
    (r'.*', 'NN')
]

tagger = RegexpTagger(patterns)

words = input("Enter words: ").split()

print("POS Tags:", tagger.tag(words))
