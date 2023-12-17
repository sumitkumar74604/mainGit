'''
Type Casting: It is a mechanism to convert one type of reference into another type.
In Python, variables are of dynamic type i.e their is no fixed datatype.so when we assign any value to that variable, it datatype depends upon that value type.
'''

#Dynamic Type
x = 30
print("Age is:",x)
x = "Videh Jaiswal"
print("Name is:",x)
x = 34567.33
print("Salary is:",x)
print("------------------")

#Convert String into Int
age = "30" # Obj1 
print("Type is:",type(age))
print("Age is:",age)
print("------------------")
age = int(age) # Obj2
print("Type is:",type(age))
print("Age is:",age)

#Convert String into Float
salary = "34567.34"
print("Type is:",type(salary))
print("Salary is:",salary)
print("------------------")
salary = float(salary)
print("Type is:",type(salary))
print("Salary is:",salary)
print("------------------")

#Exceptional Case: We can convert only numeric string value to int
#gender = "Male"
#gender = int(gender)
#ValueError: invalid literal for int() with base 10: 'Male'
print("********************************")

nage = 45
print("Type is:",type(nage))
print("New Age is:",nage)
print("------------------") 
nage = str(nage)
print("Type is:",type(nage))
print("New Age is:",nage)
print("------------------") 