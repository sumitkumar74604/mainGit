'''
Wap to calculate Sum of Series  ( 1/1+1/2+1/3+1/4+.....1/n)
'''

print("\n Wap to calculate Sum of Series  ( 1/1!+1/2!+1/3!+1/4!+.....1/n)\n")
sum=0
fact=1
divide_sum=0
last_digit=int(input("Enter Last Value (n) - \t"))
for i in range (1,last_digit+1):
    fact=fact*i
    sum=sum+(i/fact)
    print([i]," sum - \t",sum)
print(" Total sum of series - \t",sum)

