import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')

text="Python is easy to learn. It is a popular programming language."
words=word_tokenize(text)

print("Word Tokens:",words)