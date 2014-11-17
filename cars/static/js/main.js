$(document).ready(function(){
    $("#driver").click(function(event){
        $.ajax({
            type:'GET',
            url:'/get-list/',
            success:function(response){
              console.log(response);
              if (1 == response.status) {
                  $('#load_data').html(response.html);
              }
            }
        });
    });

    $("#add_car").click(function(event){
      event.preventDefault();
      $.ajax({
        type:'GET',
        url:$(this).attr('href'),
        success:function(response){
          console.log(response);
          $('#load_data').html(response.html);
        }
      });
    });

    function CarEntry(){
      $('#cars').validate({
        rules:{
          name:{required:true},
          image:{required:true}
        },
        message:{
          name:{required:'*'},
          image:{required:'*'}
        },

        submitHandler:function(form){
          $.ajax({
            url:form.action,
            type:form.method,
            data:$(form).serialize(),
            success:function(response){
              if (response.status == 0) {
                $('#form_error').text(response.message).show(),
              }
              else{
                alert(response.message);
              }
            }
          });
        }
      });
    }


});
