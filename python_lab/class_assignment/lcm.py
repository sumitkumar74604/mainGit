'''
wap to find LCM of Two Number :-
'''

print("\nwap to find LCM of Two Number :-\n")
n1=12  # 1 2 3 4 6 12
n2=16  # 1 2 4 8 16
if n1>n2:
    max=n1
else:
    max=n2
while True:
    if max%n1==0 and max%n2==0:
        print("L.C.M - ",max)
        break
    print(" Max - ",max)
    max+=1