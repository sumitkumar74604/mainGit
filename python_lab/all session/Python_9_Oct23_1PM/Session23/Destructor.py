'''
Destructor:
1.It is used to de-initialize object.
2.It is a member of a class.
3.It is called automatically at last of program execution.
Syntax:
def __del__(self):
    ...statement    
'''

class Student:
     #parameterized constructor
    def __init__(self,stud_name,stud_rollno,stud_course,stud_fees):
        self.collegeName="IIT Indore"
        self.stud_name=stud_name
        self.stud_rollno=stud_rollno
        self.stud_course=stud_course
        self.stud_fees=stud_fees
        print("=============calling default constructor======")    

    def display(self):
        print("Name is:",self.stud_name)
        print("Rollno is:",self.stud_rollno)
        print("Course is:",self.stud_course)
        print("Fees is:",self.stud_fees)
        print("College is:",self.collegeName)

    def __del__(self):
        print("=============calling destructor===========")    

#--- 

s1 = Student("Raj Sharma",121,"BCA",34567.34)
s1.display()

# 1. Create class Farmer with varibales
# (name, crop, earning).
# - Create perameterized
# constructor.
# - Create display function
# - Compare earnings of two Farmers
# and print name and crop of farmer who
# earns more.

# 2. Create class Circle with variable
# radius.
# - Create parameterized constructor.
# - Create display function to display
# radius and area.
# - Create function isBiggerThan( c:
# otherCircle) -> Bool
# - Create Two objects and call all the
# above functions