'''
Wap that accept in number from user and calculate Maximum and minimum Value:- 
'''

print("\n Wap that accept in number from user and calculate Maximum and minimum Value:- \n")

num=int(input("Enter Number - \t"))
greater=0
min=0
while num!=0:
    remain=num%10
    if remain>=greater:
        greater=remain
    if remain<=greater:
        min=remain
    num=num//10
print(" Maximum - \t",greater)
print(" Minimum - \t",min)
    