// $(document).ready(function(){

//     $('#solicitud').on('submit', function(e){
//     $.ajax({
//         method:'POST',
//         url:'/documents/{{eachdocument.slug}}/updatedocumentviews/',
//         data:{
//         firstnamevalue:$('#firstname').val(),
//         lastnamevalue:$('#lastname').val(),
//         csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
//         }, 
//     success: function() {alert('Data Successfully Posted');},
//     });
    
//     }
    
//     );
//     });

window.addEventListener("load", (event) => {
    function agregarPasajero(idV, idU){
        let payload={
            viaje_id: idV,
            user_id: idU
        }
        fetch('')
    }
})