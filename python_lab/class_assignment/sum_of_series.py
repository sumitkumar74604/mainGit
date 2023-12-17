'''
Wap to calculate Sum of Series  ( 1/1+1/2+1/3+1/4+.....1/n)
'''

print("\n Wap to calculate Sum of Series  ( 1/1+1/2+1/3+1/4+.....1/n)\n")
num=1
sum=0
divide_sum=0
last_digit=int(input("Enter Last Value (n) - \t"))
for i in range (1,last_digit+1):
    sum=1/i
    divide_sum=divide_sum+sum
    print([i]," sum - \t",sum)
print("Divide Sum - \t",divide_sum)