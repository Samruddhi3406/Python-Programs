#Reverse string
string=input("Enter a String:")
rev=""
for i in string:
    rev=i+rev
print("Reverse String:",rev)