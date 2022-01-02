function modo_diurno () {
    document.body.style.backgroundColor = "transparent";
    document.getElementById("tabla").style.backgroundColor = "transparent";
    document.getElementById("modalAdd").style.backgroundColor = "white";
    document.getElementById("modalEdit").style.backgroundColor = "white";

}

function modo_nocturno () {
    document.body.style.backgroundColor = 'grey';
    document.getElementById("tabla").style.backgroundColor = "grey";
    document.getElementById("modalAdd").style.backgroundColor = "grey";
    document.getElementById("modalEdit").style.backgroundColor = "grey";
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

function updatePokemonItem() {
    const idInput = document.getElementById("edit-id");
    const numInput = document.getElementById("edit-num");
    const nameInput = document.getElementById("edit-name");
    const imgInput = document.getElementById("edit-img");
    const typeInput = document.getElementById("edit-type");
    const heightInput = document.getElementById("edit-height");
    const weightInput = document.getElementById("edit-weight");
    const weaknessesInput = document.getElementById("edit-weaknesses");

    const pokemon = {
        num: numInput.value.trim(),
        name: nameInput.value.trim(),
        img: imgInput.value.trim() ? imgInput.value.trim() : "static/pokemon_unknown.png",
        type: typeInput.value.trim().split(",")[0] ? typeInput.value.trim().split(",")          : ["Desconocido"],
        height: heightInput.value.trim(),
        weight: weightInput.value.trim(),
        weaknesses: weaknessesInput.value.trim().split(",")[0] ? weaknessesInput.value.trim().split(",")          : ["Desconocido"],
    };

    $.ajax({
        url: '/pokemon/' + idInput.value.trim(),
        type: 'PUT',
        dataType: 'json',
        processData: false,
        contentType: 'application/json',
        data: JSON.stringify(pokemon),

        success: function(data) {
            $("tbody").empty();
            $.getJSON('/pokemon').done(ver_datos)
            numInput.value = ""
            nameInput.value = ""
            imgInput.value = ""
            typeInput.value = ""
            heightInput.value = ""
            weightInput.value = ""
            weaknessesInput.value = ""
        },
        error : function(xhr, status) {
            alert('Error, compruebe los campos');
        }
    })
}

function addPokemonItem() {
    const numInput = document.getElementById("add-num");
    const nameInput = document.getElementById("add-name");
    const imgInput = document.getElementById("add-img");
    const typeInput = document.getElementById("add-type");
    const heightInput = document.getElementById("add-height");
    const weightInput = document.getElementById("add-weight");
    const weaknessesInput = document.getElementById("add-weaknesses");

    const pokemon = {
        num: numInput.value.trim(),
        name: nameInput.value.trim(),
        img: imgInput.value.trim() ? imgInput.value.trim() : "static/pokemon_unknown.png",
        type: typeInput.value.trim().split(",")[0] ? typeInput.value.trim().split(",")          : ["Desconocido"],
        height: heightInput.value.trim(),
        weight: weightInput.value.trim(),
        weaknesses: weaknessesInput.value.trim().split(",")[0] ? weaknessesInput.value.trim().split(",")          : ["Desconocido"],
    };

    $.ajax({
        url: '/pokemon',
        type: 'POST',
        dataType: 'json',
        processData: false,
        contentType: 'application/json',
        data: JSON.stringify(pokemon),

        success: function(data) {
            $("tbody").empty();
            $.getJSON('/pokemon').done(ver_datos)
            numInput.value = ""
            nameInput.value = ""
            imgInput.value = ""
            typeInput.value = ""
            heightInput.value = ""
            weightInput.value = ""
            weaknessesInput.value = ""
        },
        error : function(xhr, status) {
            alert('Error, compruebe los campos');
        }
    })
}

function get_pokemon (){
    $.ajax({
        url: '/pokemon/',
        type: 'GET',
        dataType: 'json',
        success: function(data){
            ver_datos(data)
        }
    });
    $("tbody").empty();
    $.getJSON('/pokemon').done(ver_datos)
}

function ver_datos(datos){
    let htmlString = ''
    
    $.each(datos, function(index, value){
        let p = JSON.parse(value)
        
        htmlString += `<tr>`
        htmlString += `<td id="td">${p.num}</td>`
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
        htmlString += `<a href="#editPokemonModal" class="btn btn-warning btn-sm" data-toggle="modal"><span>Editar</span></a>`
        htmlString += `<br/>`
        htmlString += `<a class="btn btn-danger btn-sm" onclick="eliminar('${p.num}')">Eliminar</a>`
        htmlString += `</td>`
        htmlString += `</tr>`
    });
    $("tbody").append(htmlString)
}

function ver(p){
    let htmlString = ''
        
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
    htmlString += `<a href="#editPokemonModal" class="edit" data-toggle="modal">Editar</a>`
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
        if(value == '')
            $.getJSON('/pokemon').done(ver_datos);
        else{
            let url = '/pokemon/' + value
            $("tbody").empty();
            
            $.getJSON(url).done(ver);
        }
    });
    
});
