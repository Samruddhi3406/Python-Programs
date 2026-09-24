import re

text = "My phone number is 9876543210"

result = re.search("[0-9]+", text)

if result:
    print("Number found:", result.group())
else:
    print("Number not found")