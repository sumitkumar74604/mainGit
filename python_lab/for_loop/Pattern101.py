'''
1010101
0101010
1010101
0101010
1010101
0101010
1010101
'''

for row in range(1,8):
    if row%2==0:
        for col in range(1,8):
            if col%2==0:
                print("1",end="")
            else:
                print("0",end="")
    else:
        for col in range(1,8):
            if col%2==0:
                print("0",end="")
            else:
                print("1",end="")
    print("")

