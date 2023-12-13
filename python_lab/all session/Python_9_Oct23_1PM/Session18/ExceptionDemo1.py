'''
Exception:It is a runtime error, when it occurs program terminates.
Types of Exception:
1.NameError
2.ZeroDivisionError
3.IndexError
4.KeyError
5.ValueError
6.TypeError
7.ModuleNotFoundError
8.FileNotFoundError
'''
#ZeroDivisionError
# print("--------Before Exception-----------")
# a=10
# b=0
# print("result is:",a/b)
# print("--------After Exception------------")

#IndexError: list index out of range
# print("--------Before Exception-----------")
# l1 = [10,20,30,40]
# print("l1[12] is:",l1[12])
# print("--------After Exception------------")

#KeyError: 'address'
# print("--------Before Exception-----------")
# dic = {"name":"Neha Sharma","age":23}
# print("Address is:",dic["address"])
# print("--------After Exception------------")

#ValueError: invalid literal for int() with base 10: 'Male'
# print("--------Before Exception-----------")
# gender="Male"
# gender=int(gender)
# print(gender)
# print("--------After Exception------------")


# print("--------Before Exception-----------")
# def personDetails(name,age,address):
#     print("Name is:",name)
#     print("Age is:",age)
#     print("Address is:",address)
# #personDetails("Mukesh Sharma",12,"Indore M.P") 
# personDetails(12,"Indore M.P")    
# #TypeError: personDetails() missing 1 required positional argument: 'address'    
# print("--------After Exception------------")

#FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'
print("--------Before Exception-----------")
fo=open("data.txt","r")
strdata = fo.read()
print("--------After Exception------------")
