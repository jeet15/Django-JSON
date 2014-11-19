$(document).ready(function(){

    $("#back").css("background", "#99CCFF");

    setTimeout(function () {
        $("#back").css("background", "yellow");
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

    $("#form").validate({
        rules:{
            name:{
                required:true
            },
            email:{
                required:true
            }
        },
        message:{
            name:"required field",
            email:"required field"
        }
    });

    /* form fetching using ajax */

    $("#add_user").click(function(event){
      event.preventDefault();
      $.ajax({
        type:'GET',
        url:$(this).attr('href'),
        success:function(response){
          console.log(response);
          $('#load_form').html(response.html);
          userBind();
        }
      });
    });

    /* form validation code */
    function userBind(){
        $("#user_form").validate({
          rules:{
            name:{
              required:true
            },
            email:{
            required:true
            }
          },
          message:{
            name :"required field",
            email:"required field"
            }
        });    
    }
});