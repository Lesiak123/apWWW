var map_colors = ["rgb(204,227,255)", "rgb(180,213,253)", "rgb(153,199,255)", "rgb(125,183,254)", "rgb(90,164,254)", "rgb(53,144,255)",
    "rgb(2,115,253)", "rgb(2,96,212)", "rgb(1,74,163)", "rgb(0,53,117)", "rgb(255,219,112)", "rgb(255,205,112)", "rgb(255,193,94)",
    "rgb(255,181,84)", "rgb(255,169,81)", "rgb(255,157,57)", "rgb(254,144,32)", "rgb(255,134,9)", "rgb(231,121,0)", "rgb(206,104,0)"];

function get_voiv_color(voiv_name) {
    var percentage = $(".voivodeship_row").filter(function() {
        return $(this).children(".voiv_name").text() == voiv_name;
    }).children(".first_percent").text();

    var index;
    if (percentage >= 50) {
        index = Math.floor((percentage-50)/2.27);
        if (index > 9) {
            index = 9;
        }
    } else if (percentage < 50) {
        percentage = 100 - percentage;
        index = 10 + Math.floor((percentage-50)/2.27);
        if (index > 19) {
            index = 19;
        }
    }
    return map_colors[index];
}

AmCharts.makeChart( "mapdiv", {
  "type": "map",
  /**
   * create data provider object
   * map property is usually the same as the name of the map file.
   * getAreasFromMap indicates that amMap should read all the areas available
   * in the map data and treat them as they are included in your data provider.
   * in case you don't set it to true, all the areas except listed in data
   * provider will be treated as unlisted.
   */
  "dataProvider": {
    "map": "polandLow",
    "areas":[
        {id:"PL-DS", "color": get_voiv_color("dolnośląskie")},
        {id:"PL-KP", "color": get_voiv_color("kujawsko-pomorskie")},
        {id:"PL-LD", "color": get_voiv_color("łódzkie")},
        {id:"PL-LU", "color": get_voiv_color("lubelskie")},
        {id:"PL-LB", "color": get_voiv_color("lubuskie")},
        {id:"PL-MA", "color": get_voiv_color("małopolskie")},
        {id:"PL-MZ", "color": get_voiv_color("mazowieckie")},
        {id:"PL-OP", "color": get_voiv_color("opolskie")},
        {id:"PL-PK", "color": get_voiv_color("podkarpackie")},
        {id:"PL-PD", "color": get_voiv_color("podlaskie")},
        {id:"PL-PM", "color": get_voiv_color("pomorskie")},
        {id:"PL-SL", "color": get_voiv_color("śląskie")},
        {id:"PL-SK", "color": get_voiv_color("świętokrzyskie")},
        {id:"PL-WN", "color": get_voiv_color("warmińsko-mazurskie")},
        {id:"PL-WP", "color": get_voiv_color("wielkopolskie")},
        {id:"PL-ZP", "color": get_voiv_color("zachodniopomorskie")}
    ]
  },

  "areasSettings": {
    "autoZoom": true,
    "selectedColor": "#CC0000"
  },

  /**
   * let's say we want a small map to be displayed, so let's create it
   */
  "mediumMap": {}
} );



function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

window.addEventListener('load', function(){
    $(".voivodeship_row").each(function(index){
        curRow = $(this);
        var first = curRow.children(".first_percent").text();
        var background = "linear-gradient(to right, blue " +
            first +
            "% , " +
            "orange " +
            first +
            "%)";
        curRow.children(".bar_cell").css({'background-image': background});
    });
})

$('.close').click(function(){
    $('.modal').hide();
});

$('#type_button').click(function(){
    var typeName = $('#select_by_type').val();
    $.ajax({
        type:'GET',
        url:'editing/type',
        data:{
           name: typeName
        },
        success: produce_table
    });
})

$('#voiv_button').click(function(){
    var vName = $('#select_by_voiv').val();
    $.ajax({
        type:'GET',
        url:'editing/voiv',
        data:{
            name: vName
        },
        success: produce_table
    });
})

$('#inh_button').click(function(){
    var min,max;
    switch($('#select_by_inh').val()) {
        case '5':
            min = 0;
            max = 5000;
            break;
        case '10':
            min = 5001;
            max = 10000;
            break;
        case '20':
            min = 10001;
            max = 20000;
            break;
        case '50':
            min = 20001;
            max = 50000;
            break;
        case '100':
            min = 50001;
            max = 100000;
            break;
        case '200':
            min = 100001;
            max = 200000;
            break;
        case '500':
            min = 200001;
            max = 500000;
            break;
        case '501':
            min = 500001;
            max = 50000000;
            break;
        default:
            alert($('#select_by_inh').val());
    }

    $.ajax({
        type:'GET',
        url:'editing/inh',
        data:{
            lower: min,
            upper: max
        },
        success: produce_table
    });
})

function produce_table(data) {
    var district_html =
        "<tr> " +
            "<th>Gmina</th> " +
            "<th>" + $("#first_cand").text() + "</th> " +
            "<th>" + $("#second_cand").text() + "</th> " +
       "</tr>";
    var parsed_data = JSON.parse(data);
    for(i = 0; i < parsed_data.length; i++) {
        var votes_for_second = parsed_data[i].fields.relevant_votes - parsed_data[i].fields.votes_for_first;
        district_html += "<tr> " + "<td class='dis_name'>" + parsed_data[i].fields.Name + "</td>" + "<td>" + "<input type='text' value='" +
            parsed_data[i].fields.votes_for_first + "' class='vote_input1' />" + "</td>" + "<td>" + "<input type='text' value='" +
            votes_for_second + "' class='vote_input2' />" + "</td>" + "<td class='ss'>" + "<button class='save_button'>Zapisz</button>" + "</td>" + "</tr>";
    }
    $('#modal_table').html(district_html);
    $('.modal').show();
}