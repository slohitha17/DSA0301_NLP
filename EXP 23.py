
text = input("Enter a paragraph: ")

sentences = text.split(".")

connectors = ["however", "therefore", "because", "moreover",
              "furthermore", "firstly", "finally", "then"]

print("\nSentences:")
for sentence in sentences:
    if sentence.strip():
        print(sentence.strip())

print("\nConnecting words:")
for word in connectors:
    if word in text.lower():
        print(word)

if len(sentences) > 2:
    print("\nText contains multiple connected sentences.")
else:
    print("\nText contains fewer sentences.")
