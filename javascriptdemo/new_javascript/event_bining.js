
var headone=document.querySelectorAll("#one")
var two=document.querySelector("#two")
var three=document.querySelector("#three")

function mouseov(){
console.log(item.textContent);

}

function clk(){
two.textContent="clicked";
two.style.color="yellow";
}

function dbcclk(){
three.textContent="double clicked";
three.style.color="green";
}
for(var item of headone){
    item.addEventListener("mouseover",mouseov)
}
two.addEventListener("click",clk)
three.addEventListener("dblclick",dbcclk)
