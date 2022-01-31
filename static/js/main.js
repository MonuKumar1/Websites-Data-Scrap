var $message = $("#message");
$message.on("keydown keypress", function() {    
    var $this = $(this),
    val = $(this).val()
                 .replace(/(\r\n|\n|\r)/gm," ") // replace line breaks with a space
                 .replace(/ +(?= )/g,''); // replace extra spaces with a single space

    $this.val(val);
});

$message.bind("paste", function() {
    var $elem = $(this)
    console.log("paste checking")
    setTimeout(function () {
        console.log("after 1 second");
        val = $elem.val()
                     .replace(/(\r\n|\n|\r)/gm," ") // replace line breaks with a space
                     .replace(/ +(?= )/g,''); // replace extra spaces with a single space

        $elem.val(val);
    }, 100);


    // console.log("space checking")
})

// on button click
$('#onsub').click(function (e) {
    e.preventDefault();
    console.log("onsub working")
    
    $("#overlay").fadeIn(300);

    
    
    var message = $("#message").val();

    // fetch('/submit', {
    //   body: JSON.stringify({urls:message}),
    //   method: 'POST',
    //   headers: {
    //       'Content-Type': 'application/json; charset=utf-8'
    //   },
    // })
    // .then(response => response.blob())
    // .then(response => {
    //     console.log('responce received')
    //     const blob = new Blob([response], {type: 'application/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'});
    //     const downloadUrl = URL.createObjectURL(blob);
    //     $('#dwnlod').css('display', 'block')
    //     $('#dwnlod').attr('href', downloadUrl);
    //     $('#dwnlod').attr('download','urls.xlsx');
    //     $("#overlay").fadeOut(300);
    // })

    $.ajax({
        type: "POST",
        url: "/submit",
        data: JSON.stringify({urls:message}),
        dataType: "json",
        headers: {
            'Content-Type': 'application/json; charset=utf-8'
        },
        success: function (response) {
            console.log('responce received')
            console.log(response)
            $('#dwnlod').css('display', 'block')
            $('#dwnlod').attr('href', response.gsheet_link);
            $('#dwnlod').attr('download','urls.xlsx');
            $("#overlay").fadeOut(300);
        }
        // console.log('responce received')
        //     console.log(response)
        //     if (response.status == 'error') {
        //         console.log('error')
        //         $("#overlay").fadeOut(300);
        //         alert(response.message)
        //     }else{
        //         $('#dwnlod').css('display', 'block')
        //         $('#dwnlod').attr('href', response.gsheet_link);
        //         $('#dwnlod').attr('download','urls.xlsx');
        //         $("#overlay").fadeOut(300);
        //     }

        // }
    });

     
  });

