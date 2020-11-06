class bank:
    def create(self,no,type,name):
        self.no=no
        self.type=type
        self.name=name
        self.bname="SBI"
        self.balance=500000
    def deposit(self,amount):
        self.balance+=amount
        print("balance :",self.balance)
    def withdraw(self,amount):
        if(self.balance>amount):
            self.balance-=amount
            print("balance :", self.balance)
        else:
            print("insufficient balance")
    def balanceenq(self):
        print("current balance :",self.balance)

ob=bank()
ob.create(19619,"savings","vishnu")
ob.withdraw(25000)
