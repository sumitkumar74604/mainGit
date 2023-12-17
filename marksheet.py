'''Q.4 Write a program accept 5 subject marks (Hint P=67,C=87,M=90,H=98,E=88) and calculate total
marks and percentage.'''

print("\n Q.4 Write a program accept 5 subject marks (Hint P=67,C=87,M=90,H=98,E=88) and calculate total marks and percentage.\n")
h =  int(input("enter Hindi Marks = "))
e =  int(input("enter English Marks = "))
m =  int(input("enter Math Marks = "))
sst =  int(input("enter S S T Marks = "))
sci =  int(input("enter Science Marks = "))
total = h+e+m+sst+sci
per = total/5
print("Total Marks = ",total)
print("Total Percentage = ",per)
