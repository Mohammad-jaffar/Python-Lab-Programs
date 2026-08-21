class StudentDetails:
    sem = "BCA 5th"
    def __init__(self,name):
        self.name = name
        print("Name : " , self.name)
        print("Semester : ", self.sem)

S1 = StudentDetails("Ali")
s2 = StudentDetails("Khan")
print()

class Students:
    def __init__(self, name, sem):
        self.name = name
        self.sem = sem

    def display(self):
        print("Name : ",self.name)
        print("Sem : ",self.sem)
Stu1 = Students("Ali","BCA 3rd")
Stu2 = Students("Nasir","BCA 1st")
Stu1.display()
Stu2.display()