/*$(document).ready(function() {    
});*/

$("#addCliente").on("click", function(){
    Swal.fire({
      title: '<strong>Cliente</strong>',
      icon: 'info',
      html:
        '<select name="hall" id="cmbCliente"></select>',
      showCloseButton: true,
      showCancelButton: true,
      focusConfirm: false,
      confirmButtonText:
        'Guardar',
      confirmButtonAriaLabel: 'Guardar',
      cancelButtonText:
        'Cancelar',
      cancelButtonAriaLabel: 'Thumbs down'
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
    $("#addressCliente").html("<strong>"+element.nombres + element.apellidos +"</strong> &nbsp"+
      element.direccion +"&nbsp"+
      "Phone:" + element.telefono +"&nbsp"+
      "Email:" + element.email);
      $("#addressCliente").show();

  }
});
}

$("#addTrasportista").on( "click", function(){
  Swal.fire({
    title: '<strong>Transportista</strong>',
    icon:  'info',
    html:  '<select name="hall" id="cmbTransportista"></select>',
    showCloseButton: true,
    showCancelButton: true,
    focusConfirm: false,
    confirmButtonText:
      'Guardar',
    confirmButtonAriaLabel: 'Guardar',
    cancelButtonText:
      'Cancelar',
    cancelButtonAriaLabel: 'Thumbs down'
  }).then((result) => {
    if (result.value) {
      var idTransportista = $("#cmbTransportista").find(":selected").val();
      dibujarTransportista(idTransportista);
      Swal.fire(
        'Guardado!',
        'Transportista guardado',
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
  $("#addressTransportista").html("<strong>"+element.nombres + element.apellidos +"</strong> &nbsp"+
    element.direccion +"&nbsp"+
    "Doc:" + element.documento);
    $("#addressTransportista").show();
}
});
}
/*
$( "#addProducto" ).on( "click", function(){


  Swal.fire({
    title: '<strong>Producto</strong>',
    icon: 'info',
    html:
      '<select name="hall" id="cmbProducto"></select>' +'<br>Cantidad:',
      //'<input id  = "cantidadProducto"></input>
    showCloseButton: true,
    input: 'text',
    inputValue: "1",
    showCancelButton: true,
    focusConfirm: false,
    confirmButtonText:'Guardar',
    confirmButtonAriaLabel: 'Guardar',
    cancelButtonText: 'Cancelar',
    cancelButtonAriaLabel: 'Thumbs down',
    inputValidator: (value) => {
      if (!value) {
        return 'Necesita ingresar una cantidad!'
      }
      if(value){
        var idProducto = $("#cmbProducto").find(":selected").val();
        var cantidad2 = value;
        var confirm = false
        var confirmP = true
        dataDetalletemp = $table.bootstrapTable('getData')
        Productos.forEach(element => { 
          if(element.id==idProducto && element.stock>=cantidad2){ 
            confirm = true
            dataDetalletemp.forEach(element2 => {  
              if(element2.name==element.nombre){
                confirmP = false                
              }
            });
          }
        });
        if(!confirm){
          return 'Verificar Cantidad.'
        }
        if(!confirmP){
          return 'El producto ya esta agregado'
        }
      }
    }
  }).then((result) => {
    if (result.value) {
      var idProducto = $("#cmbProducto").find(":selected").val(); 
      var cantidad2 = result.value; 
      dibujarProducto(idProducto, cantidad2);
      confirm = true
      Swal.fire(
        'Guardado!',
        'Producto guardado',
        'success'
      ) 
    }
  })
 

  Productos.forEach(element => {
    $('#cmbProducto').append(new Option(element.nombre + " STOCK:" +element.stock + "  ",element.id))
  });

} );
*/

$("#addProductoNuevo").on("click", function(){
  var idProducto = $("#form-control").find(":selected").val();
  if (idProducto>0){
    var cantidad2 = $("#cant_input").val(); 
    var confirm = false
    var confirmP = true
    dataDetalletemp = $table.bootstrapTable('getData')
    Productos.forEach(element => { 
      if(element.id==idProducto && element.stock>=cantidad2){ 
        confirm = true
        dataDetalletemp.forEach(element2 => {  
          if(element2.name==element.nombre){
            confirmP = false                
          }
        });
      }
    });
    if(!confirm){
      $("#mensajeError").html("Verificar Cantidad.");
      $("#mensajeError").show();
      setTimeout(function() {
        $("#mensajeError").fadeOut();           
      },3000);    
    }else{
      if(!confirmP){
        $("#mensajeError").html("El producto ya esta agregado");
        $("#mensajeError").show();  
        setTimeout(function() {
          $("#mensajeError").fadeOut();           
        },3000);
      }else{
        dibujarProducto(idProducto, cantidad2);
      }
    }
  }else{
    $("#mensajeError").html("Seleccionar un producto, utilice la casilla de filtro.");
    $("#mensajeError").show();  
    setTimeout(function() {
      $("#mensajeError").fadeOut();           
    },3000);
    
  }
    



});



var dataDetalle=[]
var total = 0.0
var subtotal = 0.0
var igv = 0.0 
function dibujarProducto(idProducto, cantidad2){
  
  Productos.forEach(element => {
if(element.id == idProducto){
  var CantidadMasUno = $table.bootstrapTable('getData').length + 1
  var cantidad = cantidad2;
  $table.bootstrapTable('insertRow', {
    index: 1,
    row: {
      id: element.id,
      item: CantidadMasUno,
      cant: cantidad,
      name: element.nombre,
      price: '$' + element.costo,
      total: cantidad * element.costo, 
      igv: element.igv
    }
  })

  var tableData = document.getElementById('table').getElementsByTagName('tbody').item(0);
  var rowData = tableData.getElementsByTagName('tr');            
  for(var i = 0; i < rowData.length - 1; i++){
      for(var j = 0; j < rowData.length - (i + 1); j++){
          if(parseInt(rowData.item(j).getElementsByTagName('td').item(0).innerHTML) > parseInt(rowData.item(j+1).getElementsByTagName('td').item(0).innerHTML)){
            tableData.insertBefore(rowData.item(j+1),rowData.item(j));
      }
    }
  }
  
  dataDetalle = $table.bootstrapTable('getData')
  //console.log(dataDetalle)
   total = 0.0
   subtotal = 0.0
   igv = 0.0 
  dataDetalle.forEach(element => {
    //console.log(element)
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
      title: 'Item ID',
      visible: false
    },
    {
      field: 'item',
      title: 'Item'
    },{
      field: 'cant',
      title: 'Cantidad'
    }, {
      field: 'name',
      title: 'Producto'
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
    if (idClienteSeleccionado>0){
      if (idTransportistaSeleccionado>0){
        var CantidadFilas =  $table.bootstrapTable('getData').length;
        if(CantidadFilas>0){
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
          
          var url = "setPedido" 
          $.ajax({
            type: "POST",
            url: url,
            data: JSON.stringify(pedido),
            success: function(data){
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


          dataDetalle.forEach(elementD => {
            Productos.forEach(elementP => {
              if(elementD.id==elementP.id){
                var cantidadTotal = elementP.stock - elementD.cant;
                producto = {
                  "id" : elementD.id,
                  "stock" : cantidadTotal
                }
                urlP='setProductoStock'
                console.log(producto) 
                $.ajax({
                  type: "POST",
                  url: urlP,
                  data: JSON.stringify(producto),
                  success: function(data){
                    if(!data.error){
                      console.log('Exito!')
                    }else{
                      console.log('sin exito!')
                    }
                  }
                });
              }
            });
          });
          /*
          setTimeout(function() {
            //return redirect('nuevo');
            return render(request,'nuevo', context)         
          },3000); */

        }else{
          $("#mensajeErrorGeneral").html("Ingresar productos.");
          $("#mensajeErrorGeneral").show();
          setTimeout(function() {
            $("#mensajeErrorGeneral").fadeOut();           
          },3000);
          return
        }
      }else{    
        $("#mensajeErrorGeneral").html("Verificar Transportista.");
        $("#mensajeErrorGeneral").show();
        setTimeout(function() {
          $("#mensajeErrorGeneral").fadeOut();           
        },3000);
        return
      }
    }else{ 
      $("#mensajeErrorGeneral").html("Verificar Cliente.");
      $("#mensajeErrorGeneral").show();
      setTimeout(function() {
        $("#mensajeErrorGeneral").fadeOut();           
      },3000); 
      return
      //document.getElementById("addCliente").click();
    }
    

  });





////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////FILTROS///////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function filterFloat(evt,input){
  // Backspace = 8, Enter = 13, ‘0′ = 48, ‘9′ = 57, ‘.’ = 46, ‘-’ = 43
  var key = window.Event ? evt.which : evt.keyCode;    
  var chark = String.fromCharCode(key);
  var tempValue = input.value+chark;
  if(key >= 48 && key <= 57){
      if(filter(tempValue)=== false){
          return false;
      }else{       
          return true;
      }
  }else{
        if(key == 8 || key == 13 || key == 0) {     
            return true;              
        }else if(key == 46){
              if(filter(tempValue)=== false){
                  return false;
              }else{       
                  return true;
              }
        }else{
            return false;
        }
  }
}
function filter(__val__){
  var preg = /^([0-9]+\.?[0-9]{0,2})$/; 
  if(preg.test(__val__) === true){
      return true;
  }else{
     return false;
  }
  
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////FILTROS///////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
