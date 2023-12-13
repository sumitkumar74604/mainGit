for _ in range(5):
    for _ in range(5):
        print("*",end=" ")
    print("")
print("----------------------------")

for row in range(5):
    for col in range(row+1):
        print("*",end="")
    print("")
print("----------------------------")

for row in range(5,0,-1):
    for col in range(5,row-1,-1):
        print(col,end="")
    print()
print("----------------------------")
#
#        5
#      45
#    345
#  2345
#12345
for row in range(5,0,-1):
    for space in range(1,row+1):
        print(" ",end="")
    for col in range(row,6):
        print(col,end="")
    print("")
print("----------------------------")

for row in range(5,0,-1):
    for col in range(row,6):
        print(col,end="")
    print("")
print("----------------------------")

i=1
for row in range(1,6):
    for col in range(1,row+1):
        print(i,end="")
        i=i+1
    print("")
print("----------------------------")    

for row in range(5,0,-1):
    for col in range(row,0,-1):
        print(col,end="")
    print("")
print("----------------------------")

for row in range(1,6):
    for space in range(5,row-1,-1):
        print(" ",end="")
    for col in range(1,row+1):
        print(col,end="")
    for col in range(1,row):
        print(col,end="")
    for space in range(5,row-1,-1):
        print(" ",end="")
    print("")
for row in range(6,0,-1):
    for space in range(5,row-1,-1):
        print(" ",end="")
    for col in range(1,row+1):
        print(col,end="")
    for col in range(1,row):
        print(col,end="")
    for space in range(5,row-1,-1):
        print(" ",end="")
    print("")
print("----------------------------")

for row in range(5,0,-1):
    for space in range(1,row):
        print(" ",end="")
    for col in range(5,row-1,-1):
        print(col,end="")
    for col in range(5,row,-1):
        print(col,end="")
    for space in range(1,row):
        print(" ",end="")
    print("")
for row in range(2,6):
    for space in range(1,row):
        print(" ",end="")
    for col in range(5,row-1,-1):
        print(col,end="")
    for col in range(5,row,-1):
        print(col,end="")
    for space in range(1,row):
        print(" ",end="")
    print("")
print("----------------------------")

for row in range(1,6):
    for col in range(5,row-1,-1):
        print(col,end="")
    print()
print("----------------------------")

for row in range(1,6):
    for col in range(row,row*2):
        print(col,end="")
    print()
print("----------------------------")

for row in range(5,0,-1):
    for col in range(1,row+1):
        print(col,end="")
    print("")
print("----------------------------")