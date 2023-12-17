'''
Wap that accept three digit number from user and find the grater digit in it
'''

print("\nWap that accept three digit number from user and find the grater digit in it\n")

num=int(input("Enter the 3 digit number - \t"))
while num>999 or num<100:
    num=int(input("Enter the 3 digit number - \t"))
greater=0
while num!=0:
    remain=num%10
    if remain>=greater:
        greater=remain
    num=num//10
print(" Greater - \t",greater)
    