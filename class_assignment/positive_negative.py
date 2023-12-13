'''
Wap that accept a three digit number from user and calculate whether it is positibe 
negative or Zero
'''
print("\nWap that accept a three digit number from user and calculate whether it is positibe negative or Zero\n")

num=int(input("Enter Digit - \t"))
if num >0:
    print("Number is positive ",num)
elif num<0:
    print("Number is Negative ",num)
else:
    print("Number Is Zero ",num)