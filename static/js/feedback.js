$('button.submit').disabled = true;


function enable_submit() {
    $('button.submit').disabled = false;
    $('button.submit').addClass('not-disabled')
}

function disabled_submit() {
    $('button.submit').disabled = true;
    $('button.submit').removeClass('not-disabled')  
}


$('.rating').on(
    'click', function () {
        var rating = this['value'];
        $('.feedback').css('display', "block");
        feedback_validate(rating);
    });