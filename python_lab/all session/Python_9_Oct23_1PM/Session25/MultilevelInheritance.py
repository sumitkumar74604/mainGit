'''
Multi Level Inheritance:
A=>B=>C=>D=>E......
-------------------------
Runtime polymorphism is nothing but method overriding. In Python, method overriding occurs when a derived class provides its own implementation of a method that is already defined in its base class.
'''

class OneBHK:
    def __init__(self,room,kitchen,hall):
        self.room=room
        self.kitchen=kitchen
        self.hall=hall

    def getArea(self):
        return self.room+self.kitchen+self.hall

    def display(self):
        print("Room is:",self.room)
        print("Hall is:",self.hall)
        print("Kitchen is:",self.kitchen)
#--- 

o1 = OneBHK(100,80,120)
o1.display()
print("Area of OneBHK is :",o1.getArea())
print("===============================================")
#--------------------

class TwoBHK(OneBHK):

    def __init__(self, room, kitchen, hall, secondroom):
        super().__init__(room, kitchen, hall)
        self.secondroom=secondroom

    def getArea(self):
        return super().getArea() + self.secondroom

    def display(self):
        super().display() 
        print("Second Room is:",self.secondroom)
#-----

t1 = TwoBHK(110,90,130,100)
t1.display()
print("Area of TwoBHK is:",t1.getArea())
print("===============================================")

class ThreeBHK(TwoBHK):

    def __init__(self,room,kitchen,hall,secondroom,thirdroom):
        super().__init__(room,kitchen,hall,secondroom)
        self.thirdroom=thirdroom

    def getArea(self):
        return super().getArea() + self.thirdroom

    def display(self):
        super().display() 
        print("Third Room is:",self.thirdroom)
#--

th1 = ThreeBHK(120,70,140,100,90)
th1.display()
print("Area of ThreeBHK is:",th1.getArea())

print("===============================================")

def paintingCharges(flat):
    area = flat.getArea()
    charges = area*12

    #isinstance :Return whether an object is an instance of a class or of a subclass thereof.
    if isinstance(flat,OneBHK):
        print("OneBHK")
        charges=charges-charges*5/100

    if isinstance(flat,TwoBHK):
        print("TwoBHK")
        charges = area*12
        charges=charges-charges*8/100    

    if isinstance(flat,ThreeBHK):
        print("ThreeBHK")
        charges = area*12
        charges=charges-charges*10/100         

    return charges    
#-------

print("Charges of OneBHK in Rs:",paintingCharges(o1))
print("Charges of TwoBHK in Rs:",paintingCharges(t1))
print("Charges of ThreeBHK in Rs:",paintingCharges(th1))

