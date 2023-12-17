'''
Write a program to calculate sum of digits number.(Hint:-123 is a given number then o/p=6)
'''
# num = 123
# sum = 0
# rem = num%10 #3
# sum = sum + rem #3
# num = num//10 #12

# rem = num%10 #2
# sum = sum + rem #3+2=5
# num = num//10 #1

# rem = num%10 #1
# sum = sum + rem #3+2=5+1=6
# num = num//10 #0
# print("Sum is:",sum)

'''
Write a program accepts an amount in rupees (Hint Rs 4567) and find out how many currency of
Rs 2000,500,200,100,50,20,10,5,2,1
'''
amt = 5888
temp = amt
note2000 = amt//2000 #2
amt = amt % 2000 #567
print("Note2000 X ",note2000,"=",2000*note2000)

note500 = amt//500 #1
amt = amt % 500 #67
print("Note500 X ",note500,"=",500*note500)

note200 = amt//200 #0
amt = amt % 200 #67
print("Note200 X ",note200,"=",200*note200)

note100 = amt//100 #0
amt = amt % 100 #67
print("Note100 X ",note100,"=",100*note100)

note50 = amt//50 #1
amt = amt % 50 #17
print("Note50 X ",note50,"=",50*note50)

note20 = amt//20 #0
amt = amt % 20 #17
print("Note20 X ",note20,"=",20*note20)

note10 = amt//10 #1
amt = amt % 10 #7
print("Note10 X ",note10,"=",10*note10)

note5 = amt//5 #1
amt = amt % 5 #2
print("Note5 X ",note5,"=",5*note5)

note2 = amt//2 #1
amt = amt % 2 #0
print("Note2 X ",note2,"=",2*note2)

note1 = amt//1 #0
amt = amt % 1 #0
print("Note1 X ",note1,"=",1*note1)
print("Total Amount:",temp)








