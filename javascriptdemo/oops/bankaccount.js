class bank{

        static bname(){
        var bankname="SBI";
        console.log(bankname)
        }

        constructor(acno,name){
        this.balance=5000;
        this.acno=acno;
        this.name=name;
        }

        deposit(amount){
        this.balance+=amount;
        console.log(amount+"has been credited.Available balance"+this.balance)
        }

        withdraw(amount){
        if(amount>this.balance){
        console.log("insufficient balance")}
        else{
        this.balance-=amount;
        console.log(amount+"has been debited.Available balance"+this.balance)}
        }


}

var obj=new bank(1112000,"vishnu");
obj.deposit(10000);
bank.bname();
