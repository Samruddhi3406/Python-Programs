class InvalidAgeException(Exception):
    pass
Valid_age=18

try:
    input_age=int(input("Enter your age:"))
    if input_age<Valid_age:
        raise InvalidAgeException
    else:
        print("Eligible")
        
except InvalidAgeException:
    print("Invalid Age")