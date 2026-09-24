import re

pattern=re.compile("Python")
text="Python is a programming language"

result=pattern.search(text)

if result:
    print("Pattern Found")
else:
    print("Pattern Not Found")