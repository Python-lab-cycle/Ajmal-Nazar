class bank():
    def __init__(self,acnt,nam,typ):
        self.ac=acnt
        self.name=nam
        self.type=typ
        self.amount=0
    def printamt(self):
        print("Account Name",self.name)
        print("Account Number=",self.ac)
        print("Account Type=",self.type)
        print("Balance=",self.amount)
    def deposit(self,d1):
        self.amount=self.amount+d1
        return(self.amount)
    def with1(self,w1):
        return(self.amount-w1)
n=input("Enter Name:")
t=input("Enter Type:")
a=int(input("Enter Account Number:"))
obj=bank(a,n,t)
print("Account Details")
obj.printamt()
while[True]:
    print("\n*****Menu*****")
    print("\n1.Deposit")
    print("\n2.Withdraw")
    choice=int(input("Enter Choice:"))
    if(choice==1):
        d=int(input("Enter Amount to Deposit:"))
        print("Balance Amount:",obj.deposit(d))
    elif(choice==2):
        w=int(input("Enter amount to withdraw"))
        if(w>d):
            print("Insufficient Balance")
        else:
            print("Balance Amount=",obj.with1(w))
    else:
        print("Enter a valid choice")
#print()
    
    
