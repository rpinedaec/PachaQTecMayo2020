$(document).ready(function() { 
    console.log("Cargado!!!")
});

$( "#addCliente" ).on( "click", function(){
    console.log("Agregar Cliente")
    Swal.fire({
        title: 'Agrega un cliente',
        input: 'select',
        inputOptions: {
          clientes
        },
        inputPlaceholder: 'Selecciona un cliente',
        showCancelButton: true
        
      })
      
     

} );


$('#table').bootstrapTable({
    columns: [{
      field: 'id',
      title: 'Item ID'
    }, {
      field: 'name',
      title: 'Item Name'
    }, {
      field: 'price',
      title: 'Item Price'
    }],
    data: [{
      id: 1,
      name: 'Item 1',
      price: '$1'
    }, {
      id: 2,
      name: 'Item 2',
      price: '$2'
    }]
  })