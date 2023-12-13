'''
Decorator: It is function that accept function as a argument and return a function.
It takes a result of function,modifies the results and return it.
In Decorators,  functions are taken as arguments into another function and then called inside wrapper function.
we use @function_name to specify a decorator to be applied on another function.
'''

def decorator1(func):
    def inner():
        val=func()+12 #15+12=27
        print("d1:",val)
        return val
    return inner
22
def decorator2(func):
    def inner():
        val=func()+15 #0+15=15
        print("d2:",val)
        return val
    return inner

def decorator3(func):
    def inner():
        val=func()%10 #10%10=0
        print("d3:",val)
        return val
    return inner

@decorator1
@decorator2
@decorator3
def sum():
    return 10

print("Sum is:",sum())