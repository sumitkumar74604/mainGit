'''
Exception Handling:
1.nested try except block
'''
print("--------Before Exception-----------")
l1 = [10,20,30,40]
dic = {"name":"Rahul","age":22}
try:
    print("l1[2] is:",l1[2])
    try:
        print("address:",dic["address"])
    except KeyError as e:
        print("Exception Occur:",e)     
except Exception as e:
    print("Exception Occur:",e)      
print("--------After Exception------------")

