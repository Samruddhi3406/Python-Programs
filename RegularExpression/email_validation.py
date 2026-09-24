import re
email=input("Enter an email:")

if re.search(r'@gmail.com$',email):
    print("Valid Email")
else:
    print("Invalid Email")