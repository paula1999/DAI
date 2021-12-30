function modo_diurno () {
    document.body.style.color = 'black';
    document.body.style.backgroundColor = "transparent";
}

function modo_nocturno () {
    document.body.style.color = 'white';
    document.body.style.backgroundColor = '#333';
}

function aumentar_tam() {
    document.body.style.fontSize = "150%"

}

function disminuir_tam() {
    document.body.style.fontSize = "50%"
}

function eliminar(id) {
    $.ajax({
        url: '/pokemon/' + id,
        type: 'DELETE',
        dataType: 'json'
    })
}

function ver(datos){
    $.each(datos, function(index, value){
        htmlString = `<tr>`
        htmlString += `<td>${value['num']}</td>`
        htmlString += `<td>${value['name']}</td>`
        htmlString += `<td>${value['img']}</td>`
        htmlString += `<td>${value['type']}</td>`
        htmlString += `<td>${value['height']}</td>`
        htmlString += `<td>${value['weight']}</td>`
        htmlString += `<td>${value['weaknesses']}</td>`

        if(value.hasOwnProperty('prev_evolution')){
            htmlString += `<td>${value['prev_evolution']}</td>`
        }

        if(value.hasOwnProperty('next_evolution')){
            htmlString += `<td>${value['next_evolution']}</td>`
        }
        
        htmlString += `<td> <a class="btn btn-danger btn-sm" onclick="eliminar('${value.id}')">Borrar</a></td>`
        htmlString += `</tr>`
        
        $("tbody").append(htmlString)
    });
}

$(function () {
    $.getJSON('/pokemon').done(ver);
    $("#buscar_num").change(function() {
        let value = $(this).val();
        console.log(value);
        $("tbody").empty();
        $.getJSON('/pokemon', {
            num: value
        }).done(ver);
    });
});
