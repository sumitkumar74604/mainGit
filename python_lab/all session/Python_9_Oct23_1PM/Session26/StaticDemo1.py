'''
Static :
Single Memory Allocation.
All objects of a class shared memory of static variable. 
Accessing variable using className then that variable is said to be static variable.
It gets memory at compile time.

'''

class Bank:
    customer=""
    accNo=0
    balance=0.0
    #static 
    savinginterestRate = 3.2
    SI=0
    time=0
    noOfCustomer=0

    def __init__(self,customer,accNo,balance,time):
        self.accNo=accNo
        self.customer=customer
        self.balance=balance
        self.time=time
        Bank.noOfCustomer+=1

    def calSI(self):
        self.SI = (self.balance*Bank.savinginterestRate*self.time)/100  

    def display(self):
        print("Customer Name is:",self.customer)
        print("Customer AccNo is:",self.accNo)
        print("Customer Balance in Rs:",self.balance)
        print("Saving Interest Rate is:",Bank.savinginterestRate,"%")
        print("Saving Interest Amount in Rs:",self.SI," in ",self.time," years")
        print("===============================================")

    @staticmethod
    def BankInfo():
        print("Palasia Branch Indore M.P")
        print("No of Customer is:",Bank.noOfCustomer)

#--- 

Bank.savinginterestRate = 4.1

b1 = Bank("Raj Yadav",1212,120000.0,2)
b1.calSI()
b1.display() 

b2 = Bank("Mukesh Yadav",4545,230000.0,3)
b2.calSI()
b2.display() 

Bank.BankInfo() 

