$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/rango/like_category/', {catgory_id: catid}, function(data){
        $('#like_count').html(data);
        $('#likes').hide();
   });
});

