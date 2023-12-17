''''
Wap to calculate sum ofsquare of natural number
'''

print("\nWap to calculate sum of square of natural number\n")
last_digit=int(input("Enter last Digit -\t"))
sum=0
for i in range (0,last_digit):
    squ=i*i
    print([i]," - "," Square - ",i*i)
    sum=sum+squ
print(" Total sum of Square - ",sum)
