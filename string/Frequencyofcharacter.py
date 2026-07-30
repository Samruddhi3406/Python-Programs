#Find the number of times a specified character appears in a string
String=input("Enter a string:")
target_character=input("Enter charcter:")
frequency=0
for char in String:
    if char==target_character:
        frequency+=1
print("Frequency of '" + target_character + "':", frequency)