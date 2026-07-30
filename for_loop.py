num=int(input("enter number:"))
for i in range(1,num):
    print(i)

num=int(input("enter number:"))
for i in range(1,num):
    if i%2==0:
        print("Even no.s are:",i)

num=int(input("enter number:"))
for i in range(1,num):
    if i%2!=0:
        print("Odd no.s are:",i)

num=int(input("Enter no."))
for i in range(1,num):
    print(i*i)

n = 5
for i in range(1, n + 1):
    ch = ord('A')
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()

n=3
for i in range(n):
    ch = ord('A')
    for j in range(n):
        print(chr(ch), end=" ")
        ch += 1
    print()