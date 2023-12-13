'''
   c1c2c3c4c5
 r1 * * * * * 
 r2 * * * * *
 r3 * * * * *
 r4 * * * * *
 r5 * * * * *

 r  c
 0  0
    1
    2
    3
    4 
 1  0
    1
    2
    3
    4     

'''

for _ in range(5): #row
    for _ in range(5): #col
        print("*",end=" ")
    print()    
print("-------------------")

'''
*
**
***
****
*****
'''
for row in range(5): #row
    for col in range(row+1): #col
        print("*",end="")
    print()    
print("-------------------")

'''
$$$$*
$$$**
$$***
$****
*****    
'''

for row in range(5,0,-1):
    #space
    for space in range(0,row-1):
        print(" ",end="")
    #star content
    for col in range(row-1,5):
        print("*",end="")     
    print()    
print("-------------------")

'''
    *
   ***
  *****
 *******
*********    
'''
for row in range(5,0,-1):
    #space
    for space in range(0,row-1):
        print(" ",end="")
    #star content
    for col in range(row-1,5):
        print("*",end="")
    #star content    
    for col in range(row-1,4):
        print("*",end="")         
    print() 
print("-------------------")
'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    * 
'''
for row in range(5,0,-1):
    #space
    for space in range(0,row-1):
        print(" ",end="")
    #star content
    for col in range(row-1,5):
        print("*",end="")
    #star content    
    for col in range(row-1,4):
        print("*",end="")         
    print() 
for row in range(2,6):
    #space
    for space in range(0,row-1):
        print(" ",end="")
    #star content
    for col in range(row-1,5):
        print("*",end="")
    #star content    
    for col in range(row-1,4):
        print("*",end="")         
    print()     
print("-------------------")

'''
5
54
543
5432
54321

r c 


'''

for row in range(5,0,-1):
                     #(5,4,-1)# 5
                     #(5,3,-1)# 54
                     #(5,2,-1)# 543
                     #(5,1,-1)# 5432
                     #(5,0,-1)# 54321      
    for col in range(5,row-1,-1):
        print(col,end="")
    print()
        
print("-----------")


'''
    5
   545
  54345
 5432345
543212345
 5432345
  54345
   545
    5  


54321
5432
543
54
5

    5
   45
  345
 2345
12345

1
23
345
4567
56789

12345
1234
123
12
1

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

'''