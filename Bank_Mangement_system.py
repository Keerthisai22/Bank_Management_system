class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit_amount(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"💸 Amount deposited successfully Rs.{amount}\n")
        else:
            print("❌No sufficient Amount\n")
    def balance_amount(self):
        print("Account Holder:",self.name)
        print("Balance Amount:",self.balance)
class SavingsAccount(BankAccount):
    def withdraw(self,amount):
        if amount-self.balance<1000:
            self.balance-=amount
            print(f"💸 Amount withdraw successfully Rs.{amount}\n")
        else:
            print("❌Insufficient Amount\n")
    def interest(self):
        interest=self.balance*0.05
        self.balance+=interest
        print(f"💰 Interest: Rs.{interest}")
class CurrentAccount(BankAccount):
    def withdraw(self,amount):
        if amount<=self.balance+2000:
            self.balance-=amount
            print(f"💸 Amount withdraw successfully Rs.{amount}\n")
        else:
            print("❌Insufficient Amount\n")
def main():
    print("\n🏦 BANK MANAGEMENT SYSTEM 🏦\n")
    acc_type=input("Enter the acccount_type (savings/current)=").lower()
    name=input("Enter the name=")
    balance=int(input("Enter the Initial balance="))
    if acc_type=="savings":
        account=SavingsAccount(name,balance)
    else:
        account=CurrentAccount(name,balance)
    print("\n1.Deposit Amount")
    print("2.Withdraw Amount")
    print("3.Balance Amount")
    if acc_type=="savings":
        print("4.Interest")
    print("0.Exit")
    while True:
        choice=int(input("\nEnter the choice="))
        if choice==1:
            account.deposit_amount(float(input("Enter the Amount=")))
        elif choice==2:
            account.withdraw(float(input("Enter the Amount=")))
        elif choice==3:
            account.balance_amount()
        elif choice==4 and acc_type=="savings":
            account.interest()
        elif choice==0:
            print("\n🏦Thank you for using python bank!💰")
            break
        else:
            print("❌Invalid choice")
main()
            
            
