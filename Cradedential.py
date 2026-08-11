# in a single data 

data = {"ID":1,"Name":"Ali","Course":"BCA","Password":"Ali@123"}
username = input("Enter the Name : ")
password = input("Enter the password : ")

if username == data["Name"]:
    if password == data["Password"]:
        print("Login Successfully")
    else:
        print("Incorrect password")
else:
    print("Username not found")

# multiple dictionaries 
# list of dictionaries
users = [
    {"ID": 1, "Name": "Ali", "Course": "BCA", "Password": "Ali@123"},
    {"ID": 2, "Name": "Jaffar", "Course": "BCA", "Password": "Jaffar@123"},
    {"ID": 3, "Name": "Ahmed", "Course": "BSc", "Password": "Ahmed@123"}
]
username = input("Enter Name : ")
password = input("Enter Password : ")

found = False

for user in users:
    if username == user["Name"] and password == user["Password"]:
        print("Login Successfully")
        found = True
        break
if not found:
    print("Invalid Username or Password")
   