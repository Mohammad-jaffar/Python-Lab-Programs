for i in range(0,20,2):
    print(i)
    
numbers = (1,2,3,4,5,6,8,96,54)
for i in numbers:
    print(i)

# syntax
# for index in sequence:
#   print(i)

Students = [ " ali" , " nasir " , " zakir ", " Khan" , " Fatima"]

for i in range(len(Students)):
    print(i)
    print(Students[i])
    
    # formated version
    print(f"{i} Students in {Students[i]}")
