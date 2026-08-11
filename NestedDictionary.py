users = {
    "Ali": {
        "ID": 1,
        "Course": "BCA",
        "Password": "Ali@123"
    },
    "Jaffar": {
        "ID": 2,
        "Course": "BCA",
        "Password": "Jaffar@123"
    },
    "Ahmed": {
        "ID": 3,
        "Course": "BSc",
        "Password": "Ahmed@123"
    }
}

username = input("Enter Name: ")
password = input("Enter Password: ")

if username in users:
    if users[username]["Password"] == password:
        print("Login Successfully")
    else:
        print("Incorrect Password")
else:
    print("Username Not Found")