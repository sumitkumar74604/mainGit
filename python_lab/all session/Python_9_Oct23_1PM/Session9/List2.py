stud_marks = [56,34,78,66,89,45]
max = stud_marks[0]
min = stud_marks[0]

for x in range(len(stud_marks)):
    if max < stud_marks[x]:
        max = stud_marks[x]
    elif min > stud_marks[x]:
        min = stud_marks[x]
#----

print("Max is :",max,"Min is:",min)            