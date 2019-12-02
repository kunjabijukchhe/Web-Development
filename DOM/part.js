var myHeader=document.querySelector("h1");
myHeader.style.color='red';

//Ramdom color
function color() {
  var letter="0.123456789ABCDEF";
  var color="#";
  for(var i=0;i<6;i++)
  {
    color+=letter[Math.floor(Math.random()*16)];

  }
  return color;

}

function change() {
    colorInput=color()
    myHeader.style.color=colorInput;
}
//millisecond=500
setInterval("change()",500);
