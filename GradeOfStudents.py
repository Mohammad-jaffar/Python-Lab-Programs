# wap to print the grade of student's. User has to enter his or her percentage and as per the percentage return grade using fucntion 
# 90 - 100 -> A+ , 80 - 89 -> A , 70 - 79 -> B , 60 - 69 -> C , 50 - 59 -> D , 40 - 49 -> E , marks < 40 -> fail
def GradeGenerator(marks):
    if marks >= 90 and marks <= 100:
        return "A+"
    elif marks >= 80 and marks <= 89:
        return "A"
    elif marks >= 70 and marks <= 79:
        return "B"
    elif marks >= 60 and marks <= 69:
        return "C"
    elif marks >= 50 and marks <= 59:
        return "D"
    elif marks >= 40 and marks <= 49:
        return "E"
    elif marks >= 0 and marks < 40:
        return "Fail"
    else:
        return "Invalid Percentage"

percentage = float(input("Enter your percentage : "))
grade = GradeGenerator(percentage)
print("Grade : ",grade)