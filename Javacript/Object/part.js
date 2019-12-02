// var employee={
//   name:"Jhon Smith",
//   job:"Programmer",
//   age:31,
// // nameLength:function() {
// //     console.log(this.name.length);
// //
//   report:function(){
//     alert("Name is "+this.name+" ,Job is "+this.age+" , Age is "+this.age)
//   }
//
//
// }
//
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,

};
var employee1 = {
  name: "Alice Smith",
  job: "Developer",
  age: 29,

};
var person = {
  firstName: "John",
  lastName : "Doe",
  id     : 5566,

};
console.log("%c My friend","color:orange;font-size:20px");
console.log({employee,person});
console.table([employee,employee1,person])

console.time('looper')
var i=0;
while(i<1000000){
  i++
}
console.timeEnd('looper')
//Stack trace logs
const deleteMe=()=>console.trace("bye")
deleteMe()
