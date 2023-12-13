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

    #parameterized constructor
    def __init__(self,stud_name,stud_rollno,stud_course,stud_fees):
        self.collegeName="IIT Indore"
        self.stud_name=stud_name
        self.stud_rollno=stud_rollno
        self.stud_course=stud_course
        self.stud_fees=stud_fees
        print("calling default constructor")

    def display(self):
        print("Name is:",self.stud_name)
        print("Rollno is:",self.stud_rollno)
        print("Course is:",self.stud_course)
        print("Fees is:",self.stud_fees)
        print("College is:",self.collegeName)

#--- 

s1 = Student("Raj Sharma",121,"BCA",34567.34)
s1.display()
