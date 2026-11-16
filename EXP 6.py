
import random

text = "I love NLP and I love Python"
words = text.split()

bigrams = {}

for i in range(len(words)-1):
    bigrams.setdefault(words[i], []).append(words[i+1])

word = "I"
result = [word]

for i in range(5):
    if word not in bigrams:
        break
    word = random.choice(bigrams[word])
    result.append(word)

print("Generated text:", " ".join(result))
