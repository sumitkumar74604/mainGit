'''
1. Create a dictionary to store name_of_course (key) and duration_in_month(value).
store 5 pairs by default
'''
#print dictionary
Coursedetail={"C":"2 month","C++":"1 month","javascript":"2 month","Python":"2 month","Java":"2 month"}
print(Coursedetail)

#print dictionary in detailed 
for a in Coursedetail:
    print("Course Name :",a," , ","Course Duration :",Coursedetail[a])
print("=====================================>")

'''
2. create a dictionary to store name of cricket teams according to their world rankings
'''
teamdetail={"India":"First","Australia":"Second","pakistan":"Third","South Africa":"Fourth","New zealand":"Fifth"}

#print dictionary
print(teamdetail)

#print dictionary in detailed
for a in teamdetail:
    print("team:",a," , ","World_ranking:",teamdetail[a] )

print("=====================================>")

'''
3.Create dictionary to store name of
states and 3 cities of each state
'''

statename={"Madhya pradesh":["ujjain","Bhopal","Dewas","Indore"],"Andhra Pradesh":["Chittoor","Tirupati","Visakhapatnam"],"Bihar":["Gaya","Motihari","Muzaffarpur"]}

#print dictionary
print(statename)

print("------------------------------------")
#print dictionary in detailed
for state in statename:
    print(state,":-" ,end=" ")
    for city in statename[state]: 
        print(city," ",end="")
    print()
print("------------------------------------")
for state in statename:
    print(state,":-" ,end=" ")
    print(statename[state])
print()