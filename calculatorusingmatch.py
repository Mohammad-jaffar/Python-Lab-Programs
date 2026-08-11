# WAP of calculator using match condition where the user have to give the inputs

def Calculator(num1, num2,result):
    match result:
        case "Add":
            print(num1+num2)
        case "Sub":
            print(num1-num2)
        case "Mul":
            print(num1*num2)
        case "Div":
            print(num1/num2)
        case "+":
            print(num1+num2)
        case "-":
            print(num1-num2)
        case "/":
            print(num1/num2)
        case "*":
            print(num1*num2)
        case _:
            print("Enter a valid operator")

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the secount number : "))
result = input("Enter the operator (Add,Sub,Mul,Div , /, *, + , - ) : ")
Calculator(num1,num2,result)
