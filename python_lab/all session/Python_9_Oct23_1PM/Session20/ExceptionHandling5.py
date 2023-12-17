'''
Exception Handling:
1. try finally block
'''
print("--------Before Exception-----------")
l1 = [10,20,30,40]
dic = {"name":"Rahul","age":22}
try:
    print("l1[2] is:",l1[12])  
except IndexError as e:
    print("Exception Occur:",e)      
finally:
    print("Finally always executes")      
print("--------After Exception------------")

