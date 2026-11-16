
word = input("Enter a singular noun: ")

if word.endswith(("s", "sh", "ch", "x", "z")):
    plural = word + "es"
elif word.endswith("y"):
    plural = word[:-1] + "ies"
else:
    plural = word + "s"

print("Plural form:", plural)
