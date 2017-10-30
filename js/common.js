$(document).ready(function(){
    $('button[type="toggle"]').click(function(){
        var target = $(this).attr('toggle-target');
        $(target).toggle();
    });
});
