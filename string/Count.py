#Count no. of vowels,consonants,digits,space,specialcharacter
str=input("Enter String:")
v_count=0
C_count=0
digit_count=0
space=0
special_character=0
for i in str:
    if i in "aeiouAEIOU":
        v_count=v_count+1
    elif '0'<= i <='9':
        digit_count+=1
    elif i==" ":
        space+=1
    elif i not in "aeiouAEIOU":
        C_count=C_count+1
    else:
        special_character+=1
print("Number of vowels:",v_count)
print("Number of consonants:",C_count)
print("Number of Digits:",digit_count)
print("Number of Spaces:",space)
print("Number of Special Character",special_character)