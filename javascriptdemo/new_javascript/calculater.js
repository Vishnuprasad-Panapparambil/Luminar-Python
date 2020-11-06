function insert(num){
        var screen=document.getElementById("screen");
        screen.value=screen.value+num;
        }
function equal(){
        var screen1=document.getElementById("screen1");
        var screen=document.getElementById("screen");

        var display=eval(screen.value);

        screen1.value=display;
}
function screenclear(){
        var screen1=document.getElementById("screen1");
        var screen=document.getElementById("screen");
        screen.value="";
        screen1.value="";

}
function backspace(){
        var data=document.getElementById("screen").value;
        var data1=data.subString(0,)