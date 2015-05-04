$(".open-panel").click(function(){
  
  $("html").addClass("openNav");
  
});
	
$(".close-panel, #content").click(function(){
  
$("html").removeClass("openNav");
  
});