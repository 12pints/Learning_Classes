#define class Bankaccount
class BankAccount:
    def __init__(self, name, balance=0.0):
        self.log("Account created!")
        self.name=name
        self.balance=balance

    def getBalance(self):  #Getter for Balance
        self.log("Balance checked at " + str(self.balance))
        return self.balance

    def setBalance(self, newBalance):  #Setter for new Balance
        self.log("Balance changed to "+ str(newBalance))
        self.balance=newBalance

    def deposit(self, amount):
        self.balance += amount
        self.log("deposited  +" + str(amount) + " total:" + str(self.balance))

    def withdraw(self, amount):
        self.balance -=amount
        self.log("withdrawn -" + str(amount) + " total:" + str(self.balance))

    def log(self, message): #logging method
        myLog=open("TestLog.txt", "a")
        print(message, file=myLog)
        myLog.close()


myBankAccount=BankAccount("Pietje Retief")  #this creates the bank account and sets the balance to 0.0 when opening
myBankAccount.setBalance(20.0)
print(myBankAccount.getBalance())
myBankAccount.deposit(25.0)
print(myBankAccount.getBalance())
myBankAccount.withdraw(5.0)
print(myBankAccount.getBalance())


