$(function(){
    var $cars = $('#car-list');
    $ajax({
        type:'GET',
        url:'apps/get-list/',
        success:function(cars){
            if (1 == response.status) {
                console.log(response.name)
            };
        };
    });
});

