'''
File Handling:It is a storage capable to store bulk amount of data simulteneously at particular location.This storage is permanent in nature.i.e once created they can also be accessed and managed manually.
predefined function:
obj = open("file location","mode")

File Mode:
1.write(w):
It checks if file exists or not.If not, created a new file and content can be written.but if file is exists, then it will override file content.
================
2.append(a):It checks if file exists or not.If not, created a new file and content can be written.but if file is exists, then it will add a new content.
================
3.read(r):It checks if file exists or not.If not,it will result in error.If exists, then it will read a file content
================
'''
fo = open("test.txt","r")
print("File Position 1 at:",fo.tell())
data = fo.read(10)
print(data)
print("File Position 2 at:",fo.tell())
data = fo.read(10)
print(data)
print("File Position 3 at:",fo.tell())
print("File Position 2 at:",fo.tell())
