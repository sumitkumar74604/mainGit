'''
Decorator: It is function that accept function as a argument and return a function.
It takes a result of function,modifies the results and return it.
In Decorators,  functions are taken as arguments into another function and then called inside wrapper function.
we use @function_name to specify a decorator to be applied on another function.
'''

#decorator
def decorator1(func):
    def inner():
        print("======Good Morning:d1=====")
        func()
    return inner 

def decorator2(func):
    def inner():
        print("======Good Evening d2=====")
        func()
    return inner 

def decorator3(func):
    def inner():
        print("=====Good Night:d3=====")
        func()
    return inner    
           
@decorator1
@decorator2
@decorator3
def f1():
    print("=====Good Afternoon======")

f1()