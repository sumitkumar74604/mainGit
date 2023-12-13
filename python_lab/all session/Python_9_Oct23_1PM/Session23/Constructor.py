'''
Constructor: 
1.It is used to initialize an object.
2.It called automatically when we create an object of a class.
3.It is a member of a class.
Syntax:

def __init__(self):
    ...statement

Types of Constructor:
1.Default Constructor
2.Parameterized Constructor
'''

class Student:

    def __init__(self):
        self.collegeName="IIT Indore"
        self.stud_name=""
        self.stud_rollno=0
        self.stud_course=""
        self.stud_fees=0.0
        print("calling default constructor")

    def display(self):
        print("Name is:",self.stud_name)
        print("Rollno is:",self.stud_rollno)
        print("Course is:",self.stud_course)
        print("Fees is:",self.stud_fees)
        print("College is:",self.collegeName)

#--- 

s1 = Student()
print(type(s1))
print("Base Class:",Student.__base__)
s1.stud_name = "Sonal Sharma"
s1.stud_rollno = 121
s1.stud_course = "BCA"
s1.stud_fees = 45678.45
s1.display()
