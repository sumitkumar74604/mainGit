'''
Inheritance:code reusability.
When one class inherit properties,features of another class and another class have it's own properties and features.
Types of Inheritance:
3.Multiple Inheritance:
               A     B
                  C
==========
Syntax:

class A:
    data member
    member method
class B(A):
    data member
    member method    
'''

class A:

    def __init__(self):
        print("A's Constructor")

    def display(self):
        print("A's Display method")    

class B:

    def __init__(self):
        print("B's Constructor")

    def display(self):
        print("B's Display method")     
    
class C(A,B):

    def __init__(self):
        super().__init__()
        B.__init__(self)
        print("C's Constructor")  

    def display(self):
        super().display()
        B.display(self)
        print("C's Display method")           

obj = C()
obj.display()
