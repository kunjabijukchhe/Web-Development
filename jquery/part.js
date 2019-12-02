// var x=$('h1');
// var newCSS={
//     'color':'white', 'background':'blue','border':'20px solid orange'}
//
//     x.css(newCSS)
// $('h1').click(function(){
//     console.log("there was a click")
// })
var x=$("h1");

var newCSS={
    "color":"#3c5c56",
    "background":"#bbede4",
  "border":"2px solid pink"}
//x.css(newCSS)


var listItem=$("li");
listItem.css("color","blue")
listItem.eq(0).css("color","#bbede4")
listItem.eq(-1).css("color","#bbede4")


x.text()
x.text("KUNJA BIJUKCHHE")
x.html()
x.html("<b>kunja</b>")
x.html("<i>kunja</i>")

$('input')
//$('input').eq(1).attr('type','checkbox')
$('input').eq(1).val('kunja')
$('input').eq(0).attr('placeholder','kunja')

$('h1')

x.addClass("turnRed")
x.removeClass("turnRed")
x.toggleClass("turnBlue")
listItem.addClass("turnBlue")
listItem.removeClass("turnBlue")
listItem.toggleClass("turnRed")
//listItem.toggleClass("turnRed") //this add and remove
