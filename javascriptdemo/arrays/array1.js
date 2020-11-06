var ar=[4,8,5];
var ar1=[]
var s=0;
for(item of ar){
s=s+item;
}
for(item of ar){
t=s-item;
ar1.push(t);
}
console.log(ar1);