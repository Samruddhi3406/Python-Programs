# 1.	Write a program to building a simple student grade management system for a class of students. The system will store student names and their grades (both as lists) and should be able to perform the following operations:
# ●	Add a new student and their grade.
# ●	Update the grade of an existing student.
# ●	Remove a student from the list.
# ●	Calculate and display the average grade of the class.
# ●	Display the highest and lowest grades in the class.

StudentNames = []
StudentGrades = []
while True:
    print("------ Student Grade Management System -----")
    print("1. Add a new student and their grade")
    print("2. Update the grade of an existing student")
    print("3. Remove a student from the list")
    print("4. Calculate and display the average grade of the class")
    print("5. Display the highest and lowest grades in the class")
    print("6. Exit")

    choice=int(input("Enter your choice (1-6): "))

    if choice==1:
        name=input("Enter student name:")
        grade=float(input("Enter student grade:"))
        StudentNames.append(name)
        StudentGrades.append(grade)
        print("Student added successfully!")

    elif choice==2:
        name=input("Enter student name to update grade:")
        if name in StudentNames:
            index=StudentNames.index(name)
            new_grade=float(input("Enter new grade:"))
            StudentGrades[index]=new_grade
            print("Grade updated successfully!")
        else:
            print("Student not found!")

    elif choice==3:
        name=input("Enter student name to remove:")
        if name in StudentNames:
            index=StudentNames.index(name)
            StudentNames.pop(index)
            StudentGrades.pop(index)
            print("Student removed successfully!")
        else:
            print("Student not found!")

    elif choice==4:
        if len(StudentGrades)>0:
            average=sum(StudentGrades)/len(StudentGrades)
            print("Average grade of the class:",average)
        else:
            print("No students in the list!")

    elif choice==5:
        if len(StudentGrades)>0:
            highest=max(StudentGrades)
            lowest=min(StudentGrades)
            print("Highest grade in the class:",highest)
            print("Lowest grade in the class:",lowest)
        else:
            print("No students in the list!")

    elif choice==6:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice! Please try again.")

        