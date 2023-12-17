'''
OOPS:Object Oriented Programming Structure.
Object:Any real world entity.ex-laptop etc.
Properties:color,shape,size,price,modal etc.
Behaviour:Chair:=> sitting,rotate,move.
===================================================
Function — a set of instructions that perform a task. 
Method — a set of instructions that are associated with an object.
-----------
Functions are independent blocks of code that can be called from 
anywhere, while methods are tied to objects or classes and need an 
object or class instance to be invoked.
====================================================
Class: It is a blue print of an Object.
       It is a collection of an Objects.
       It is a user defined datatype.
       It is a collection of variables/attributes/properties and 
       methods/behaviour/features.
==============
Object: Memory
       It is an instance(example) of a Class.       
==============
Syntax:

class ClassName:
      'doc'
      data members
      member methods
========
self: It is a reference to current class      
'''

class Mobile:
    'This is a class contains information about Mobiles'

    #class variables,instance variables and object variables
    mob_brand=""
    mob_price=0.0
    mob_features=""

    def setData(self):
        print(self)
        self.mob_brand = input("Enter a Mobile Brand\n")
        self.mob_price = float(input("Enter a Mobile Price\n"))
        self.mob_features = input("Enter a Mobile Features\n")

    def getData(self):
        print("Mobile Brand is:",self.mob_brand) 
        print("Mobile Price is:",self.mob_price)
        print("Mobile Features is:",self.mob_features)
        print("===========================================")

#--- 

obj = Mobile()
obj1 = Mobile()
obj.setData()
#obj.getData()
# print("Module:",Mobile.__module__) 
# print("Document:",Mobile.__doc__)
# print("Base Class:",Mobile.__base__)
# print("Info:",Mobile.__dict__)

obj1.setData()
#obj1.getData()

#compare
if obj.mob_price > obj1.mob_price:
    print(obj.mob_brand," price is higher than ",obj1.mob_brand )
else:
    print(obj1.mob_brand ," price is higher than ", obj.mob_brand )


list_mobile = [obj,obj1]
for index in range(len(list_mobile)):
    list_mobile[index].getData()

    