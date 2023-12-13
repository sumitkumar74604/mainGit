'''
Sorting: Arrange element in ascending and descending order
'''

stud_marks = [56,34,67,88,90,44]

for x in range(len(stud_marks)):
    for y in range(x+1,len(stud_marks)):
           # 56 > 34
           # [34,56,67,88,90,44]
           # First Iteration
           # 56 > 44
           # [34,44,67,88,90,56]
           # Second Iteration
           # 67 > 56
           # [34,44,56,88,90,67]
           # Third Iteration
           # 88 > 67
           # [34,44,56,67,90,88]
           # Fourth Iteration
           # 90 > 88
           # [34,44,56,67,88,90]
           # Five Iteration
           # [34,44,56,67,88,90]
           # Sixth  Iteration
        if stud_marks[x]<stud_marks[y]:
            temp = stud_marks[x]
            stud_marks[x] = stud_marks[y]
            stud_marks[y] = temp
print(stud_marks)        



