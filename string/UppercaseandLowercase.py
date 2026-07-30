#UppercaseandLowerCase
string=input("Enter string:")
upper_count=0
lower_count=0
for i in string:
    if i.isupper():
        upper_count+=1
    else:
        lower_count+=1
print("Number of Uppercase Letters:",upper_count)
print("Number of lowercase Letters:",lower_count)

