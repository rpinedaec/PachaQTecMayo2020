$(document).ready(function() { 
    console.log("Cargado!!!")
});

$( "#addCliente" ).on( "click", function(){

  clientes.forEach(element => {
    $('#cmbCliente').append(new Option(element.id, element.nombres))
  });

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
        Swal.fire(
          'Guardado!',
          'Tu cliente se ha guardado',
          'success'
        )
      }
    })
    clientes.forEach(element => {
      console.log(element);
      $('#cmbCliente').append(new Option(element.nombre,element.id))
    });
  
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