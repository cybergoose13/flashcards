let cardArr= []
let clicks= 1;

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


$(document).on('click', '.swipe-wrap',function (params) {
    setCard(clicks)
});

$(document).on('click', '#btn_next', function (params) {
    
    if(clicks < cardArr.length -1){
        clicks += 1;
    }else{
        clicks=0;
    }
    setQuestion(clicks)
})

function setCard(params) {
    var card_text= $('#h1_question').text()
   if(card_text === '') {
       $('#h1_question').text(cardArr[params].question).css("color","blue")
   }else if(card_text  === cardArr[params].question){
       $('#h1_question').text(cardArr[params].answer).css("color", "green")
   }else{
       $('#h1_question').text(cardArr[params].question).css("color", "blue")
   }
}

function setQuestion(params){
    $('#h1_question').text(cardArr[params].question).css("color", "blue")
}