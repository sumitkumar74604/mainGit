'''
Wap to calculate to entered number is perfect or not (sum of factorial a number like 6)
'''

print("\nWap to calculate to entered number is perfect or not (sum of factorial a number like 6)\n")

def prefect(digit):
    temp=digit
    sum=0
    for i in range (1,digit):
        if (digit%i==0):
            sum=sum+i
    print(" Sum = ",sum)
        
    if temp==sum:
        print(" Number is prefect - ",digit)
    else:
        print(" Number isn't prefect - ",digit)
    
digit=int(input("Enter Digit or number - \t"))
prefect(digit)
