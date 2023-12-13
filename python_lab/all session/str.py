str="The quick fox jumped over the lazy dog"
countv=0
counts=0
for s in str:
    if s=="a" or s=="e" or s=="i" or s=="o" or s=="u":
        countv+=1
        print(countv)
    if s.isspace()==1:
        counts+=1
str=str.title()

print("the numbers of vowels are:",countv)
print("the numbers of spaces are:",counts)
print(str)
print("the length of string is:",len(str))