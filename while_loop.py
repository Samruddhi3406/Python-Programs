num=int(input("Enter a number:"))
i=1
while i<=num:
    print(i)
    i=i+1

num=int(input("Enter a number:"))
i=1
while i<=num:
    if i%2==0:
        print("Even Numbers",i)
    i=i+1

num=int(input("Enter a number:"))
i=1
while i<=num:
    if i%2!=0:
        print("Odd Numbers:",i)
    i=i+1

num=int(input("Enter a number:"))
i=1
sum=0
while i<=num:
    sum=sum+i
    i=i+1
print(sum)

num=int(input("Enter a number:"))
i=1
sum=0
while i<=num:
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)

num=int(input("Enter a number:"))
i=1
sum=0
while i<=num:
    if i%2!=0:
        sum=sum+i
    i=i+1
print(sum)

n = int(input("Enter a number: "))
while n>=1:
    print(n)
    n=n-1