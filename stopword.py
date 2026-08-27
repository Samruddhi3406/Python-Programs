import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

text="Python is a popular programming language and it is easy to learn."

words=word_tokenize(text)

stop_words=set(stopwords.words('english'))

filtered_words=[word for word in words if word.lower() not in stop_words]

print("Original words:")
print(words)

print("After Removing Stopwords:")
print(filtered_words)