class BankAccount:
    
    __ROI = 10.5
    
    def __init__(self,name,amount):
        self.Name = name
        self.Amount = int(amount)
        self.depositAmount = 0.0
        self.withdrawAmount =0.0
        self.IntrestAmount = 0.0
    
    def Deposit(self,depositAmount):
            self.Amount = self.Amount + depositAmount
            print("Current Amount is : ",self.Amount)
        
    def Withdraw(self,withdrawAmount):
        if (self.withdrawAmount < self.Amount):
            self.Amount = self.Amount - withdrawAmount
            print("Current Amount is : ",self.Amount)
        else:
            print("Withdraw amount is greatr than your current Amount : ")
            print("Thank You For Choosing our Bank...")

    
    def CalculateIntrest(self):
        self.IntrestAmount = self.Amount*(BankAccount.__ROI/100)
    
    def Display(self):
        print("Name Of Accountant : ",self.Name)
        print("Your Current Amount is : ",self.Amount)
        
        print("Rate of Intrest on your amount is ",self.IntrestAmount)
        
def main():
    
    Name = input("Enter your Name  : ")
    Amount = float(input("Enter the amount : "))
    
    obj1 = BankAccount(Name,Amount)
    
    Deposit = float(input("Enter the deposit amount : "))
    obj1.Deposit(Deposit)
    
    withdraw = float(input("Enter the withdraw amount : "))
    obj1.Withdraw(withdraw)
    
    obj1.CalculateIntrest()
    obj1.Display()
    

if __name__=="__main__":
    main()