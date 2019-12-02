//1
// function helloWorld() {
//   console.log("hello World");
//
// }

//2
// function name(name) {
//   console.log("Hello "+name);
// }

//3
// function add(n1,n2) {
//   console.log("The sum of two number are "+(n1+n2));
// }
// function cude(num) {
//   return num*num*num
// }

var v="Gobal V"
var stuff="Gobal Stuff"

function fun(stuff) {
  console.log(v);
  stuff="reassign stuff inside func"
  console.log(stuff);
}
fun();
console.log(stuff);
