#list of dictionary
print("enter last digit - ",end="")
num=int(input())
personlist = []
for _ in range(num):
    name = input("Enter a name\n")
    age = int(input("Enter a age\n"))
    address = input("Enter a address\n")
    dic = {}
    dic["name"]=name
    dic["age"]=age
    dic["address"]=address
    personlist.append(dic)   
#print(personlist)
for index in range(len(personlist)):
     dic = personlist[index]
     #access multiple record
     for key in dic:
          print("Key is:",key," Value is:",dic[key])
     print("=========================")