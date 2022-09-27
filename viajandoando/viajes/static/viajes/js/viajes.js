// function pedir_mostrar_modal_viaje() {
//     $.ajax({url: "/api/obtener_viaje/1"}).done(mostrar_modal_viaje);
// }

// function mostrar_modal_viaje(data) {
//     $("#botonModal").click().html("<p>Cantidad: " + data.descripcion.toString() + "</p>");
// }

$(document).ready(function () {
    $(".boton-ver-mas").click(function (e) { 
        e.preventDefault();
        var idViaje = $(this).data("viaje-id");
        $.ajax({
            type: "get",
            url: "/api/viajes",
            data: {"id":idViaje},
            dataType: "json",
            success: function (response) {
                console.log(response[0])
                $(".modal-title").html("Conductor: "+ response[0].conductor);
                $(".modal-body-descripcion").html("Descripcion: " + response[0].descripcion);
                $(".modal-body-fecha").html("Fecha: " + response[0].datetime);
                $(".modal-body-imagen").html("Imagen vehiculo: " + response[0].imagen_vehiculo);
            }
        });
    });
});