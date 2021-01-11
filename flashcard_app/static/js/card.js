let cardArr= []
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

$(document).on('click', '.title', function (params) {
    window.location.replace('/')
})

$(document).on('click', '.card',function (params) {
    // setCard(clicks)
    $('.card').css("transform", "rotateY(-180deg)")
});

$(document).on('click', '#btn_next', function (params) {
    
    if(clicks < cardArr.length -1){
        clicks += 1;
    }else{
        clicks=0;
    }
    setQuestion(clicks)
})

$(document).on('click', '#btn_prev', function (params) {
    if(clicks < 1){
        clicks= cardArr.length -1
    }else{
        clicks -= 1
    }
    setQuestion(clicks)
})

function setCard(params) {
    var card_text= $('#h1_question').text()
   if(card_text === '') {
       $('#h1_question').text(cardArr[params].question)
       $('#h1_answer').text(cardArr[params].answer)
   }else if(card_text  === cardArr[params].question){
       $('#h1_question').text(cardArr[params].answer)
   }else{
       $('#h1_question').text(cardArr[params].question)
       $('#h1_answer').text(cardArr[params])
   }
}

function setQuestion(params){
    $('#h1_question').text(cardArr[params].question).css("color", "blue")
    $('#h1_answer').text(cardArr[params].answer)
}