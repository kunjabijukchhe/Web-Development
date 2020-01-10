//$("h1").click(function(){console.log("click")})
//$("h1").click(function(){$(this).text("i was click")})
$("#press").click(function(){$("h3").toggleClass("turnBlue")})//#=class in input (#press)=input

//key press
$('input').eq(0).keypress(function(){$("h3").toggleClass("turnRed")})
//$('input').eq(0).keypress(function(){console.log(event)})
$('input').eq(1).keypress(function(event){
  if(event.which===13)//13=enter
  {
    $("h3").toggleClass("turnRed")
  }

})


//on
//$("h1").on('dblclick',function(){$(this).text("i was click")})//if double click
//$("h1").on('dblclick',function(){$(this).toggleClass("turnRed")})
$("h1").on('mouseenter',function(){$(this).toggleClass("turnRed")})

//on
$("input").eq(1).on('click',function(){$('.container').slideUp(3000)})
$("input").eq(1).on('click',function(){$('.container').fadeOut(3000)})
