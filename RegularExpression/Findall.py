import re

text = "I like Python and Python is easy"
result = re.findall("Python", text)

print(result)