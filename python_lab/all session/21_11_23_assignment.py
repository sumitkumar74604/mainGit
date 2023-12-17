'''
Create a class Rectangle with three data member (length, breadth & area
Rectangle) length and breadth data member to store the value of length &
breadth of rectangle and third variable area Rectangle to store the area of
rectangle. Now also create method members

• inputValue() - to take input for length and breadth from user.

• calculateArea()- to calculate area of rectangle.

• showArea() - to display the area of rectangle.
'''
print("------------------------ 1st Assignment -------------------")
print("\n''' Create a class Rectangle with three data member (length, breadth & area Rectangle) length and breadth data member to store the value of length &  readth of rectangle and third variable area Rectangle to store the area of rectangle. Now also create method members ''' ")
print("• inputValue() - to take input for length and breadth from user.")
print("• calculateArea()- to calculate area of rectangle.")
print("• showArea() - to display the area of rectangle.\n")


class rectangle:
    'Rectangle data '
    length=0
    breadth=0
    area_of_rect=0
    
    def input_data(self):
        self.length=float(input("enter rectange length - \t"))
        self.breadth=float(input("enter rectange Breadth -  \t"))
    
    def output_data(self):
        print("The area of Rectangle - \t",self.area_of_rect)
    
    def cal(self):
            self.area_of_rect=self.length*self.breadth  
r=rectangle()
r.input_data()
r.cal()
r.output_data()
print("****************************************************************************")


'''

Create a class DemoArithmetic with three data member that are firstNo, secondNo to store the value given by the
user and third one is result to store the result value.In this class also
create following method:
a. inputValue() - to take input value from user
b. addition() - to perform addition operation
c. substraction() - to perform substraction operation
d. multiplication() - to perform multiplication operation
e. divide() - to perform divide operation
'''
print("\n--------------------- 2nd Assignment -----------------------")
print(" \nCreate a class DemoArithmetic with three data member that are firstNo, secondNo to store the value given by the user and third one is result to store the result value.In this class also create following method:")
print("a. inputValue() - to take input value from user")
print("b. addition() - to perform addition operation")
print("c. substraction() - to perform substraction operation")
print("d. multiplication() - to perform multiplication operation")
print("e. divide() - to perform divide operation\n")

class demo_arthihemetic:
    num_1st=0
    num_2nd=0
    num_3rd=0
    
    def get_data(self):
        self.num_1st=int(input("enter first digit - \t"))
        self.num_2nd=int(input("enter second digit - \t"))
    
    def add(self):
        self.num_3rd=self.num_1st+self.num_2nd
        print("\nAddition - \t",self.num_1st," + ",self.num_2nd," = ",self.num_3rd)
        
    def sub(self):
        self.num_3rd=self.num_1st-self.num_2nd
        print("Subtraction - \t",self.num_1st," - ",self.num_2nd," = ",self.num_3rd)
        
    def multi(self):
        self.num_3rd=self.num_1st*self.num_2nd
        print("Multiplication -",self.num_1st," * ",self.num_2nd," = ",self.num_3rd)
        
    def divide(self):
        if self.num_1st<=0:
            print("Division is : 0")
        elif self.num_2nd<=0:
            print("division is : infinite")
        else:
            self.num_3rd=self.num_1st/self.num_2nd
            print("division - \t",self.num_1st," / ",self.num_2nd," = ",self.num_3rd)
        
d=demo_arthihemetic()
d.get_data()
d.add()
d.sub()
d.multi()
d.divide()
