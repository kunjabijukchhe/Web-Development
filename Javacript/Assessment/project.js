var a=prompt("Enter your first name:")
var b=prompt("Enter your last name:")
var c=prompt("Enter your age:")
var d=prompt("Enter your height in centimeters:")
var e=prompt("Enter your pet name:")
alert("Thank you for your information")

var ab=null;

var cc=null;
var dd=null;
var ee=null;

if (a[0]===b[0]) {
  ab=true;
}else {
  ab=false;
}


if(c>20 && c<30)
{
  cc=true;
}else {
  cc=false;
}

if(d>=170)
{
  dd=true;
}else {
  dd=false;
}

if (e[e.length-1]==="y") {
  ee=true;
}
else {
  ee=false;

}

if (ab && cc && dd && ee) {
  console.log("Welcome Comrade! You've passed the Spy Test");

}
else {
  console.log("Sorry, nothing to see here.");
}
