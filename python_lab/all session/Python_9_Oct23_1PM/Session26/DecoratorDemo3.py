'''
Decorator: It is function that accept function as a argument and return a function.
It takes a result of function,modifies the results and return it.
In Decorators,  functions are taken as arguments into another function and then called inside wrapper function.
we use @function_name to specify a decorator to be applied on another function.
'''

print("========== Definition ==========")
def make_bold(fn):
    print("make_bold decorator")
    def wrapper():
        print("bold")
        return "<b>" + fn() + "</b>"
    return wrapper

def make_italic(fn):
    print("make_italic decorator")
    def wrapper():
        print("italic")
        return "<i>" + fn() + "</i>"
    return wrapper

@make_bold
@make_italic
def hello():
  return "hello world"

print("========== Execution ==========")
print(hello())