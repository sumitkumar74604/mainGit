'''
Basic list student_record 
'''
'''stud_record = [11,22,33,44,55,90]
print("student record")
print(stud_record)
'''

'''Basic list  student record input by user '''
print("---------- input record----------")
stud_record=[]
n=int(input("input last student record  - "))
for i in range(n):
    print(i,"name -",end=" ")
    name=(input())
    print(i,"age -",end=" ")
    age=int(input())
    stud_record.append(name)
    stud_record.append(age)
    #stud_record=[student]
print("---------student record - -------------")
for index in range (len(stud_record)):
    print(index," - ",stud_record[index]) 