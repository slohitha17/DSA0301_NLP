import re

s = input("Enter text: ")
print("Match:", re.findall(r"cat", s))
print("Search:", bool(re.search(r"dog", s)))
