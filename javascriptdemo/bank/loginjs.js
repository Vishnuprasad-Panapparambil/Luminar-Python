class bank{
        static account(){

            var data={"amal":{"username":"amal","password":"user one","balance":1000,"mpin":100},
                      "athul":{"username":"athul","password":"user two","balance":2000,"mpin":101} }

            return data


        }

        static login(){

                var uname=document.querySelector("#usr").value;
                var pwd=document.querySelector("#pwd").value;


                var data=bank.account()

                if(uname in data){
                       var pass=data[uname]["password"];

                        if(pass===pwd){
                            alert("login successfully");
                            window.location="http://localhost:63342/luminartechnolab/javascriptdemo/bank/login2.html";
                        }
                        else{
                            alert("invalid");
                        }
                }




        }


        }