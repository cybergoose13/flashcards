$(document).ready(function name(params) {
    console.log("Page is ready.");
});



$(document).on('click', function name(params) {
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
    
    $.ajax({
        type: "GET",
        url: "/test",
        datatype: "json",
        success: function (params) {
            console.log(params)
        }
    })
});