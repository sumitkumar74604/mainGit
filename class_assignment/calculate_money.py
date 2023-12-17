'''
A cashier has some amount of money ( e.g - 4526).
WAP to calculate out how many currency of 2000 , 1000 , 
500 , 100 , 50 , 20 , 10 , 5
'''
print("\nA cashier has some amount of money ( e.g - 4526),WAP to calculate out how many ,currency of 2000 , 1000 ,500 , 100 , 50 , 20 , 10 , 5 \n")
cash=int(input("Enter cash - \t"))
Two_Thousand=cash//2000
cash=cash%2000
One_Thousand=cash//1000
cash=cash%1000
Five_hundred=cash//500
cash=cash%500
One_Hundred=cash//100
cash=cash%100
Fifty=cash//50
cash=cash%50
Twenty=cash//20
cash=cash%20
Ten=cash//10
cash=cash%10
Five=cash//5
cash=cash%5

print("2000 - \t",Two_Thousand)
print("1000 - \t",One_Thousand)
print("500 - \t",Five_hundred)
print("100 - \t",One_Hundred)
print("50 - \t",Fifty)
print("20 - \t",Twenty)
print("10 - \t",Ten)
print("5 - \t",Five)








