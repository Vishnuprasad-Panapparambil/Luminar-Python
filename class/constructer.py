class bank:
    def __init__(self,no,type,name):
        self.no=no
        self.type=type
        self.name=name
        self.bname="SBI"
        self.balance=500000

    def print(self,amount):
        self.balance+=amount
        print("balance :",self.balance)
f=open("employidetails")
emp=[]
for data 
ob=bank()