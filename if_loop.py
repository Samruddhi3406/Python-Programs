marks=int(input("enter marks:"))
if marks>=85:
    print('Grade A')
elif marks>=75:
    print('Grade B')
elif marks>=55:
    print('Grade C')
elif marks>=35:
    print('Grade D')
else:
    print("Fail")

n=int(input("enter a number:"))
if n==0:
    print("Number is zero")
else:
    print("Number is not zero")

num1=int(input("Enter a number1:"))
num2=int(input("Enter a number2:"))
if num1>num2:
    print("Largest number is:",num1)
else:
    print("Largest number is:",num2)

num=int(input("Enter a number:"))
if num>0:
    print("Number is positive")
else:
    print("Number is negative")

ch=(input("Enter character:"))
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("character is vowel")
else:
    print("character is consonant")


num1=int(input("Enter a number1:"))
num2=int(input("Enter a number2:"))
num3=int(input("Enter a number3:"))
if num1>num2 and num1>num3:
    print("largest number is:",num1)
elif num2>num3:
    print("largest number is:",num2)
else:
    print("largest number is:",num3)


num1=int(input("Enter a number1:"))
num2=int(input("Enter a number2:"))
num3=int(input("Enter a number3:"))
if num1<num2 and num1<num3:
    print("Smallest number is:",num1)
elif num2<num3:
    print("Smallest number is:",num2)
else:
    print("Smallest number is:",num3)

num=int(input("Enter a number:"))
if num%2==0:
    print("Even")
else:
    print("Odd")

year=int(input("Enter a year: "))
if (year%400==0) or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")

