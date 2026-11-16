
import re

exp = input("Enter logical expression: ")

if re.match(r'^[A-Za-z]+\([A-Za-z]+\)$', exp):
    print("Valid logical expression")
else:
    print("Invalid logical expression")
