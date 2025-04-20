#Given marks of a student, print on the screen:

#Grade A if marks >= 90
#Grade B if marks >= 70
#Grade C if marks >= 50
#Grade D if marks >= 35
#Fail, otherwise.


marks = int(input("Enter marks to know the grade: "))

def getGrade(marks):
    if marks >= 90:
        return "Grade A"
    elif marks >= 70:
        return "Grade B"
    elif marks >= 50:
        return "Grade C"
    elif marks >= 35:
        return "Grade D"
    else:
        return "Fail"

grade = getGrade(marks)
print(f"Your grade is: {grade}")

