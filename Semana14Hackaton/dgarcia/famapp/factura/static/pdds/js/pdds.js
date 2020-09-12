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
var idClienteSeleccionado;
function dibujarCliente(idCliente){
idClienteSeleccionado = idCliente
clientes.forEach(element => {
if(element.id == idCliente){
  $("#addressCliente").html("<strong>"+element.nombres + element.apellidos +"</strong><br>");
    $("#addressCliente").show();

}
});
}

$( "#addTrasportista" ).on( "click", function(){


console.log("Agregar Tecnico")
Swal.fire({
  title: 'Escoje el Tecnico',
  text: "Escoja un Tecnico",
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
      'Tu Tecnico se ha guardado',
      'success'
    )
  }
})

Transportistas.forEach(element => {

  $('#cmbTransportista').append(new Option(element.nombres ,element.id))
});

} );
var idTransportistaSeleccionado;
function dibujarTransportista(idTransportista){
idTransportistaSeleccionado = idTransportista
Transportistas.forEach(element => {
if(element.id == idTransportista){
$("#addressTransportista").html("<strong>"+element.nombres +"</strong><br>");
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
var dataDetalle=[]
var total = 0.0
var subtotal = 0.0
var igv = 0.0 
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
    total: cantidad * element.costo, 
    igv: element.igv
  }
})

dataDetalle = $table.bootstrapTable('getData')
console.log(dataDetalle)
 total = 0.0
 subtotal = 0.0
 igv = 0.0 
dataDetalle.forEach(element => {
  console.log(element)
  subtotal += element.total
  if(element.igv){
    igv += element.total * 0.18
  }
  total = subtotal + igv
});
$("#subtotal").text(subtotal)
$("#igv").text(igv)
$("#total").text(total)

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

$( "#sendPedido" ).on( "click", function(){
  pedido = {}
  
  cab = {
    cliente : idClienteSeleccionado,
    transportista : idTransportistaSeleccionado,
    fecha : fecha,
    subtotal : subtotal,
    igv : igv,
    total : total
  }
  dataDetalle = $table.bootstrapTable('getData')
  pedido.det = dataDetalle
  pedido.cab = cab
  console.log(JSON.stringify(pedido))
  var url = "setPedido"
  
   $.ajax({
    type: "POST",
    url: url,
    data: JSON.stringify(pedido),
    success: function(data){
      console.log(data)
      if(!data.error){
        Swal.fire(
          'Exito!',
          'se creo el pedido.'+ data.data,
          'success'
        )
      }else{
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: 'No se pudo procesar tu pedido!',
         
        })
      }
    }
  });

});