# WAP to find the area and Perimeter  of a rectangle whose sides are given by the user
# formula :
#          area = length X width
#          Perimeter = 2 X ( length + width )

length = float ( input ( "Enter the length of rectangle : "))
width = float ( input ( " Enter the Width of rectangle : "))

area = lambda length, width : length * width
parameter = lambda length, width : 2 * ( length + width )

print(f"the area of rectangle with {length} and {width} is {area(length,width)}")
print(f"the parameter of rectangle with {length} and {width} is {parameter(length,width)}")

