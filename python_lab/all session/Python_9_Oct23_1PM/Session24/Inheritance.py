'''
Inheritance:code reusability.
When one class inherit properties,features of another class and another class have it's own properties and features.
Types of Inheritance:
1.Single Level Inheritance:

      Class A(Super,Base,Parent) ==> Class B(Subclass,Derieved,Child)
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

    def show(self):
        print("Id is:",self.id)
        print("Salary is:",self.salary)    
        print("Designation is:",self.designation)

#--- 

e1 = Employee("Neha Sharma",23,"Indore M.P",121,23456.23,"Python Django Developer")
e1.display()
e1.show()

        