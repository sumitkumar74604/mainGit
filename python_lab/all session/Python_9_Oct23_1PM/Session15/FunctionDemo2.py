#In Python , Functions are pass by reference
#Integer,Float,String and Tuple are immutable Objects. so a new object is created in the memory.
def sample(a):
    print(a,id(a))
    a=a+15
    print(a,id(a))
#--- 

a=12
sample(a)
print(a,id(a))
print("==================")
#List is mutable
def setList(l):
    print("list:",l,"Memory Address:",id(l))
    l.append(60)
    l.append(70)
    l.append(80)
    print("list:",l,"Memory Address:",id(l))
#-- 
l1 = [10,20,30,40,50]

setList(l1)
print("list:",l1,"Memory Address:",id(l1))
print("=============================")
def setList1(l):
    print("list1:",l,"Memory Address1:",id(l))
    l=[11,22,33,44,55]
    print("list1:",l,"Memory Address1:",id(l))
#-- 
l1 = [10,20,30,40,50]

setList1(l1)
print("list1:",l1,"Memory Address1:",id(l1))
print("=============================")

def setDic(d):
    print("Dic1:",d,"Memory Address2:",id(d))
    #d["gender"]="Male"
    d={"gender":"Male"}
    print("Dic2:",d,"Memory Address2:",id(d))
#-- 
d={"name":"Rahul Sharma","age":12,"address":"Indore M.P"}
setDic(d)
print("Dic1:",d,"Memory Address2:",id(d))

