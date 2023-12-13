'''
Wap to calculate gross salary and net salary . Accept basic salary from user , 
TA  - 10% of basic salary , DA - 500 , PF - 7.8% of basic salary,
ns - gs-pf ,GS - basic+ta+da;
'''

print("\nWap to calculate gross salary and net salary . Accept basic salary from user ,TA  - 10% of basic salary , DA - 500 , PF - 7.8% of basic salary,ns - gs-pf ,GS - basic+ta+da;\n")

basic=float(input("Enter Basic salary - \t"))
da=500
pf=(basic*7.8)/100
ta=(basic*10)/100
gs=basic+ta+da
ns=gs-pf
print("TA - ",ta)
print("DA - ",da)
print("PF - ",pf)
print("Gross Salary - ",gs)
print("NET Salary - ",ns)
