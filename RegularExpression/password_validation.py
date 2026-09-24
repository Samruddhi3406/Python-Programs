import re

password=input("Enter Password:")

if re.search(r'^(?=.*[A-Za-z])(?=.*[0-9])(?=.*[@#$%]).{8,}$',password):
    print("Valid Password")
else:
    print("Invalid Password")