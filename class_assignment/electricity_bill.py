'''
Wap to for generating electricity bill . Accept last month unit 
and current unit from user then , calculate Bill and print bill amout according 
following condition for unit .
0-100 chage 2rs/unit
101-200 charge 3rs/unit
201-300 4rs/unit
300 charge 5rs/unit 




print("\nWap to for generating electricity bill . Accept last month unit  and current unit from user then , calculate Bill and print bill amout according  following condition for unit .")
print("\n0-100 chage 2rs/unit,101-200 charge 3rs/unit ,201-300 4rs/unit ,300 charge 5rs/unit  \n")

c_unit=float(input("Enter Current Month Electricity Unit - \t"))
l_unit=float(input("Enter Last Month Electricity Unit - \t"))
print("-----------------------------------------------------")

if c_unit>0 and c_unit<=100:
    print("Current Month Electricity Bill - \t",c_unit*2)
elif c_unit>101 and c_unit<=200:
    print("Current Month Electricity Bill - \t",c_unit*3)
elif c_unit>201 and c_unit<=300:
    print("Current Month Electricity Bill - \t",c_unit*4)
else :
    print("Current Month Electricity Bill - \t",c_unit*5)
print("-----------------------------------------------------")
if l_unit>0 and l_unit<=100:
    print("Last Month Electricity Bill - \t",l_unit*2)
elif l_unit>101 and l_unit<=200:
    print("Last Month Electricity Bill - \t",l_unit*3)
elif l_unit>201 and l_unit<=300:
    print("Last Month Electricity Bill - \t",l_unit*4)
else :
    print("Last Month Electricity Bill - \t",l_unit*5)

'''


def electricity(unit):
    if unit>0 and unit<=100:
        #print("Current Month Electricity Bill - \t",unit*2)
        return unit*2
    elif unit>101 and unit<=200:
        #print("Current Month Electricity Bill - \t",unit*3)
        return unit*3
    elif unit>201 and unit<=300:
        return unit*4
        #print("Current Month Electricity Bill - \t",unit*4)
    else :
        return unit*5
        #print("Current Month Electricity Bill - \t",unit*5)

c_unit=float(input("Enter Current Month Electricity Unit - \t"))
l_unit=float(input("Enter Last Month Electricity Unit - \t"))
print("-----------------------------------------------------")
e1=electricity(c_unit)
print("Current Month Electricity Bill - \t",e1)
e2=electricity(l_unit)
print("Last Month Electricity Bill - \t",e2)