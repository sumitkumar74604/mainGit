'''
A Lamba Function:
It is a anonymous function means it doesn't have any name.
It can take any number of arguments, but can only have one expression.
It return a function.
It doesn't have return and def keyword.
---------------
Syntax:
lamba arguments : expression
'''
#without arguments
greeting = lambda : print("Hello World")
greeting()

#with a argument
f1 = lambda a : a+10
print("Result :",f1(12))

#with arguments
f2 = lambda a,b : a+b
print("Addition is :",f2(12,23))

#tuple as a expression
f3 = lambda a,b : (a-b,a+b)
tup = f3(12,23)
print(tup[0],tup[1])

#return lambda in func
def myfunc(n):
    return lambda a:a*n
#---
f1 = myfunc(5)
print(f1(2))

#nested lambda
#return first method
first = lambda x: (lambda y:x+y)
#return second method
second = first(10)
print(second(20))

#map func using list
l1 = [45,56,67,78,89,90]
def square(n):
    print("val:",n)
    return n+2
l2 = map(square,l1)
print("Modified List:",list(l2),id(list(l2)))
print("Original List:",l1,id(l1))
print("=================================")
#map func using tuple
tup = (45,56,67,78,89,90)
def square(n):
    n=n+2
    return n 
tup_map = map(square,tup)
print("Modified Tuple:",tuple(tup_map))
print("Original Tuple:",tup)
print("=================================")

#map func using list of dic
list_dic = [
    {
    "name":"Neha Sharma",
    "id":12,
    "salary":23000.0    
},
{
    "name":"Mukesh Sharma",
    "id":11,
    "salary":25000.0    
},
{
    "name":"Priya Sharma",
    "id":10,
    "salary":24000.0    
},
{
    "name":"Muskan Sharma",
    "id":15,
    "salary":27000.0    
},
]

# return list of salary
# def change(obj):
#     return obj["salary"]+100

# mapObj = map(change,list_dic)
# print("list dic:",list(mapObj))

def change(obj):
    obj["salary"]=obj["salary"]+100
    return obj

mapObj = map(change,list_dic)
print("list dic:",mapObj)
print("list_original:",list_dic)

