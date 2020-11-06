class bank{
        static account(){

            var data={"amal":{"username":"amal","password":"user one","balance":1000,"mpin":100},
                      "athul":{"username":"athul","password":"user two","balance":2000,"mpin":101} }

            return data


        }

        static deposit(){

                var user=document.querySelector("#usr").value;
                var mpin=document.querySelector("#mpin").value;
                var amn=Number(document.querySelector("#amount").value);


                var data=bank.account()

                if(user in data){
                       var id=data[user]["mpin"];

                       if(id==mpin){
                       data[user]["balance"]+=amn;
                       alert("Available balance is "+data[user]["balance"]);
                       }
                       }
                }

                        static withdraw(){

                var user1=document.querySelector("#usr").value;
                var mpin1=document.querySelector("#mpin").value;
                var amn1=Number(document.querySelector("#amount").value);


                var data=bank.account()

                if(user1 in data){

                       var id=data[user1]["mpin"];
                       var bal=data[user1]["balance"]

                       if(id==mpin1){
                            if(bal>amn1){
                                data[user1]["balance"]-=amn1;
                                alert("Available balance is "+data[user1]["balance"]);
                                }
                            else{
                                 alert("Insufficient balance")
                                }
                            }
                       else{
                            alert("incorrect mpin");
                            }
                       }
                       else{
                            alert("user not found");
                       }
                }

                static balance(){

                var user=document.querySelector("#usr").value;
                var mpin=document.querySelector("#mpin").value;
                var amn=Number(document.querySelector("#amount").value);


                var data=bank.account()

                if(user in data){
                       var id=data[user]["mpin"];

                       if(id==mpin){
                       amount.value=data[user]["balance"];

                       alert("Available balance is "+data[user]["balance"]);
                       }
                       }
                }
}