#Remove all spaces from the input string. 
str=input("Enter a String:")
no_space=""
for i in str:
    if i!=" ":
        no_space+=i
print(no_space)