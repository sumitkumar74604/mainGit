class add:
    def _init_(self,a,b):
        self.qty=a
        self.price=b
        
    def show(self):
        sum=0
        for i in range (0,5):
            c=self.qty[i]*self.price[i]
            sum=sum+c
            print([i]," Multiply = ",self.qty[i],"  * ",self.price[i],"=",c,"\t SUM = ",sum)
        print("Total SUM = ",sum)
qty=[1,2,3,4,5]
price=[100,200,300,400,500] 
a1=add()
a1.qty=qty
a1.price=price
a1.show()