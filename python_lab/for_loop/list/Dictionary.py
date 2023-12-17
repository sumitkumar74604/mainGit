'''
Dictionary: It is a sequence which is used to store heterogenous data reference, where each data will be given by a key-value pair.
Syntax:

dic = { key:value,key1:value....,keyn:value }

key must be unqiue.
key is immutable and value is mutable.

'''

person_dic = {"name":"Rohit Soni","age":23,"address":"Indore M.P"}
print(person_dic)
print("Type is:",type(person_dic))

#access single record
print("Name is:",person_dic["name"])
print("Age is:",person_dic.get("age"))

print("=================================")
#access multiple record
for key in person_dic:
    print("Key is:",key," Value is:",person_dic[key])

print("===============keys==================")
for key in person_dic.keys():
    print(key)
print("===============values==================")
for val in person_dic.values():
    print(val)
print("===============tuple==================")
# for tup in person_dic.items():
#     print(tup)   
#     print(tup[0],tup[1]) 
for (k,v) in person_dic.items():
    print(k,v)        
print("=========================")
#update
person_dic["age"]=25
#access multiple record
for key in person_dic:
    print("Key is:",key," Value is:",person_dic[key])
print("=========================")

#remove
#person_dic.pop("address")
#access multiple record
# for key in person_dic:
#     print("Key is:",key," Value is:",person_dic[key])
# print("=========================")

#remove last key-value pair
#tup = person_dic.popitem()
#print(tup)
#access multiple record
# for key in person_dic:
#     print("Key is:",key," Value is:",person_dic[key])
# print("=========================")

#list of dictionary
# personlist = []
# for _ in range(3):
#     name = input("Enter a name\n")
#     age = int(input("Enter a age\n"))
#     address = input("Enter a address\n")
#     dic = {}
#     dic["name"]=name
#     dic["age"]=age
#     dic["address"]=address
#     personlist.append(dic)
#---    
# print(personlist)
# for index in range(len(personlist)):
#     dic = personlist[index]
#     #access multiple record
#     for key in dic:
#          print("Key is:",key," Value is:",dic[key])
#     print("=========================")
#---
dic1 = {452001:"Indore",456010:"Ujjain",456335:"Nagda",455001:"Dewas"} 
print(dic1)   
print("City:",dic1[452001])
#access multiple record    
for key in dic1:
    print("Key is:",key," Value is:",dic1[key])
#----
print(person_dic)    
emp_dic = {"id":232,"salary":34567.34,"designation":"Python Django Developer"}
# newdic = person_dic+emp_dic
# print(newdic)
#TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

person_dic.update(emp_dic)
print(person_dic)
#dictionary of list
dic2 = {
    "address":["Vijay Nagar Indore","Palasia Indore","Rajwada Indore","LIG Indore"]
}

print(dic2["address"])
print("----------------")
for addr in dic2["address"]:
    print(addr)
print("-------------")    
'''
a dictionary key must be of a type that is immutable. For example, you can use an integer, float, string, or Boolean as a dictionary key. However, neither a list nor another dictionary can serve as a dictionary key, because lists and dictionaries are mutable
'''
#dic = {[]:[]}