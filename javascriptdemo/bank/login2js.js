 class bank{


        static deposit(){
        window.balance=5000;
        var amount=document.getElementById("screen1").value;
        window.balance+=eval(amount);
        alert(amount+"has been credited.Available balance"+window.balance)
        screen1.value=("balance"+window.balance);
        }

        static withdraw(){
        var amount=document.getElementById("screen").value;
        alert(window.balance)
        alert(amount)
        if(amount>window.balance){
        console.log("insufficient balance")}
        else{
        window.balance-=amount;
        alert(amount+"has been debited.Available balance"+window.balance)}
        screen.value=("balance"+window.balance);
        }
}