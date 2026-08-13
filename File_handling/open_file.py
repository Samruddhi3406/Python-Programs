file=open("File_handling/hello.txt","r")
print(file.read())
file.close()

#With Statement
with open("File_handling/hello.txt","r") as file:
    data=file.read()
    print(data)
    file.close()