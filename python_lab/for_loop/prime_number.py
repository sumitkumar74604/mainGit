'''
wap to print prime no.
'''
count=0
lower=int(input("enter start digit - "))
upper=int(input("enter end digit number - "))
print("prime numbers are :- ")
for i in range(lower,upper):
    if i>2:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            count+=1
            print(i)
print(" total prime count - ",count)