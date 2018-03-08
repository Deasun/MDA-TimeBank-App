$(document).ready(function() {

    // Numbers (need) on Challenge Pages dissolve in on page load
    $('h1.hidden').fadeIn(1000).removeClass('hidden');
    $('h2.hidden').show(1000).removeClass('hidden');
    $('h1.hidden_title').delay(1000).show("fast").removeClass('hidden');
    $('h2.hidden_title').delay(1000).show("fast").removeClass('hidden');
    $('form.hidden_title').delay(1000).show("fast").removeClass('hidden');


    // Send Ajax request for guesses


    // AJAX POST Request
    $('.challenge_btn').click(function() {
        var score = $('#numScore').val();
        $.ajax({
            url: '/challenge_1',
            data: $('form').serialize(),
            type: 'POST',
            // Define what to do with the request here? Text filed black angle?
            success: function(response) {
                alert("SUCCESS!");
            },
            error: function(error) {
                return false;
            }
        });
    });


    
    // Transitions after button click
    $('.challenge_btn').click(function() {
        $(this).slideUp("fast");
        $('h1.hidden_answer').fadeIn(4000).removeClass('hidden');
        $('.hidden_icon').delay( 2500 ).fadeIn(400).fadeOut(400).fadeIn(400).fadeOut(400).fadeIn(400).removeClass('hidden');
    });
});
