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
});
