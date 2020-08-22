$(document).ready(function() { 
    console.log("Cargado!!!")
});

$( "#addCliente" ).on( "click", function(){


    console.log("Agregar Cliente")
    Swal.fire({
      title: 'Escoje el cliente',
      text: "Escoja un cliente",
      icon: 'success',
      html:
        '<select name="hall" id="cmbCliente"></select>',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Guardar'
    }).then((result) => {
      if (result.value) {
        var idCliente = $("#cmbCliente").find(":selected").val();
        dibujarCliente(idCliente);
        Swal.fire(
          'Guardado!',
          'Tu cliente se ha guardado',
          'success'
        )
      }
    })

    clientes.forEach(element => {

      $('#cmbCliente').append(new Option(element.nombres + " "+ element.apellidos ,element.id))
    });
  
} );

function dibujarCliente(idCliente){
clientes.forEach(element => {
  if(element.id == idCliente){
    $("#addressCliente").html("<strong>"+element.nombres + element.apellidos +"</strong><br>"+
      element.direccion +"<br>"+
      "Phone:" + element.telefono +"<br>"+
      "Email:" + element.email);
      $("#addressCliente").show();

  }
});
}

$( "#addTrasportista" ).on( "click", function(){


  console.log("Agregar Transportista")
  Swal.fire({
    title: 'Escoje el Transportista',
    text: "Escoja un Transportista",
    icon: 'success',
    html:
      '<select name="hall" id="cmbTransportista"></select>',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Guardar'
  }).then((result) => {
    if (result.value) {
      var idTransportista = $("#cmbTransportista").find(":selected").val();
      dibujarTransportista(idTransportista);
      Swal.fire(
        'Guardado!',
        'Tu Transportista se ha guardado',
        'success'
      )
    }
  })

  Transportistas.forEach(element => {

    $('#cmbTransportista').append(new Option(element.nombres + " "+ element.apellidos ,element.id))
  });

} );

function dibujarTransportista(idTransportista){
  Transportistas.forEach(element => {
if(element.id == idTransportista){
  $("#addressTransportista").html("<strong>"+element.nombres + element.apellidos +"</strong><br>"+
    element.direccion +"<br>"+
    "Phone:" + element.telefono +"<br>"+
    "Email:" + element.email);
    $("#addressTransportista").show();

}
});
}

$( "#addProducto" ).on( "click", function(){


  console.log("Agregar Producto")
  Swal.fire({
    title: 'Escoje el Producto',
    text: "Escoja un Producto",
    icon: 'success',
    html:
      '<select name="hall" id="cmbProducto"></select>'+
      '<br>Agrega la Cantidad'+
      '<input id  = "cantidadProducto"></input>',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Guardar'
  }).then((result) => {
    if (result.value) {
      var idProducto = $("#cmbProducto").find(":selected").val();
      dibujarProducto(idProducto);
      Swal.fire(
        'Guardado!',
        'Tu Producto se ha guardado',
        'success'
      )
    }
  })

  Productos.forEach(element => {

    $('#cmbProducto').append(new Option(element.nombre,element.id))
  });

} );

function dibujarProducto(idProducto){
  Productos.forEach(element => {
if(element.id == idProducto){
  var cantidad = $("#cantidadProducto").val();
  $table.bootstrapTable('insertRow', {
    index: 1,
    row: {
      id: element.id,
      cant: cantidad,
      name: element.nombre,
      price: '$' + element.costo,
      total: cantidad * element.costo
    }
  })
  console.log("Encontre el productp!!!!!")
  console.log(element.nombre)
 
}
});
}

$('#table').bootstrapTable({
    columns: [{
      field: 'id',
      title: 'Item ID'
    },
    {
      field: 'cant',
      title: 'Cantidad'
    }, {
      field: 'name',
      title: 'Nombre Prducto'
    }, {
      field: 'price',
      title: 'Precio'
    }, {
      field: 'total',
      title: 'Total'
    }]
  })
  var $table = $('#table')