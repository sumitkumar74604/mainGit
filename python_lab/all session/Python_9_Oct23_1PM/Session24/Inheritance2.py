'''
Inheritance:code reusability.
When one class inherit properties,features of another class and another class have it's own properties and features.
Types of Inheritance:
2.Hierarchical Inheritance:

                  A

            B          C 

        D      E    F      G          
==========
Syntax:

class A:
    data member
    member method
class B(A):
    data member
    member method    
'''

class Person:
    name=""
    age=0
    address=""

    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def display(self):
        print("Name is:",self.name)
        print("Age is:",self.age)
        print("Address is:",self.address)
#--- 

class Employee(Person):

    def __init__(self,name,age,address,id,salary,designation):
        super().__init__(name,age,address)
        self.id=id
        self.salary=salary
        self.designation=designation

    #method overriding:same name and same arguments
    def display(self):
        super().display()
        print("Id is:",self.id)
        print("Salary is:",self.salary)    
        print("Designation is:",self.designation)

#--- 
print("=========== Employee Record ==================")
e1 = Employee("Neha Sharma",23,"Indore M.P",121,23456.23,"Python Django Developer")
e1.display()


class Student(Person):

    def __init__(self,name,age,address,rollno,course,fees):
        super().__init__(name,age,address)
        self.rollno=rollno
        self.course=course
        self.fees=fees

    #method overriding:same name and same arguments
    def display(self):
        super().display()
        print("Rollno is:",self.rollno)
        print("Course is:",self.course)    
        print("Fees is:",self.fees)

#--- 
print("=========== Student Record ==================")

e1 = Student("Priya Sharma",23,"Indore M.P",121,"BCA",34567.34)
e1.display()
        