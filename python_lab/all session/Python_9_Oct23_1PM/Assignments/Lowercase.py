print("\n Q.10 Write a program to calculate whether character is in lowercase or uppercase.\n")

x=input("enter character\t")
# if (x>='A')and(x<='Z'):
# 	print( x, "is uppercase")
# elif (x>='a')and(x<='z'):
# 	print(x , " is lowercase")
# else:
# 	print(x,"given value is not a character")
val = ord(x)	
if (val>=65)and(val<=90):
	print( x, "is uppercase")
elif (val>=97)and(val<=122):
	print(x , " is lowercase")
else:
	print(x,"given value is not a character")