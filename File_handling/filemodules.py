# Read functions
# file=open("File_handling/hello.txt","r")
# text=file.read()
# print(text)

# line=file.readline()
# print(line)

# lines=file.readlines()
# print(lines)

# write function
# with open("File_handling/hello.txt","w") as file:
#     file.write("Next session about datatypes")
#     file.close()

#append function
# file=open("File_handling/hello.txt","a")
# file.write("It will be conduct at 9:00am")
# file.close()

#r+ mode:  read+write
# with open("File_handling/hello.txt", "r+") as file:
#     print(file.read())
#     file.write("Hello")

#w+ mode: write+read
# with open("File_handling/hello.txt", "w+") as file:
#     file.write("Hello")
#     file.seek(0)
#     print(file.read())

# #a+ mode: append+read
# with open("File_handling/hello.txt", "a+") as file:
#     file.write("New Data")
#     file.seek(0)
#     print(file.read())

# x mode: create a new file
# file=open("File_handling/Newfile","x")
# file.write("Hello,Everyone")
# file=open("File_handling/Newfile","r")
# print(file.read())

#b mode:
# To read file
# rb:
# with open("File_handling//Newfile","rb")as file:
#     data=file.read()
#     print(data)

# rb+:
# with open("File_handling//Newfile","rb+")as file:
#     print(file.read())
#     file.write("Hello")
    
#To write
# wb:
# with open("File_handling/Newfile","wb")as file:
#     file.write(b"Hello and welcome to python programming\n")

# wb+:
# with open("File_handling/Newfile","wb+")as file:
#     file.write(b"Hello and welcome to python programming\n")
#     print(file.read())

#To append
# ab:
# with open("File_handling/Newfile","ab")as file:
#     file.write(b"Lets go\n")

#ab+:
# with open("File_handling/Newfile","ab+")as file:
#     file.write(b"Lets go\n")
#     print(file.read())
