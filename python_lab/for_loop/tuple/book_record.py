'''
Declare tuple to store information
about Book Title, Price, Auther,
pageCount. Store information of any 4
books in an array and print as below
Title
Pages
Price
Auther
========================================
=====
Let US C
450
Kanitkar
338
.......................................
'''
book=(("let us c",450,"Kanitkar",338),
("Math",380,"R.S.Argwal",280),
("madame bovary",500,"Gustave Flaubert",310),
("Gita",560,"Ved Vayas",600))
'''
print("--------------------------------------")
print("------------------------Output Data------------")
print(book)
print("--------------------------------------")
print("--------access from loop Output Data------------")
for x in range (len(book)):
    print(book[x])
print("--------------------------------------")
print("--------access from loop book record Data------------")
for x in range (len(book)):
    print("Title :",book[x][0])
    print("Pages :",book[x][1])
    print("Author :",book[x][2])
    print("Price :",book[x][3])
    print("----------------------------------------------")

    '''

book=[("let us c",450,"Kanitkar",338),
("Math",380,"R.S.Argwal",280),
("madame bovary",500,"Gustave Flaubert",310),
("Gita",560,"Ved Vayas",600)]


print(book)
print("--------------------------")
for x in range(len(book)):
    newbook=book[x]
    print("Title :",newbook[0])
    print("Pages :",newbook[1])
    print("Author :",newbook[2])
    print("Price :",newbook[3])
    print("-----------------------------")
print("***********************")