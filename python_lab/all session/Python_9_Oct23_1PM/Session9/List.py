'''
List:
'''

stud_marks = [55,67,78,89,90]
print("Type is:",type(stud_marks))
print(stud_marks)

#access single record
print("+ve index:",stud_marks[2])
print("-ve index:",stud_marks[-2])

#length of list
print("Length is:",len(stud_marks))
print("=====================================")
#store data of different type
empdetails = ["Videh Jaiswal",101,34567.343,"IT"]

#access single record
print("+ve index:",empdetails[2])
print("-ve index:",empdetails[-3])
print("=====================================")

#access all data
for a in range(len(empdetails)):
    print("Index:",a," Data:",empdetails[a])
print("=====================================")

#access all data
for a in range(len(stud_marks)):
    print("Index:",a," Data:",stud_marks[a])
print("=====================================")

