
sentence = input("Enter a sentence: ").lower()

if any(word in sentence for word in ["hello", "hi", "hey"]):
    print("Dialog Act: Greeting")

elif sentence.endswith("?"):
    print("Dialog Act: Question")

elif any(word in sentence for word in ["please", "kindly"]):
    print("Dialog Act: Request")

elif any(word in sentence for word in ["thank you", "thanks"]):
    print("Dialog Act: Thanking")

else:
    print("Dialog Act: Statement")
