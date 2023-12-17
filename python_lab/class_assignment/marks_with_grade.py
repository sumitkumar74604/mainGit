'''
Wap to that accept marks (out of 100) of five subject from user 
and calculate the sum then calculate percentage % ? Display massage
according to following condition % >= 60 Grade A
'''

print("\n'''Wap to that accept marks (out of 100) of five subject from user and calculate the sum then calculate percentage % ? Display massage according to following condition % >= 60 Grade A '''\n")

hin=int(input("Enter Hindi Marks -\t"))
while hin>100 or hin<0:
    hin=int(input("Enter Hindi Marks Between 1 - 100  -\t"))
    
eng=int(input("Enter English Marks -\t"))
while eng>100 or eng<0:
    eng=int(input("Enter English  Marks Betwwen 1-100 -"))
    
math=int(input("Enter Math Marks -\t"))
while math>100 or math<0:
    math=int(input("Enter Math Marks Between 1-100 -"))
    
sst=int(input("Enter Social Science Marks -\t"))
while sst>100 or sst<0:
    sst=int(input("Enter Social Science Marks Between 1-100 -"))

sci=int(input("Enter Science Marks -"))
while sci>100 or sci<0:
    sci=int(input("Enter Science Marks Between 1-100 -"))
    
sum=hin+eng+math+sst+sci
per=sum/5
print("Total Marks - ",sum,"\t","Percentage - ",per,"%")
if per>=60:
    print("Grade - A")
elif per>=50 :
    print("Grade - B")
elif per>=40:
    print("Grade - C")
else:
    print("Grade - D")