'''
 wap to check the prime number using function with argument and return type ?
'''

print("\nwap to check the prime number using function with argument and return type ?\n")

def prime(num):
    i=1
    count=0
    while i<=num:
        if num%i==0:
            count+=1
            #print(i)
            #print("Count - ",count)
        i+=1
    return count

num=int(input("Enter Number - "))
p1=prime(num)
if(p1==2):
    print("Given Number Is Prime - ",num)
else:
    print("Given Number Isn't Prime - ",num)
    
        