
words = input("Enter a sentence: ").split()

tags = {
    "I": "PRP",
    "play": "VBP",
    "cricket": "NN",
    "eat": "VBP",
    "apple": "NN"
}

for word in words:
    print(word, ":", tags.get(word, "NN"))
