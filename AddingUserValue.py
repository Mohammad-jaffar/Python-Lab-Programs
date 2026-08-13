# WAP to calculate the sum of no's of input by the user. User may input any of integer
def Calculator(*args):
    sum = 0

    for num in args:
        sum = sum + num
    return sum

n = int(input("How many numbers do you want to enter : "))
numbers =[]
for i in range(n):
    num = int(input(f"Enter number for {i+1} : "))
    numbers.append(num)

print("Sum =",Calculator(*numbers))
