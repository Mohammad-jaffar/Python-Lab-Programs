# WAP to print the result of the Student when the Student input percentage ( below 40 is fail ) and rest pass

# syntax : variable = "output1 " if condition else "output2"

marks = float ( input ("Enter the marks of the student : "))

result = lambda marks : "Pass " if marks > 40 else "Fail"

print(result(marks))