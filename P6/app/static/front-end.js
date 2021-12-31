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
    $(function() {
        $.ajax({
            url: '/pokemon/' + id,
            type: 'DELETE',
            dataType: 'json'
        })
        $("tbody").empty();
        $.getJSON('/pokemon').done(ver_datos)
    });
}

function editar(id) {
    $.ajax({
        url: '/pokemon/' + id,
        type: 'PUT',
        dataType: 'json'
    })
}

function aniadir(id) {
    $.ajax({
        url: '/pokemon/' + id,
        type: 'POST',
        dataType: 'json'
    })
}

function ver_datos(datos){
    let htmlString = ''
    
    $.each(datos, function(index, value){
        let p = JSON.parse(value)
        
        htmlString += `<tr>`
        htmlString += `<td>${p.num}</td>`
        htmlString += `<td>${p.name}</td>`
        htmlString += `<td><img src="${p.img}" width="120" height="120"></img></div></td>`
        htmlString += `<td>${p.type}</td>`
        htmlString += `<td>${p.height}</td>`
        htmlString += `<td>${p.weight}</td>`
        htmlString += `<td>${p.weaknesses}</td>`
        
        if(p.hasOwnProperty('prev_evolution')){
            htmlString += `<td>`
            $.each(p.prev_evolution, function(i, v){
                htmlString += `${v.num}: ${v.name}<br/>`
            });
            htmlString += `</td>`
        }
        else 
            htmlString += `<td></td>`

        if(p.hasOwnProperty('next_evolution')){
            htmlString += `<td>`
            $.each(p.next_evolution, function(i, v){
                htmlString += `${v.num}: ${v.name}<br/>`
            });
            htmlString += `</td>`
        }
        else 
            htmlString += `<td></td>`
        
        htmlString += `<td>`
        htmlString += `<a class="btn btn-warning btn-sm" onclick="editar('${p.num}')">Editar</a>`
        htmlString += `<br/>`
        htmlString += `<a class="btn btn-danger btn-sm" onclick="eliminar('${p.num}')">Eliminar</a>`
        htmlString += `</td>`
        htmlString += `</tr>`
    });
    $("tbody").append(htmlString)
}

function ver(dato){
    let htmlString = ''
    console.log(dato)
    
    let p = dato
    console.log(p.num)
        
        htmlString += `<tr>`
        htmlString += `<td>${p.num}</td>`
        htmlString += `<td>${p.name}</td>`
        htmlString += `<td><img src="${p.img}" width="120" height="120"></img></div></td>`
        htmlString += `<td>${p.type}</td>`
        htmlString += `<td>${p.height}</td>`
        htmlString += `<td>${p.weight}</td>`
        htmlString += `<td>${p.weaknesses}</td>`
        
        if(p.hasOwnProperty('prev_evolution')){
            htmlString += `<td>`
            $.each(p.prev_evolution, function(i, v){
                htmlString += `${v.num}: ${v.name}<br/>`
            });
            htmlString += `</td>`
        }
        else 
            htmlString += `<td></td>`

        if(p.hasOwnProperty('next_evolution')){
            htmlString += `<td>`
            $.each(p.next_evolution, function(i, v){
                htmlString += `${v.num}: ${v.name}<br/>`
            });
            htmlString += `</td>`
        }
        else 
            htmlString += `<td></td>`
        
        htmlString += `<td>`
        htmlString += `<a class="btn btn-warning btn-sm" onclick="editar('${p.id}')">Editar</a>`
        htmlString += `<br/>`
        htmlString += `<a class="btn btn-danger btn-sm" onclick="eliminar('${p.id}')">Borrar</a>`
        htmlString += `</td>`
        htmlString += `</tr>`
    
    $("tbody").append(htmlString)
}

$(function () {
    $.getJSON('/pokemon').done(ver_datos);
    
    $("#buscar_num").change(function() {
        let value = $(this).val();
        let url = '/pokemon/' + value
        console.log(url);
        $("tbody").empty();
        
        $.getJSON(url).done(ver);
    });
    
});
