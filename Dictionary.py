# Dictonary sequence type

# making dictionary using key:value
information = { "Name":"Ansar", "Age":22, "Course":"MA"}
# accessing whole dictionary
print(information)
# direct access
# using keys 
print("Name : ",information["Name"])
print("enrolled course is : ",information["Course"])
# returns all the keys
information.keys();
# returns all the values
information.values();
# retrun both the values and keys
information.items();
# adding in a dictionary
information["Address"] = "baroo"
print(information)
# modifying the values
information["Address"] = "Barsoo"
print(information)
# key with no value
information["Grade"] = " "
print (information)
# delete from dictionary
del information["Address"]
print(information)
information.pop("Age")
print(information)
information.popitem()
print(information)
# dictionary with same key
# the last key value override the same key value that's already exesting
info = {"Name":"ali","Name":"Nasir"}
print(info)
# using iteration to print the dictiony data in iterative maner
data = {" Name " : "Ali","Age":22,"Course":"MA","Address":"Baroo","GRADE":"A"}
# using for loop to print all the data in dictionary
for key,value in data.items():
    print(f"{key}:{value}")
# copy keyword
# it copys the whole dictionary to the new dictionary
datacopy = data.copy()
print(datacopy)
