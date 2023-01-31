$(window).scroll(function(){
    var scroll = $(window).scrollTop();
    console.log(scroll)

    document.getElementById("myBody").style.marginTop = (-100 - 0.5 * scroll) + "px";
});