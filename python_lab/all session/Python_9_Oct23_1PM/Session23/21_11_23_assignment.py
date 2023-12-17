'''
1. Create class Farmer with varibales (name, crop, earning).
- Create perameterized constructor.
- Create display function
- Compare earnings of two Farmers and print name and crop of farmer who earns more.
'''
print("\n1. Create class Farmer with varibales (name, crop, earning). - Create perameterized constructor.")
print("- Create display function")
print("- Compare earnings of two Farmers and print name and crop of farmer who earns more.\n")

class Farmer:
    def __init__(self,name,crop,earning):
        self.name=name
        self.crop=crop
        self.earning=earning
    
    def display(self):
        print(" Farmer Name - ",self.name)
        print(" Farmer Crop - ",self.crop)
        print(" Farmer Earning - ",self.earning)
        
f=Farmer("Tichku","Rice",485320.254)
f1=Farmer("pillu","Maze",482135.125)
f.display()
f1.display()
print("-----------------------------")
f1.display()
print("--------------compare------------------")

if f.earning>f1.earning:
    print(" Farmer ",f.name," earned more  then Farmer - ",f1.name,f.earning-f1.earning)
else:
    print(" Farmer ",f1.name," earned more then Farmer  - ",f.name,f1.earning-f.earning)

print("*******************************************************************************")

'''

2. Create class Circle with variable radius.
- Create parameterized constructor.
- Create display function to display radius and area.
- Create function isBiggerThan( c:otherCircle) -> Bool  
- Create Two objects and call all the above functions
'''

print("\n2. Create class Circle with variable radius.")
print(" Create parameterized constructor.")
print("- Create display function to display radius and area.")
print("- Create function isBiggerThan( c:otherCircle) -> Bool ")
print("- Create Two objects and call all the above functions\n")

class Cycle:
    def __init__(self,radius) :
        self.radius=radius
        
    def display(self):
        print(" The Radius is - ",self.radius)
        print(" The Area of circle is - ",3.14*self.radius*self.radius)

    def Bigger(self,c):
        if c.radius>c1.radius:
            print("1st  Bigger then - 2nd  ")
            return True
        else:
            print("1st isn't Bigger then - 2nd ")
            return False
        
    
c=Cycle(6)
c1=Cycle(5)
c.display()
print("----------------------------------------------------------------------")
c1.display()
print("-----------------------------------")
print(c.Bigger(c))