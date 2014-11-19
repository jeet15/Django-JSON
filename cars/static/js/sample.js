$(document).ready(function(){
    var $vl = $("#back");

    $vl.css("background", "#99CCFF");

    setTimeout(function () {
        $vl.css("background", "yellow");
    }, 2000);


    $("#btn1").click(function(){
        alert("This is the link"+ $("#ht1").attr("href"))
    });
    $("#btn2").click(function(){
        alert("This is the value "+ $("#txt").val())
    });

    $("#a1").click(function(event){
        event.preventDefault();
        alert("This is the preventDefault")
    });

});