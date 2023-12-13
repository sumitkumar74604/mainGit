'''
Prime Number:
'''

num = 7
n=2
temp=1
if num == 1 or num == 0 :
   print("Number is not a Prime Number",num) 
else:
    while n<=num//2:
        if num%n == 0:
            temp=0
            break
        n+=1 
#---    
    if temp==1:
        print("Number is a Prime Number:",num)
    else:
        print("Number is not a Prime Number",num)               
