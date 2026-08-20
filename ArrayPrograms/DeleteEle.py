arr=[12,45,64,32,78,90]
num=int(input("Enter a number to delete"))
for i in arr:
    if num==i:
        arr.remove(num)

print("Array after deletion:",arr)