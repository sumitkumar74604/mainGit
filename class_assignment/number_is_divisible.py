''''
Wap to calculate 1st number is divisible by 2nd number or not
'''
print("\nWap to calculate 1st number is divisible by 2nd number or not\n")

num=int(input("Enter Number 1st - \t"))
num1=int(input("Enter Number 2nd - \t"))
if num%num1==0:
    print("NUmber ",num,"is divisible by number",num1)
else:
    print("NUmber ",num,"isn't divisible by number",num1)