class person{

    setperson(age,name){

    this.age=age;
    this.name=name;

    }
    printvalues(){

    console.log(this.name);
    console.log(this.age);

    }
}

var ob=new person();
ob.setperson(25,"vishnuprasad");
ob.printvalues();
