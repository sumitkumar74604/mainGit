'''
Function: 
It is a self contained block of statement which is used to perform a particular task.
It is used to reduce code.
Syntax:
def func_name(arguments):
    ...statements
    return return_value
=================
On the basis of return type and arguments, Functions are divided into four type:
1.function without return type and without argument.
2.function without return type and with argument.
3.function with return type and without argument.
4.function with return type and with argument.
'''

#Type 1:
def greeting():
    print("Good Morning!!!")
#-- 

greeting() 
print("--------------------")
#Type 2:
def add(a,b):
    print("Addition is:",a+b)

#-- 
add(12,23)
print("--------------------")

#Type 3:
def mul():
    c = a*b
    return c 
a=12
b=23
print("Multiplication is:",mul())
print("--------------------")

#Type 4:
def cube(a):
    return a*a*a 
print("Cube is:",cube(5))
print("-------------------")

#Required Arguments
def employeeDetails(name,id,salary):    
    print("Name is:",name)
    print("Id:",id)
    print("Salary:",salary)
    print("-------------------")
#----

#employeeDetails("Rahul Sharma",232,23000.0)
#employeeDetails(232,23000.0)
#TypeError: employeeDetails() missing 1 required positional argument: 'salary'

employeeDetails(101,"Videh Jaiswal",34000.0)
employeeDetails(id=101,salary=34000.0,name="Videh Jaiswal")

print("---------------------------------")

#default arguments
#def personDetails(city="Indore",name,age,gender):
#Non-default argument follows default argument
def personDetails(name,age,gender,city="Indore"):
    print("Name is:",name)
    print("Age is:",age)
    print("Gender is:",gender)
    print("City is:",city)
    print("---------------------------------")

personDetails("Ravi Soni",23,"Male")
personDetails(age=33,name="Neha Sharma",gender="Female",city="Ujjain")    

def fact(n):
    f=1
    while n!=0:
        f=f*n 
        n-=1
    return f 
print("Factorial is:",fact(5))           

print("------------------------------------")
