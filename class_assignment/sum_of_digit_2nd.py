'''
Wap to sum of digit :---
'''

print("\nWap to sum of digit :---\n")
num=int(input("Enter Last Digit : -"))
sum=0
for i in range (1,num+1):
    print([i]," - ")
    digit=int(input("Enter Digit  - \t"))
    sum=sum+i
print("Sum of Digit - ",sum)