#Palindrome Check
string=input("Enter a String:")
rev=string[::-1]
if rev==string:
    print("String is palindrome")
else:
    print("String is not palindrome")