'''
Create a class Rectangle with three
data member (length, breadth & area
Rectangle) length and breadth data
member to store the value of length &
breadth of rectangle and third variable
area Rectangle to store the area of
rectangle. Now also create method
members
• inputValue()
-
to
take input for length and breadth from
user.
• calculateArea()
-
to
calculate area of rectangle.
• showArea()
-
to
display the area of rectangle.


Create a class DemoArithmetic with
three data member that are firstNo, secondNo to store the value given by the
user and third one is result to store
the result value.In this class also
create following method:
a.
inputValue()
-
to
take input value from user
b.
addition()
-
to
perform addition operation
c.
substraction()
-
to
perform substraction operation
d.
multiplication()
-
to
perform multiplication operation
e.
divide()
-
to
perform divide operation
'''
class Rectangle:
    'This is a class describing Rectangle and its properties'
    rec_length=0
    rec_breadth=0
    area_rect=0

    def inputvalue(self):
        self.rec_length=int(input("Enter rectangle length "))
        self.rec_breadth=int(input("Enter reactangle breadth "))
    
    def calculateArea(self):
        self.area_rect=self.rec_length*self.rec_breadth
    
    def showArea(self):
        print("The area is",self.area_rect)
    
r=Rectangle()

r.inputvalue()

r.calculateArea()

r.showArea()


print("================================")

class demoArithmetic:
    'This is a class describing three data member that are firstNo, secondNo to store the value given by the user and third one is result to store the result value.'
    firstno=0
    secondno=0
    thirdno=0
    def inputvalue(self):
        self.firstno=int(input("Enter a number "))
        self.secondno=int(input("Enter a second number "))
    def addition(self):
        self.thirdno=self.firstno+self.secondno
        print("The addition is",self.thirdno)
    def substraction(self):
        self.thirdno=self.firstno-self.secondno
        print("The substraction is",self.thirdno)
    def multiplication(self):
        self.thirdno=self.firstno*self.secondno
        print("The multiplication is",self.thirdno)
    def division(self):
        self.thirdno=self.firstno/self.secondno
        print("The division is",self.thirdno)

d=demoArithmetic()
d.inputvalue()
d.addition()
d.substraction()
d.multiplication()
d.division()