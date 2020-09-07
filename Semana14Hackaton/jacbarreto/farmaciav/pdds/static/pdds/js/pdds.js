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
        '<br>Cliente: '+
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

    Clientes.forEach(element => {
      $('#cmbCliente').append(new Option(element.nombre + ", "+ element.apellidos,element.id))
    });
  
} );
var idClienteSeleccionado;
function dibujarCliente(idCliente){
  idClienteSeleccionado = idCliente
Clientes.forEach(element => {
  if(element.id == idCliente){
    $("#addressCliente").html("<strong>" + element.nombre + ", "+ element.apellidos +"</strong><br>"+
      "Dirección: " + element.direccion +"<br>"+
      "Telefono :" + element.telefono +"<br>"+
      "Email: " + element.email);
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
var idTransportistaSeleccionado;
function dibujarTransportista(idTransportista){
  idTransportistaSeleccionado = idTransportista
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
      '<br>Producto: '+
      '<select name="hall" id="cmbProducto"></select>'+
      '<br>Cantidad: '+
      '<input id  = "cantidadProducto" width="10px"></input>',
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
          price: element.costo,
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

      if(subtotal > 10){
        puntos = Math.trunc(subtotal / 10)
      } else {
        puntos = subtotal / 10
      }
    
      txtIGV = igv.toFixed(2)
      txtSubtotal = subtotal.toFixed(2)
      txtTotal = total.toFixed(2)

      $("#subtotal").text(txtSubtotal)
      $("#igv").text(txtIGV)
      $("#total").text(txtTotal)
      $("#lblPuntos").text(puntos)
    
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
      title: 'Nombre Producto'
    }, {
      field: 'price',
      title: 'Precio (S/)'
    }, {
      field: 'total',
      title: 'Total'
    }]
  })
  var $table = $('#table')
  var puntos = $("#lblPuntos").value

  $( "#sendPedido" ).on( "click", function(){    
    pedido = {}

    dataCab = {
      /*cliente : idClienteSeleccionado,
      vendedor : idTransportistaSeleccionado,*/
      idCliente : idClienteSeleccionado,
      idVendedor : 1,
      fecha : fecha,
      subtotal : subtotal,
      igv : igv,
      total : total,
      puntos : puntos
    }
    
    dataDetalle = $table.bootstrapTable('getData')
    pedido.det = dataDetalle
    pedido.cab = dataCab
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
            'se creo el pedido '+ data.data,
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

  $( "#printPage" ).on( "click", function(){
    window.print()
  });

  $( "#generatePDF" ).on( "click", function(){
    window.print()
  });