'''
Find L.C.M of two numbers:

 4 | 12, 16
 ------------
   |  3 , 4

lcm is : 48   
'''

n1 = 12
n2 = 16
max = 0
if n1>n2:
    max = n1
else:
    max = n2 

while True:
    if max%n1 == 0 and max%n2 == 0:
        print("L.C.M is:",max)
        break
    print("max:",max)
    max+=1
