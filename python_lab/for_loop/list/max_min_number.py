'''
find max and min number in given data 
'''
print("---------------- Static ---------")
stud_marks = [56,34,78,66,89,45]
max = stud_marks[0]
min = stud_marks[0]
for x in range(len(stud_marks)):

    if max < stud_marks[x]:
        max = stud_marks[x]
    elif min > stud_marks[x]:
        min = stud_marks[x]
print("Max is :",max,"Min is:",min)
#--------            
print("------------- dynamic ---------")

print("enter last digit input data - ")
num=int(input("--- "))
list = []
for i in range (num):
    print(i,"input - ",end="")
    x=int(input(""))
    list.append(x)
max = list[0]
min = list[0]
for x in range(len(list)):
    if max<list[x]:
        max=list[x]
    elif min>list[x]:
        min=list[x]
print(" your input ",list)
print("max - ",max)
print("min - ",min)