var data="hello this is javascript programming";
var words=data.split(" ");
dict={};
for (word of words){
        if(word in dict){
        dict[word]+=1;
        }
        else{
        dict[word]=1
        }
}
console.log(dict)