'''
TwoDList([row][col]) : It is a collection of OneD List.
'''
'''
r1 = [10,20,30]
r2 = [40,50,60]
r3 = [70,80,90]
twoDList = [r1,r2,r3]
print(twoDList)
#access single record 
print(twoDList[1][1])
print(twoDList[0][2])
print(twoDList[2][0])
#access all list
for row in range(len(twoDList)):
    #print(twoDList[row])
    for col in range(len(twoDList[row])):
        print("twoDList[",row,"][",col,"]:",twoDList[row][col])
'''

'''
    row=[1 2 3]        row=[6 5 4]          [0 0 0]
a1= col=[4 5 6]    b1= col=[3 2 1]      c1= [0 0 0]
'''
# 3*3-- Matrix
#                   0 1 2 --- i
x=[[1,2,3],      #0[1 2 3]
   [3,4,5],      #1[3 4 5]
   [5,6,7]]      #2[5 6 7]
# 3*3 --- Matrix
#                   0 1 2 --- i
y=[[1,2,3],      #0[1 2 3]
   [3,4,5],      #1[3 4 5]
   [5,6,7]]      #2[5 6 7]

#                   0 1 2 --- i
z=[[0,0,0],      #0[1 6 15]
   [0,0,0],      #1[]
   [0,0,0]]      #2[]

for i in range(0,3): # row for x
    for j in range(0,3): # col for y
        for k in range(0,3): # row for y
            z[i][j]=z[i][j] + x[i][k] * y[k][j]
    
for result in z:
    print (result)