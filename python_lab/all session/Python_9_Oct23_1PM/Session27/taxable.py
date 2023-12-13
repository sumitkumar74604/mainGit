from abc import ABC,abstractmethod

class Taxable (ABC):
    #def __init__(self): # iska kaaam kya hai yaha ye smjh na hai 
     #   self.TaxRate # ye kyu use ho rha hai 
    @abstractmethod
    def Gettax(self):
        pass
    
class Employee(Taxable):
    def __init__(self):
        self.ID=0
        self.Name=""
        self.salary=0
    def Gettax(self):
        if self.salary>1000000 :
            self.tsalary=(self.salary*30)/100
        elif self.salary >=500000 and self.salary<1000000:
            self.tsalary=(self.salary*20)/100
        elif self.salary <500000 :
            self.tsalary=(self.salary*6)/100
        return self.tsalary
    def display(self):
        print("---------------- Employee -------------------------------")
        print("ID - \t\t",self.ID)
        print("Name - \t\t",self.Name)
        print("Salary - \t",self.salary)
        print("Tax Charge - \t",self.tsalary)
        
class Restaurent(Taxable):
    def __init__(self):
        self.Name=""
        self.Bill=0
    def display(self):
        print("---------------- Restaurant -------------------------------")
        print("Name - \t\t",self.Name)
        print("Bill - \t\t",self.Bill)
        print("GST - \t\t",self.GST)
    def Gettax(self):
        self.GST=(self.Bill*10)/100
        return self.GST

#-----------------------------------------------------
e1=Employee()
e1.Name="S_kumar"
e1.ID=101
e1.salary=500000
e1.Gettax()
e1.display()
#-------------------
e2=Employee()
e2.Name="S_kumar"
e2.ID=102
e2.salary=5000
e2.Gettax()
e2.display()
print("***********************************************")
#-------------------

r1=Restaurent()
r1.Name="ABC"
r1.Bill=1000
r1.Gettax()
r1.display()
#---------------
r2=Restaurent()
r2.Name="DEF"
r2.Bill=100
r2.Gettax()
r2.display()
#-----------
r3=Restaurent()
r3.Name="GHI"
r3.Bill=100000
r3.Gettax()
r3.display()
print("***********************************************")

record_list=[e1,e2,r1,r2,r3]
total = 0
for i in range(len(record_list)):
    if isinstance(record_list[i],Employee ):
        total=total+record_list[i].tsalary
    if isinstance(record_list[i],Restaurent):
        total=total+record_list[i].GST
print("Total tax of  sum = \t",total)
print("--------------------------------")

#------------------------------------------
# Creating global function :------------

def Global_Function(t):
    print("Refund on apply Tax -\t",t.Gettax() * 0.05)
    
Global_Function(e1)
Global_Function(e2)
print("--------------- Restaurent ----------------------")
Global_Function(r1)
Global_Function(r2)
Global_Function(r3)
        
                

        
        