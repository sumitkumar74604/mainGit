'''
Hybrid Inheritance:combination of Multiple and Hirarchical Inheritance.
                A     B
                   C 
                D     E   
---------------------------------
'''

class A:
    #constructor
    def __init__(self):
        print("A's Constructor")
    def display(self):
        print("A's display method")
#------------------------------
class B:
    #constructor
    def __init__(self):
        print("B's Constructor")
    def display(self):
        print("B's display method")
#------------------------------
class C(A,B):
    #constructor
    def __init__(self):
        super().__init__()
        B.__init__(self)
        print("C's Constructor")
    def display(self):
        super().display()
        print("C's display method")  
#------------------------------
class D(C):
    #constructor
    def __init__(self):
        print("D's Constructor")
    def display(self):
        print("D's display method")  
#------------------------------
class E(C):
    #constructor
    def __init__(self):
        super().__init__()
        print("E's Constructor")
    def display(self):
        super().display()
        print("E's display method")                                
#------------------------------
obj = E()
obj.display()
B.display(obj)