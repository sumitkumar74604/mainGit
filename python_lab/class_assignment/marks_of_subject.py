'''
Wap that accept marks of four subject from user and calculate the total 
mark and persentage out of 500 
'''
print("\nWap that accept marks of four subject from user and calculate the total mark and persentage out of 500\n")
eng=int(input("Enter English Marks - \t\t"))
while eng >100 or eng<0:
    eng=int(input("Enter valid English Marks in 1 - 100 - \t"))
    
hin=int(input("Enter Hindi Marks - \t\t"))
while hin >100 or hin<0:
    hin=int(input("Enter valid Hindi Marks in 1 - 100 - \t"))

sst=int(input("Enter Social Science Marks - \t"))
while sst >100 or sst <0:
    sst=int(input("Enter valid Social Science Marks in 1 - 100 - \t"))

sci=int(input("Enter Science Marks - \t\t"))
while sci >100 or sci <0:
    sci=int(input("Enter valid  Science Marks in 1 - 100 - \t"))

math=int(input("Enter Math Marks - \t\t"))
while math >100 or math <0:
    math=int(input("Enter valid Math Marks in 1 - 100 - \t"))
    
sum=eng+hin+math+sst+sci
per=sum/5
print("Sum of Subject - \t\t",sum)
print("Percentage  of Subject - \t\t",per,"%")