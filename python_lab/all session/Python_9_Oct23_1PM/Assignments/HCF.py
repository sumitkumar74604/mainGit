'''
HCF:
12:1,2,3,4,6,12
16:1,2,4,8,16
4
'''

n1 = 12
n2 = 16
a = 1
hcf = 0
while a<=n2:
    if n1%a == 0 and n2%a == 0:
       hcf = a 
    a+=1
print("H.C.F is :",hcf)       