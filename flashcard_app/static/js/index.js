$(document).ready(function (params) {
    
})

$(document).on('click', '.box', function (params) {
    if($(this).attr('id') === 'add'){
        window.location.replace("new")
    }else if($(this).attr('id') === 'decks'){
        window.location.replace("categories")
    }
    
})