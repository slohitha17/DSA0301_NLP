
from nltk.stem import WordNetLemmatizer

l = WordNetLemmatizer()

word = input("Enter a word: ").lower()

print("Original word:", word)
print("Root word:", l.lemmatize(word, "v"))
