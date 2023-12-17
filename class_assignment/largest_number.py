'''
Wap to calculate largest number out of given four digit number 
'''

print("\nWap to calculate largest number out of given four digit number \n")

num1=int(input("Enter 1st Number -\t"))
num2=int(input("Enter 2nd Number -\t"))
num3=int(input("Enter 3rd Number -\t"))
num4=int(input("Enter 4th Number -\t"))
if num1>num2 and num1>num3 and num1>num4:
    print(" Number 1st is lagest then other",num1)
elif num2>num3 and num2>num4:
    print(" Number 2nd is lagest then other",num2)
elif num3>num4:
    print(" Number 3nd is lagest then other",num3)
else:
    print(" Number 4th is lagest then other",num4)