# WAP using fucntion to get the grade of student after giving the percentage of the student
def GradeCalculator(marks):
    if marks >= 90 and marks <= 100:
        return "Grade A+"
    elif marks >= 80 and marks < 90:
        return "Grade A"
    elif marks >= 70 and marks < 80:
        return "Grade B"
    elif marks >= 60 and marks < 70:
        return "Grade C"
    elif marks >= 50 and marks < 60:
        return "Grade D"
    elif marks >= 0 and marks < 50:
        return "Grade Fail"
    else:
        return "Invalid Percentage"

# Main Program
marks = float(input("Enter your percentage: "))
print("Your Grade is:", GradeCalculator(marks))