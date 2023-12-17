'''
4. create a function which accepts an
array of Int in argument and print sum
of all elements
'''

print("4. create a function which accepts an array of Int in argument and print sum of all elements")
print("------ without function-------")
a=[11,22,33,44,55]
sum=0
for i in range (len(a)):
    sum=sum+a[i]
    print([i],a[i])
print("sum - ",sum)

print("------ with function-------")
def array(a):
    sum=0
    for i in range (len(a)):
        sum=sum+a[i]
        print([i],a[i])
    print("sum - ",sum)

array(a=[11,22,33,44,55])


print("------ with function value taken from user-------")

def array(a):
    sum=0
    for i in range (len(a)):
        sum=sum+a[i]
        print([i],a[i])
    print("sum - ",sum)

print("enter last digit :- ",end="")
num=int(input())
a=[]
for i in range (num):
    print([i],"enter element :- ",end="")
    x=int(input())
    a.append(x)
print("-------------user output--------------------")
array(a)
