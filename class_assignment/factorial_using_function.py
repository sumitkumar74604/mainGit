'''
Wap to calculate factorial using funcion with return type and argument ?
'''
print("\nWap to calculate factorial using funcion with return type and argument ?\n")

def fact(num):
    f1=1
    while num!=0:
        f1=f1*num
        print("f1 - ",f1)
        num-=1
    return f1
        
num=int(input("Enter number - \t"))
f1=fact(num)
print("factorial - ",f1)