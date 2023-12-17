'''
Exception Handling:
1.  multiple exception:=> single try multiple except block
'''
print("--------Before Exception-----------")
l1 = [10,20,30,40]
dic = {"name":"Rahul","age":22}
try:
    print("l1[2] is:",l1[2])
    print("Age:",dic["age"])
    import math1
    print("Module imported Successfully")
except Exception as e:
    print("Exception Occur:",e)      
print("--------After Exception------------")

