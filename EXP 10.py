
words = input("Enter a sentence: ").split()

for word in words:
    if word == "I":
        tag = "PRP"
    elif word == "am":
        tag = "VBP"
    elif word.endswith("ing"):
        tag = "VBG"
    else:
        tag = "NN"

    print(word, ":", tag)
