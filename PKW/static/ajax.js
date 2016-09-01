//Obsługa zapisywania wprowadzonych zmian do bazy danych
$(".modal").on("click", ".save_button", function() {
    var votes_for_first = $(this).parent().siblings().children(".vote_input1").val();
    var votes_for_second = $(this).parent().siblings().children(".vote_input2").val();
    var dis_name = $(this).parent().siblings(".dis_name").text();
    $.ajax({
        type:'GET',
        url:'editing/save',
        data: {
            dn: dis_name
        },
        success: function(data) {
            question = "Ostatnia edycja miała miejsce " +
                data +
                ". Czy na pewno chcesz dokonać zmiany?";
            if(confirm(question)) {
                $.ajax({
                    type:'POST',
                    url:'viewing/save',
                    data: {
                        v1: votes_for_first,
                        v2: votes_for_second,
                        dn: dis_name
                    },
                    success: function() {
                        alert("Zmiany zostały wprowadzone");
                    }
                })
            }
        },
		error: function(data) {
			
		}
    });
});
