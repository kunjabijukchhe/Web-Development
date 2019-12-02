var a=[];

function addNew() {
  var b=prompt("What name would you like to add?")
  a.push(b)
}

function remove() {
  var c=prompt("What name would you like to remove?")
  var index=a.indexOf(c)
  a.splice(index,1)
}
function display() {
  console.log(a);
}
var start=prompt("y/n")
var request="empty"
if(start==="y"){
  while(request!=="quit")
  {
    request=prompt("add,remove,display and quit")
    if(request==="add")
    {
      addNew();
    }
    else if (request==="remove") {
      remove();
    }
    else if (request==="display")
    {
      display();
    }
    else {
      alert("Quit")
    }

  }
}
