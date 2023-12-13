'''
Prime Number: between 1 to 100
'''

a=1
count=0 
while a<=100:
    num = a
    n=2
    temp=1# else:
        #     print("Number is not a Prime Number",num) 
    if num == 1 or num == 0 :
        print("Number is not a Prime Number",num) 
    else:
        while n<=num//2:
            if num%n == 0:
                temp+1
        #     print("Number is not a Prime Number",num) p=0
                break
            n+=1 
#---    
        if temp==1:
            count+=1
            print("Number is a Prime Number:",temp)              
#---------- 
    a+=1
#--------------
print("Total prime number is:",count)


