'''
Exception Handling:
1. try-except block
'''
print("--------Before Exception-----------")
l1 = [10,20,30,40]
try:
    print("l1[12] is:",l1[12])
except IndexError as e:
    print("Exception Occur:",e)
print("--------After Exception------------")

