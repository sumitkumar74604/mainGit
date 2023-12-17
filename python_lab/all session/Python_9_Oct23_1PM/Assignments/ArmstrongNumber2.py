'''
Find Armstrong number between 1 to 1000
'''

a=1
while a<=10000:
    num = a
    temp = num 
    count=0
    while num!=0:
        count+=1
        num=num//10
    #----
    #print("Count is:",count)
    num=temp 
    power=1
    sum=0
    while num!=0:
        rem=num%10 #3
        for x in range(1,count+1):
            power = power * rem # 1*7 = 7, 7*7=49, 49*7=343
        #print(rem," power of ",count," = ",power)    
        sum = sum + power # 1 + 343 + 27 = 371
        power = 1
        num=num//10    
    #---

    if temp == sum :
        print("Number is an Armstrong Number:",sum) 
    #---    
    a+=1    