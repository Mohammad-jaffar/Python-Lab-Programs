# Function to find the greatest number
def find_greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Function call
greatest = find_greatest(a, b, c)

# Display result
print("Greatest number =", greatest)