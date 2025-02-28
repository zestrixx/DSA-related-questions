$(document).ready(function () {

    // $$$$$$$$$$$$$$$$ events on form $$$$$$$$$$$$$$$$

    $('.badge').css('background-color', '#ffb850')
    $('input[type="checkbox"]').change(function () {
        var box = $('input[type="checkbox"]:checked')
        $('.badge').text(box.length)
        if (box.length > 0) {
            $('.badge').css('background-color', 'red')
        }
        else {

            $('.badge').css('background-color', '#ffb850')
        }

    })

    // var check = 0;
    // $('input[type="checkbox"]').change(function () {
    //     if ($(this).is(':checked')) {
    //         check += 1;
    //     } else {
    //         check -= 1;
    //     }
    //     $('#result').text(check + " boxes are checked")
    // })


    $('#fname, #lname').keyup(function () {
        $('#result').text("your name is changed to " + $('#fname').val() + " " + $('#lname').val())
        // $("form").append("<p>hey appended on name change</p>")
    })


    $('input[type="checkbox"]').css('margin', "10px")

    // $('input').focusin(function () {
    //     $(this).attr('class', 'focusedin')
    // })
    // $('input').focusout(function () {
    //     $(this).attr('class', 'focusedout')
    // })

    // $$$$$$$$$$$$$$$$ events on buttons $$$$$$$$$$$$$$$$

    $('#color1').click(function () {
        $(this).addClass("color1")
        $('.blue').removeClass('color2')
        $('.red').removeClass('color3')
        $("#color").css("background-color", "lightgreen")
        $("#color").text("background color is green")
    })

    $('#color2').click(function () {
        $(this).addClass("color2")
        $('.green').removeClass('color1')
        $('.red').removeClass('color3')
        $("#color").css("background-color", "lightblue")
        $("#color").text("background color is blue")
    })

    $('#color3').click(function () {
        $(this).addClass("color3")
        $('.blue').removeClass('color2')
        $('.green').removeClass('color1')
        $("#color").css("background-color", "rgb(255, 146, 188)")
        $("#color").text("background color is red")
    })


    // $$$$$$$$$$$$$$$$ jquery accordion menu $$$$$$$$$$$$$$$$

    $('#accordion').accordion()

    // $$$$$$$$$$$$$$$$ jquery chaining $$$$$$$$$$$$$$$$

    $('#animate').click(function () {
        $('.box').css('background-color', 'red')
            .slideUp(2000)
            .slideDown(2000)
    })


    // $$$$$$$$$$$$$$$$ Temporary demo code $$$$$$$$$$$$$$$$

    $('#demo').click(function () {
        $('.red + .green').text('demo')
    })



})
