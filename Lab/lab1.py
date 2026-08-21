# wap in python script to take three input from user name , address, age and show in formated string 
# hii {name} your age is {age} you live at{address}

name = input ("Enter you'r name : ")
age = int (input("Enter you'r age : "))
address = input ("Enter you'r address : ")

print (f"hii {name} your age is {age} you live at {address}")



# class 
class Details:
    def __init__(self,name,address,age):
       self.name = name
       self.address = address
       self.age = age

    def display(self):

        print(f"hii {self.name} your age is {self.age} you live at {self.address}")
# object of class
d1 = Details("Ali","Baroo",22)
# function to diaplay the details
d1.display()
