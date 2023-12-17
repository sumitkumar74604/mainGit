'''
Wap to accept n number from user and show how many number are Even or Odd
'''
print("\nWap to accept n number from user and show how many number are Even or Odd\n")

num=int(input("Enter last digit - \t"))
a=1
while a<=num:
    if a%2==0:
        print("\t\tEven - ",a,"\t")
    else:
        print("odd - ",a)
    a+=1
  