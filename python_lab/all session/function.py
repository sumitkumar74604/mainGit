'''def greater(x,y):
    if(x>y):
        print("greater number = ",x)
    else:
        print("greater number = ",y)

greater(5,10)
'''
'''
#--------------------greater in three--------------------
def greater(x,y,z):
    if(x>y):
        if(x>z):
            print("greater number = ",x)
        else:
            print("greater number = ",z)
    elif(y>z):
        print("greater no. = ",y)
    else:
        print("greater no. = ",z)
greater(100,30,200)
'''
#------------------factorial-------------------------------
'''
def factorial(n):
    num=1
    while n!=0:
        num=num*n
        n-=1
    return num
x=factorial(5)
print("factoru=ial is = ",x)

'''
#------------------sum of two list-----------------------
'''
def a(numbers):
    total = 0
    for x in numbers:
        total = total + x
    return total

x=a([8,2,3,4,5,6])
y=a([1,2,3,4,5,6])
z=x+y
print("sum of two list = ",z)
'''

def a(t1,t2):
    
    return 0
t1=(12.5,15.3,45.6,14.8)
t2=(10,20,30,40,50)   

print(a(t1,t2))  
