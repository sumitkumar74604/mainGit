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

#-----------
#Ass3:
dic_state = {
    "Madhya Pradesh":["Indore","Ujjain","Bhopal"],
    "Rajasthan":["Jaipur","Jodhpur","Udaipur"],
    "Gujarat":["Ahemdabad","Baroda","Surat"]
}
for state in dic_state:
    print(state,":",end=" ")
    for listofCity in dic_state[state]:
        print(listofCity,end=" ")
    print()
print("=========================================")    
#----------
#dictionary of dictionary
stud_record = {
    "name":"Rahul Verma",
    "rollno":121,
    "course":"BCA",
    "address":{
        "country":"India",
        "state":"M.P",
        "city":"Indore",
        "pincode":452001,
        "location":{
            "lat":22.7196,
            "long":75.8577
        }
    }
}

print("Name:",stud_record["name"])
print("Rollno:",stud_record["rollno"])
print("Course:",stud_record["course"])
print("Country:",stud_record["address"]["country"])
print("State:",stud_record["address"]["state"])
print("City:",stud_record["address"]["city"])
print("Pincode:",stud_record["address"]["pincode"])
print("Latitude:",stud_record["address"]["location"]["lat"])
print("Longitude:",stud_record["address"]["location"]["long"])




users = [
  {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
      "name": "Romaguera-Crona",
      "catchPhrase": "Multi-layered client-server neural-net",
      "bs": "harness real-time e-markets"
    }
  },
  {
    "id": 2,
    "name": "Ervin Howell",
    "username": "Antonette",
    "email": "Shanna@melissa.tv",
    "address": {
      "street": "Victor Plains",
      "suite": "Suite 879",
      "city": "Wisokyburgh",
      "zipcode": "90566-7771",
      "geo": {
        "lat": "-43.9509",
        "lng": "-34.4618"
      }
    },
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net",
    "company": {
      "name": "Deckow-Crist",
      "catchPhrase": "Proactive didactic contingency",
      "bs": "synergize scalable supply-chains"
    }
  },
  {
    "id": 3,
    "name": "Clementine Bauch",
    "username": "Samantha",
    "email": "Nathan@yesenia.net",
    "address": {
      "street": "Douglas Extension",
      "suite": "Suite 847",
      "city": "McKenziehaven",
      "zipcode": "59590-4157",
      "geo": {
        "lat": "-68.6102",
        "lng": "-47.0653"
      }
    },
    "phone": "1-463-123-4447",
    "website": "ramiro.info",
    "company": {
      "name": "Romaguera-Jacobson",
      "catchPhrase": "Face to face bifurcated interface",
      "bs": "e-enable strategic applications"
    }
  },
  {
    "id": 4,
    "name": "Patricia Lebsack",
    "username": "Karianne",
    "email": "Julianne.OConner@kory.org",
    "address": {
      "street": "Hoeger Mall",
      "suite": "Apt. 692",
      "city": "South Elvis",
      "zipcode": "53919-4257",
      "geo": {
        "lat": "29.4572",
        "lng": "-164.2990"
      }
    },
    "phone": "493-170-9623 x156",
    "website": "kale.biz",
    "company": {
      "name": "Robel-Corkery",
      "catchPhrase": "Multi-tiered zero tolerance productivity",
      "bs": "transition cutting-edge web services"
    }
  },
  {
    "id": 5,
    "name": "Chelsey Dietrich",
    "username": "Kamren",
    "email": "Lucio_Hettinger@annie.ca",
    "address": {
      "street": "Skiles Walks",
      "suite": "Suite 351",
      "city": "Roscoeview",
      "zipcode": "33263",
      "geo": {
        "lat": "-31.8129",
        "lng": "62.5342"
      }
    },
    "phone": "(254)954-1289",
    "website": "demarco.info",
    "company": {
      "name": "Keebler LLC",
      "catchPhrase": "User-centric fault-tolerant solution",
      "bs": "revolutionize end-to-end systems"
    }
  },
  {
    "id": 6,
    "name": "Mrs. Dennis Schulist",
    "username": "Leopoldo_Corkery",
    "email": "Karley_Dach@jasper.info",
    "address": {
      "street": "Norberto Crossing",
      "suite": "Apt. 950",
      "city": "South Christy",
      "zipcode": "23505-1337",
      "geo": {
        "lat": "-71.4197",
        "lng": "71.7478"
      }
    },
    "phone": "1-477-935-8478 x6430",
    "website": "ola.org",
    "company": {
      "name": "Considine-Lockman",
      "catchPhrase": "Synchronised bottom-line interface",
      "bs": "e-enable innovative applications"
    }
  },
  {
    "id": 7,
    "name": "Kurtis Weissnat",
    "username": "Elwyn.Skiles",
    "email": "Telly.Hoeger@billy.biz",
    "address": {
      "street": "Rex Trail",
      "suite": "Suite 280",
      "city": "Howemouth",
      "zipcode": "58804-1099",
      "geo": {
        "lat": "24.8918",
        "lng": "21.8984"
      }
    },
    "phone": "210.067.6132",
    "website": "elvis.io",
    "company": {
      "name": "Johns Group",
      "catchPhrase": "Configurable multimedia task-force",
      "bs": "generate enterprise e-tailers"
    }
  },
  {
    "id": 8,
    "name": "Nicholas Runolfsdottir V",
    "username": "Maxime_Nienow",
    "email": "Sherwood@rosamond.me",
    "address": {
      "street": "Ellsworth Summit",
      "suite": "Suite 729",
      "city": "Aliyaview",
      "zipcode": "45169",
      "geo": {
        "lat": "-14.3990",
        "lng": "-120.7677"
      }
    },
    "phone": "586.493.6943 x140",
    "website": "jacynthe.com",
    "company": {
      "name": "Abernathy Group",
      "catchPhrase": "Implemented secondary concept",
      "bs": "e-enable extensible e-tailers"
    }
  },
  {
    "id": 9,
    "name": "Glenna Reichert",
    "username": "Delphine",
    "email": "Chaim_McDermott@dana.io",
    "address": {
      "street": "Dayna Park",
      "suite": "Suite 449",
      "city": "Bartholomebury",
      "zipcode": "76495-3109",
      "geo": {
        "lat": "24.6463",
        "lng": "-168.8889"
      }
    },
    "phone": "(775)976-6794 x41206",
    "website": "conrad.com",
    "company": {
      "name": "Yost and Sons",
      "catchPhrase": "Switchable contextually-based project",
      "bs": "aggregate real-time technologies"
    }
  },
  {
    "id": 10,
    "name": "Clementina DuBuque",
    "username": "Moriah.Stanton",
    "email": "Rey.Padberg@karina.biz",
    "address": {
      "street": "Kattie Turnpike",
      "suite": "Suite 198",
      "city": "Lebsackbury",
      "zipcode": "31428-2261",
      "geo": {
        "lat": "-38.2386",
        "lng": "57.2232"
      }
    },
    "phone": "024-648-3804",
    "website": "ambrose.net",
    "company": {
      "name": "Hoeger LLC",
      "catchPhrase": "Centralized empowering task-force",
      "bs": "target end-to-end models"
    }
  }
]