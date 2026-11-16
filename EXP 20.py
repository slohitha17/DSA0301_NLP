from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = [
    "Python is a programming language",
    "Machine learning uses Python",
    "NLP is used for text processing"
]

query = input("Enter search query: ")

v = TfidfVectorizer()
x = v.fit_transform(docs)
q = v.transform([query])

score = cosine_similarity(q, x)

for i in score[0].argsort()[::-1]:
    print("Document", i+1, ":", docs[i])
