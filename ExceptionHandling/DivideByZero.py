try:
    n=100
    res=n/0

except ZeroDivisionError:
    print("You Can't Divide By Zero")

except ValueError:
    print("Enter a Valid Number")

else:
    print("Result is",res)

finally:
    print("Execution Completed...")