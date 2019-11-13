

function myFunction(){
alert("fuck man it's working");
var x = document.getElementById("provident_fund").value;
var y = document.getElementById("total_tax").value;
num1 = +x;
num2 = +y;
var ans = num1 + num2;
if(ans){
document.getElementById("total_deduction").value = ans;
}else
{
alert('error');
}

}

function myFunction2(){

var x3 = document.getElementById("bs").value;
var x4 = document.getElementById("house_rent").value;
var x5 = document.getElementById("mediclaim").value;
var x6 = document.getElementById("travel").value;
var x7 = document.getElementById("dearness").value;
var x8 = document.getElementById("reimburement").value;
var x9 = document.getElementById("conveyance").value;
var x10 = document.getElementById("other_salary").value;

num3 = +x3;
num4 = +x4;
num5 = +x5;
num6 = +x6;
num7 = +x7;
num8 = +x8;
num9 = +x9;
num10 = +x10;

var ans = num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 ;
if(ans){
document.getElementById("total_salary").value = ans;
}else
{
alert('error');
}

}