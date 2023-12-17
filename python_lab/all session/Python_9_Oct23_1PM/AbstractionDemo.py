'''
'''
Abstraction:
It declares only functions but do not have body.
We can not create object of an Abstract Class.
'''

from abc import ABC,abstractmethod
#abstract class
class TwoDShape(ABC):

    def __init__(self):
        self.area=0.0
        self.perimeter=0.0
        self.shapeName=""

    @abstractmethod
    def findArea(self):
        pass

    @abstractmethod    
    def findPerimeter(self):
        pass

    def display(self):
        print("ShapeName is:",self.shapeName)
        print("Area is :",self.area)
        print("Perimeter is:",self.perimeter)
        print("==================================")
#-- 
#Concreate Class
class Square(TwoDShape):

    def __init__(self):
        super().__init__()
        self.side=0

    #concrete method
    def findArea(self):
        self.area = self.side*self.side

    def findPerimeter(self):
        self.perimeter=4*self.side

#-- 

s1 = Square()  
s1.shapeName="Square"      
s1.side =16
s1.findArea()
s1.findPerimeter()
s1.display()

class Rectangle(TwoDShape):

    def __init__(self):
        super().__init__()
        self.length=0
        self.breadth=0

    #concrete method
    def findArea(self):
        self.area = self.length*self.breadth

    def findPerimeter(self):
        self.perimeter=2*(self.length+self.breadth)
#-- 

r1 = Rectangle()
r1.shapeName = "Rectangle"   
r1.length=12.23
r1.breadth=34.23     
r1.findArea()
r1.findPerimeter()
r1.display()

print("==========")

def fencingCharges(shape):
    fen_charges = shape.area*12
    print("Shape Name is:",shape.shapeName)
    print("Fencing Charges is:",fen_charges)
    print("----------------")

fencingCharges(s1)
fencingCharges(r1)        