'''
Loop:repitation of code.
'''
#while loop
#print hello world five times

a=1
while a<=5:
    print("Hello World:",a)
    a+=1
print("==================") 
while a>1:
    a-=1
    print("Hii:",a)
print("==================") 
#print sum of square of number from 1 to 5
b=1
sum=0
while b<=5:
      #sum+=b*b
      sum = sum + b*b    
      b+=1
print("Sum is:",sum)      
print("==================") 
#print table of any number
# 5x1=5...5x10=50
a=1
t=25
while a<=10:
     print(t,"x",a,"=",t*a)     
     a+=1
print("==================") 
#find factorial of a number
# 5! = 5x4x3x2x1
n=5
f=1
while n>=1:
      f*=n        
      n-=1
print("Factorial is :",f)      
print("==================") 
#Check if a number is a perfect number or not.
n=28
s=1
sum=0
while s<n:
     if n%s==0:
        # print("Factors is:",s)
        sum+=s  
     s+=1
if sum == n :
   print("Number is a perfect number:",sum)
else:
   print("Number is not a perfect number:",sum)
