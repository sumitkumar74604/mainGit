'''
Tuple:It is a sequence which is used to store bulk amount of heterogenous data , where each data is given by index value used to access and handle data.
Note: Tuple is immutable in nature
Syntax:
tup_name = (e1,e2,....en)
'''
# stud_marks = (56,)
# print(stud_marks)
# print("Type is:",type(stud_marks))

stud_record = ("Neha Sharma",23232,"BCA",34567.454)
print(stud_record)
print("Type is:",type(stud_record))

#access single data
print(stud_record[0])
print("========data without index================")
#access all data
for data in stud_record:
    print(data)
print("==========data with index==============")
for x in range(len(stud_record)):
    print("Index:",x," Value:",stud_record[x])
print("==========data with index==============")

#convert tuple into list
newrecord = list(stud_record)
newrecord[3]=45674.45
newrecord.append((56,67,78,89,90))
print(newrecord)

#convert list into tuple
stud_record = tuple(newrecord)
print(stud_record)
print(stud_record[4][0])

for m in range(len(stud_record[4])):
    print(stud_record[4][m])
print("-----------------")

#list of tuple
t1 = (101,"Raj Sharma",23000.0,"iOS Developer")
t2 = (102,"Vijay Kumar",43000.0,"React Native Developer")
t3 = (103,"Gopal Sharma",34000.0,"MERN FULL Stack Developer")
t4 = (104,"Mukesh Verma",28000.0,"HR")
t5 = (105,"Priya Sharma",33000.0,"Python Django Developer")

#t1[2]=56566.676
#TypeError: 'tuple' object does not support item assignment

list_emp = []
list_emp.append(t1)
list_emp.append(t2)
list_emp.append(t3)
list_emp.append(t4)
list_emp.append(t5)
print(list_emp)

print("*********** Details ***************")

for tuple in list_emp:
    print(tuple[0],tuple[1],tuple[2],tuple[3])
print("----------")
l1 = []
for _ in range(2):
    name=input("Enter a name\n")
    age=int(input("Enter a age\n"))
    address=input("Enter a address\n")
    tup = (name,age,address)
    l1.append(tup)
#---
print(l1)    