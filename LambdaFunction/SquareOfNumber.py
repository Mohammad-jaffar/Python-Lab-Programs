# WAP to print the square of a given no using lambda function
number = int ( input( "Enter a no to get the square of it : "))

square = lambda number : number ** 2

print(f"The square of {number} is {square(number)}")