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
            },
            submitHandler:function(form){
                $.ajax({
                    url:form.action,
                    type:'POST',
                    data:$(form).serialize(),
                    success:function(response){
                        if (0 == response.status) {
                            $("#form_error").text(response.message).show();
                        }
                        else{
                            $("#id_name").val('');
                            $("#id_email").val('');
                            alert(response.message);

                        }
                    },
                });
            }
        });    
    }

    $("#users").click(function(event){
        $.ajax({
            type:'GET',
            url:'/all-user/',
            success:function(response){
              console.log(response);
              if (1 == response.status) {
                $('#load_form').html(response.html);
                deleteUser()
              }
            }
        });
    });

    function editUser(){

    $("#edit-user").validate({
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
    }

    function deleteUser(){

    $("#delete-user").click(function(e) {
      e.preventDefault();
      var userId = $this.data('user-id');
        $.ajax({
          url: '/delete-user/',
          type: 'get',
          data: {user_id: userId},
          success: function(response) {
            console.log(response);
            if (response.status == 1) {
              alert("user is deleted");
            }
            else{
                alert("data is not available");
            }
          }
        });
    });
    }

});