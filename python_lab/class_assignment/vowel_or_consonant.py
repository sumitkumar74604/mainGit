'''
Wap to calculate whether a character is vowel or consonent
'''

print("\nWap to calculate whether a character is vowel or consonent\n")
character=input("Enter a character -\t")
chr=ord(character)
#print(" Ascii Value is -",chr)
if 'a'==character or 'A'==character or 'e'==character or 'E'==character or 'i'==character or 'I'==character or 'o'==character or'O'==character or 'u'==character or 'U'==character:
    print("Character is Vowel - \t",character)
elif chr>=32 and chr<=64 or chr>=91 and chr<=96 or chr>=123 and chr<=127:
    print("It's not a alphabate  - \t",character)
else:
    print("Charecter is Consonent  - \t",character)