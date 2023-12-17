class Book:
    
    count=0
    discountrate=10

    def __init__(self,title,price):
        self.title=title
        self.price=price
        Book.count+=1
        

    def display(self):
        print("Book Title is:",self.title)
        print("Book Price is:",self.price)
        print("discount rate is:",Book.discountrate)
        print("================================")

    def calcdiscount(self):
        discount = (self.price*Book.discountrate)/100
        return discount

b1=Book("ramayan",200)
b2=Book("mahabharat",400)
b3=Book("panchtantra",100)
b4=Book("constitution of india",500)

totalprice=0
totaldisamt=0
list_book = [b1,b2,b3,b4]
for i in range(len(list_book)):
    totaldisamt+=list_book[i].calcdiscount()
    list_book[i].display()
    totalprice+=list_book[i].price

print("The sum of all book price is",totalprice)
print("sum of all books discount is",totaldisamt)
