cricketplayer = ["Kapil Dev","Sachin Tendulkar","Virendra Shewag","M.S Dhoni","Virat Kohli"]

#access data with index
for x in range(len(cricketplayer)):
    print("Index:",x," Player:",cricketplayer[x])
print("================================")    

#access data without index
for player in cricketplayer:
    print("Player:",player)
print("============ Add Players ====================")    

#add a new player
cricketplayer.append("Rohit Sharma")
cricketplayer.append("K.L Rahul")

#access data with index
for x in range(len(cricketplayer)):
    print("Index:",x," Player:",cricketplayer[x])
print("================================")    

#add a player at specific index
cricketplayer.insert(2,"Hardik Pandaya")
#access data with index
for x in range(len(cricketplayer)):
    print("Index:",x," Player:",cricketplayer[x])
print("================================")    

#replace player
cricketplayer[2]="Shubhman Gill"
#access data with index
for x in range(len(cricketplayer)):
    print("Index:",x," Player:",cricketplayer[x])
print("================================")    

#remove player from last index
cricketplayer.pop()
#access data with index
for x in range(len(cricketplayer)):
    print("Index:",x," Player:",cricketplayer[x])
print("================================")    

#remove player from specific index
del cricketplayer[2]
#access data with index
for x in range(len(cricketplayer)):
    print("Index:",x," Player:",cricketplayer[x])
print("================================")    

print(cricketplayer.__contains__("Parthiv Patel"))