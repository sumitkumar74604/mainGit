'''
Wap to calculate Leap year or not?
'''

print("\nWap to calculate Leap year or not?\n")
y=int(input("Enter year -\t"))
if((y % 400 == 0) or (y % 100 != 0) and (y % 4 == 0)):
    print("Year is leap Year",y)
else:
    print("Year isn't leap Year",y) 