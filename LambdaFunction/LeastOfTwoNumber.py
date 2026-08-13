# WAP to find least of two no using lambda function using condition expression

a = int ( input ("Enter first number : "))
b = int ( input ("Enter second number : "))

least = lambda a,b : a if a < b else b

print ( "least number is : ", least(a,b))