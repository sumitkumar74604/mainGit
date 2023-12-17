'''Q.9 Write a program accepts an amount in rupees (Hint Rs 4567) and find out how many currency of
Rs 2000,500,200,100,50,20,10,5,2,1'''

print("\n Q.9 Write a program accepts an amount in rupees (Hint Rs 4567) and find out how many currency of Rs 2000,500,200,100,50,20,10,5,2,1\n")
x=int(input(" enter the amount - "))
thousand = int(x/2000)
print(" 2000 - ",thousand)
x=x%2000
five = int(x/500)
print(" 500 - ",five)
x=x%500
two = int(x/200)
print(" 200 - ",two)
x=x%200
hundred = int(x/100)
print(" 100 - ",hundred)
x=x%100
fifty = int(x/50)
print(" 50 - ",fifty)
x=x%50
twenty = int(x/20)
print(" 20 - ",twenty)
x=x%20
ten = int(x/10)
print(" 10 - ",ten)
x=x%10
fives = int(x/5)
print(" 5 - ",fives)
x=x%5
twos= int(x/2)
print(" 2 - ",twos)
x=x%2
once = (x/1)
print(" 1 - ",once)






