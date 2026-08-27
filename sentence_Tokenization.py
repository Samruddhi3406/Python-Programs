import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text="Python is a easy to learn. It is a popular programming language."

sentences=sent_tokenize(text)

print("Sentence Tokens:",sentences)