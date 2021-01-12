let cardArr= [];
let clicks= 0;

$(document).ready(function name(params) {
    var getUrl= "/get/card/" + cat
    $.ajax({
        type: "GET",
        url: getUrl,
        datatype: "json",
        success: function (params) {
            for(let i =0; i < Object.keys(params).length; i++){
                cardArr.push(params[i])
            }
            setCard(clicks)
        }
    })
});

$(document).on('click', '.card',function (params) {
    getRotation(true) 
});

$(document).on('click', '#btn_next', function (params) {
    getRotation(false)
    setTimeout(function (params) {
        if(clicks < cardArr.length -1){
            clicks += 1;
        }else{
            clicks=0;
        }
        setQuestion(clicks)
    }, 700)
})

$(document).on('click', '#btn_prev', function (params) {
    getRotation(false)
    setTimeout(function (params) {
        if(clicks < 1){
            clicks= cardArr.length -1
        }else{
            clicks -= 1
        }
        setQuestion(clicks)    
    }, 700)
})

$(document).on('click', '#btn_back', function (params) {
    window.location.replace('/categories')
})

$(document).on('mouseenter', '.card', function (params) {
    $('.card').css('transform', 'rotateY(180deg)')
})

$(document).on('mouseleave', '.card', function (params) {
    $('.card').css('transform', 'rotateY(0deg)')
})

function setCard(params) {
    var card_text= $('#h1_question').text()
   if(card_text === '') {
       $('#h1_question').text(cardArr[params].question)
       $('#h1_answer').text(cardArr[params].answer)
       $('#delete_card').attr('href', '/delete/' + cardArr[params].id)
   }else if(card_text  === cardArr[params].question){
       $('#h1_question').text(cardArr[params].answer)
   }else{
       $('#h1_question').text(cardArr[params].question)
       $('#h1_answer').text(cardArr[params])
       $('#delete_card').attr('href', '/delete/' + cardArr[params].id)
   }
}

function setQuestion(params){
    $('#h1_question').text(cardArr[params].question)
    $('#h1_answer').text(cardArr[params].answer)
    $('#delete_card').attr('href', '/delete/' + cardArr[params].id)
}

function getRotation(allowRotation){
    var elID= document.getElementById('card')
    var z=window.getComputedStyle(elID, null).getPropertyValue('transform')
    if(z === 'none' && allowRotation ||
        z === 'matrix(1, 0, 0, 1, 0, 0)' && allowRotation){
        $('.card').css("transform", "rotateY(180deg)")
    }else{
        $('.card').css("transform", "none")
    }
}