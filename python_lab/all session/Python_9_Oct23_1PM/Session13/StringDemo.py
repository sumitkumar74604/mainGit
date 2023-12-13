'''
String : It is a sequence capable to store multiple characters,numbers,aplhanumeric data , each element will be given by numeral index value which is used to store and manage string data.
Note: String is immutable in nature.
'''

s="r  a  h  u  l"
#  0  1  2  3  4     +ve index:
# -5 -4 -3 -2 -1

print(s)
print("Type is:",type(s))
print("------------------")
#concatenation (+)

fname = "videh"
lname = "jaiswal"
fullname = fname+" "+lname
print("Name is:",fullname)
print("-----------------")
#multiplier
name = "neha "
n=3
r=name*n
print(r)
print("-----------------")

#membership operator in, not in
s="rahul"
s1="h"
r = s1 in s
print(r)
print("-----------------")
r = s1 not in s
print(r)
print("-----------------")

#s1,s2,s3 = "red","green","blue"
s1,s2,s3 = "rahul","raj","rakesh"
print(s1)
print(s2)
print(s3)
print("Max Value:",max(s1,s2,s3))
print("Min Value:",min(s1,s2,s3))

print("Length of String:",len(s1))
s1 = "rahul"
#access all characters
for i in range(len(s1)):
    print("index:",i,"Character:",s1[i])
print("----------------")

#method of case conversion
s1="rahul sharma"
print("Upper Case String:",s1.upper())
print("Lower Case String:",s1.lower())
print("Capitalize Case String:",s1.capitalize())
print("Title Case String:",s1.title())
print("----------------")

#method of case checking
s1 = " "
print("Is UpperCase is:",s1.isupper())
print("Is LowerCase is:",s1.islower())
print("Is Title Case is:",s1.istitle())
print("Is Numeric Case is:",s1.isnumeric())
print("Is Alpha Case is:",s1.isalpha())
print("Is AlphaNumeric Case is:",s1.isalnum())
print("Is Space Case is:",s1.isspace())
print("------------------")
#slice(start,stop,step)

str1 = "rahul sharma"
obj = slice(3)
newstr = str1[obj]
print(newstr)
obj = slice(3,10)
newstr = str1[obj]
print(newstr)
obj = slice(3,10,2)
newstr = str1[obj]
print(newstr)
print("------------------")
obj = slice(-6,-2,2)
newstr = str1[obj]
print(newstr)
print("------------------")

