'''Q.3 Write a program to find out simple interest (SI).'''
print("\nQ.3 Write a program to find out simple interest (SI).\n")
p =  int(input("enter  principal amount = "))
r =  float(input("enter Rate = "))
t =  int(input("enter ternue = ")) 
si=(p*r*t)/100
#si=int(si)
total=p+si
print(" Simple Interest = ",si)
print(" Total amount payable = ",total)
