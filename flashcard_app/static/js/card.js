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
            setH1(clicks)
        }
    })
});

$(document).on('click', function name(params) {
    
    if(clicks < cardArr.length -1){
        clicks += 1;
    }else{
        clicks=0;
    }
    setH1(clicks)
    /*
     * fetch method to get the same results as $.ajax
    ============================
    fetch("/test", {
        headers:{
            'Accept': 'json'
        }
    }).then(res => {
        return res.json()
    }).then(data => {
        console.log(data)
    })
    ===========================
    */
});

function setH1(params) {
    $('#h1_question').text(cardArr[params].question)
}