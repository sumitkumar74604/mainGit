'''
For Loop:
range(n):
single arg: start=0 and stop=n-1
-----------------------------------
range(n1,n2)
two arg: start=n1 and stop=n2-1
-----------------------------------
range(n1,n2,step)
three arg: start=n1 , stop=n2-1 and step=more than 1
'''

#print hello world five times
for x in range(5):
    print("x is:",x)
print("----------------------")

for a in range(1,6):
    print("a is:",a)
print("----------------------")

for b in range(0,10,2):
    print("b is:",b)
print("----------------------")

for c in range(10,0,-2):
    print("c is:",c)

print("--------------")

#find palindrome number
num=121
temp=num
rev=0
for a in range(1,num):
    if num!=0:
        rem=num%10 #1 2 1
        rev=rev*10+rem #1 12 121
        num=num//10 #12 #1 0
        print(rev)

if temp==rev:
    print("Number is a palindrome number")
else:
    print("Number is not a palindrome number")    

