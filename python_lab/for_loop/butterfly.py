'''
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
'''
for row in range(5,0,-1):
    for space in range(row,5):
        print(" ",end="")
    for col in range(1,row+1):
        print("*",end="")
    for col in range(1,row):
        print("*",end="")    
    print()
for row in range(2,6):
    for space in range(row,5):
        print(" ",end="")
    for col in range(1,row+1):
        print("*",end="")
    for col in range(1,row):
        print("*",end="")    
    print()            
print("-----------------") 
