function setDate() {
    timeElapsed = Date.now();
    const today = new Date(timeElapsed);
    console.log(today.toDateString())
    document.getElementById("date-today").innerHTML = '<p>' + today.toDateString() + '</p>'
}

setDate()



$(document).ready(function () {
    // messages timeout for 5 sec 
    setTimeout(function () {
        $('.message').fadeOut('slow');
    }, 5000); // <-- time in milliseconds, 1000 =  1 sec

    // delete message
    $('.del-msg').live('click', function () {
        $('.del-msg').parent().attr('style', 'display:none;');
    })
});