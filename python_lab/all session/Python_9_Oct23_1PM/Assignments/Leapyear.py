# Q.11 Write a program to calculate whether year is leap year or not.
#There is a leap year every year whose number is perfectly divisible by four - except for years which are both divisible by 100 and not divisible by 400. The second part of the rule effects century years. For example; the century years 1600 and 2000 are leap years, but the century years 1700, 1800, and 1900 are not. 

year=int(input("Enter a year"))
if year%100==0 and year%400!=0:
    print("Divide by 100 and not divide by 400")
    print("Year is not a leap year") 
elif year%400==0:
    print("Divide by 400")
    print("Year is a leap year")    
elif year%4==0:
    print("Divide by 4")
    print("Year is a leap year")    
else:
    print("Year is not a leap year")