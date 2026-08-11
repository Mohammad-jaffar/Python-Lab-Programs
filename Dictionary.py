# dictionary sequence type 

# making dictionary using key : value

information = { "Name":"Ali","Age":10, "Course":"MA", "Address":"Barsoo"}
# accessing whole dictionary
print(information)
# direct access
# using keys
print("Name : ", information["Name"])
print("Enrolled course is : ", information["Course"])
# reutrns all the key
information.keys()
# returns all the values
information.values()
# retrun both the key and values 
information.items()
# adding in dictionary
information["CGPA"] = 8
print(information)
# modifying the values
information["Course"] = "BA"
print(information)
# key with no value 
information["Grade"] = " "
print(information)
# delete from dictionary
del information["Grade"]
print(information)
information.pop("Address")
print(information)
information.popitem()
print(information)

# dictionary with same key
# the last key value override the same key value that's already existing
info = { "Name":"Ali","Name":"Nasir"}
print(info)

#using iteration to print the dictionary data in iterative manner
data = { "Name":"Nadeem", "Age":22,"Course":"BSC","Address":"Barsoo"}
for key,value in data.items():
    print(f"{key}:{value}")

# copy keyword
datacopy = data.copy()
print(datacopy)