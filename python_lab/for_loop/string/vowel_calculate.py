'''
In a given long string - The quick
fox jumped over the lazy dog
a. Calculate the number of vowels
(a,e,i,o,u)

'''
str="The quick fox jumped over the lazy dog"
print("------------ String Print ----------")
print(str)
print("------------ Vowel Print ----------")
count=0
for i in range (len(str)):
    char=str[i]
    if char=='a'and'A':
        count+=1
        print(char," ",end="")
    elif char == 'e'and'E':
        count+=1
        print(char," ",end="")
    elif char == 'i'and'I':
        count+=1
        print(char," ",end="")
    elif char == 'o'and'O':
        print(char," ",end="")
        count+=1
    elif char == 'u'and'U':
        print(char," ",end="")
        count+=1
print("\n---- Total No. Of Vowel are :-\n")
print("vowel :-" ,count)
print()




'''
1.b. Calculate the number of white spaces

'''
print("b. Calculate the number of white spaces")
count=0
for i in range (len(str)):
    char=str[i]
    for space in char:
        if space==" ":
            count+=1
print(" ---------------Space print --------------------")
print("Space Count :- ",count)
print("*******************************************")



'''
c. Generate a new string where 1st letter of each word is in caps.
'''
print("c. Generate a new string where 1st letter of each word is in caps.")
print("---------------------------------------------------------------------")
print("output str :-",str.title())
print("---------------------------------------------------------------------")
print("*********************************************************************") 
print("d. Calculate the length of the string")
length=len(str)
print("Total lenght of string :-",length)