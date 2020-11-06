//function add(num1,num2){
//return num1+num2;
//}
//f=(num1,num2) =>num1+num2
//console.log(f(10,5))
//
//f=(num1) =>num1**2
//console.log(f(5))

var arr=[1,2,3,4];
var res=arr.map(no=>no*no);
console.log(res)
var evn=arr.filter(num=>num%2==0);
console.log(evn)
var data=arr.reduce((no1,no2)=>no1+no2);
console.log(data)