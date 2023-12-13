
class BankAccount:
    def __init__(self, accountNo, balance):
        self.accountNo = accountNo
        self.balance = balance
    def display(self):
        print("AccountNo:", self.accountNo)
        print("Balance:", self.balance)


    def depositAmount(self, amt):
        self.balance = self.balance+amt

    def withdrawAmount(self, amt):
        self.balance = self.balance-amt


# ---- create a saving Account 


class SavingAccount(BankAccount):
    minimumBalance = 1000.0
    def __init__(self, customername, address, accountNo, balance):
        self.customername = customername
        self.address = address
        self.accountNo = accountNo
        self.balance = balance
        
    def display(self):
        super().display()
        print("Minimum Balance:", SavingAccount.minimumBalance)
        print("CustomerName:", self.customername)
        print("Address:", self.address)

    def withdrawAmount(self, amt):       
        # 10000-10000=2000
        if ((self.balance - amt) >= SavingAccount.minimumBalance):  
            super().withdrawAmount(amt)
            print("Yes, you can withdrawAmount !! Rs:", amt)
        else:
            print("No,you can not withdrawAmount !!")

   


# ---- Bank details 
savAcc1 = SavingAccount("Rahul Sharma", "Indore M.P 452001", 101, 32000.0)
savAcc1.withdrawAmount(310.0)
savAcc1.display()
print("---------------------------------------------------------")
savAcc2 = SavingAccount("Vinay Sharma", "Indore M.P 452001", 102, 21000.0)
savAcc2.withdrawAmount(15)
savAcc2.display()
print("---------------------------------------------------------")
savAcc3 = SavingAccount("Raj Sharma", "Indore M.P 452001", 103, 25000.0)
savAcc3.withdrawAmount(5000)
savAcc3.display()
print("---------------------------------------------------------")


class CheckingAccount(BankAccount):

    overDraftLimit = 500.0

    def __init__(self, shopname, shopaddress, accountNo, balance):
        self.shopname = shopname
        self.shopaddress = shopaddress
        self.accountNo = accountNo
        self.balance = balance
    def display(self):
        super().display()
        print("ShopName:", self.shopname)
        print("ShopAddress:", self.shopaddress)

    def withdrawAmount(self, amt):
        if amt <= (CheckingAccount.overDraftLimit+self.balance):
            super().withdrawAmount(amt)
            print("Yes, you can withdrawAmount !! Rs:", amt)
        else:
            print("No, you can not withdrawAmount !! Rs:", amt)

    

# ----


checkAcc1 = CheckingAccount(
    "Porwal Stationary", "Palasia Indore M.P", 202, 100000.0)
checkAcc1.withdrawAmount(250000.0)
checkAcc1.display()
print("---------------------------------------------------------")
checkAcc2 = CheckingAccount(
    "Gupta Stationary", "Palasia Indore M.P", 202, 50000.0)
checkAcc2.withdrawAmount(100001.0)
checkAcc2.display()
print("---------------------------------------------------------")
checkAcc3 = CheckingAccount(
    "Neha General Store", "Palasia Indore M.P", 202, 230000.0)
checkAcc3.withdrawAmount(50000.0)
checkAcc3.display()
print("---------------------------------------------------------")
checkAcc4 = CheckingAccount(
    "Gopal Kirana Store", "Palasia Indore M.P", 202, 450000.0)
checkAcc4.withdrawAmount(100001.0)
checkAcc4.display()
print("---------------------------------------------------------")

listBank = [savAcc1, savAcc2, savAcc3,
            checkAcc1, checkAcc2, checkAcc3, checkAcc4]
print(listBank)

for i in range(0, len(listBank)):
    if isinstance(listBank[i], SavingAccount):
        print("--- Saving Account---")
        listBank[i].display()
    if isinstance(listBank[i], CheckingAccount):
        print("--- Checking Account---")
        listBank[i].display()
    print("---------------------------------")
