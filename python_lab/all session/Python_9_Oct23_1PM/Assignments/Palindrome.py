'''
Palindrome number is 
121
111
'''
num = 123
temp = num
rev = 0
rem=num%10 #3
rev = rev*10+rem #3
num=num//10 #12

rem=num%10 #2
rev = rev*10+rem #3*10+2=32
num=num//10 #1

rem=num%10 #1
rev = rev*10+rem #32*10+1=321
num=num//10 #0

if rev == temp:
    print("Number is a palindrome number:",rev)
else:
    print("Number is not a palindrome number",rev)


