'''
Armstrong Number
371 => 3 * power of 3 + 7 * power of 3 + 1 * power of 3 
    = 27 + 343 + 1
    = 371
'''
num = 371 
temp = num 
sum = 0
rem = num%10 #1
sum = sum + rem*rem*rem #1
num = num//10 #37

rem = num%10 #7
sum = sum + rem*rem*rem #1 + 343
num = num//10 #3

rem = num%10 #3
sum = sum + rem*rem*rem #344 + 27 = 371
num = num//10 #0

if sum == temp:
    print("Number is a Armstrong Number:",sum)
else:
    print("Number is not an Armstrong Number:",sum)    
    



