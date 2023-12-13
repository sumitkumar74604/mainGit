n=int(input("number - "))
num=n
sum=0
count =0
while n!=0:
    count+=1
    n=n//10
print("power - ",count)
while num!=0:
    remain=num%10
    sum=sum+remain**count
    num=num//10
print("sum - ",sum)
