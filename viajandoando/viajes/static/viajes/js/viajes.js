$(document).ready(function () {
    $(".boton-ver-mas").click(function (e) { 
        e.preventDefault();
        var idViaje = $(this).data("viaje-id");
        $.ajax({
            type: "get",
            url: "/api/viajes/" + idViaje,
            data: {"id":idViaje},
            dataType: "json",
            success: function (response) {
                $(".modal-title").html(response.conductor_nombre);
                $(".modal-body-descripcion").html("Descripcion: " + response.descripcion);
                $(".modal-body-fecha").html("Fecha: " + response.fecha);
                $(".modal-body-hora").html("Horario: " + response.hora);
                $(".modal-body-imagen").html('<img src="/media/' + response.imagen_vehiculo + '" alt="Auto" style="width: 90%;" />');
            }
        });
    });
    // $(".boton-solicitar-unirse").click(function (e) { 
    //     e.preventDefault();
    //     var idSolicitud = $(this).data("solicitud-id");
    //     $.post("viajes.html", data,
    //         function (data, textStatus, jqXHR) {
    //         },
    //         "dataType"
    //     );
    //     $.ajax({
    //         type: "post",
    //         url: "/viajes",
    //         data: {"id":idSolicitud},
    //         dataType: "dataType",
    //         success: function (response) {  
    //         }
    //     });
    // });
});