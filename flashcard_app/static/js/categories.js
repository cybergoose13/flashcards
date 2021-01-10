$(document).on('click', '#title', function (params) {
    window.location.replace("/")
})

$(document).on('click', '.cat-card', function (params) {
    var id= $(this).attr('id')
    window.location.replace('/card/' + id)
})