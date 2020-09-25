


$('#table').bootstrapTable({
    columns: [{
      field: 'id',
      title: 'Item ID'
    },{
      field: 'fecha',
      title: 'Fecha'
    }, {
      field: 'cliente_id',
      title: 'Cliente'
    }, {
      field: 'transportista_id',
      title: 'Transportista'
    }, {
      field: 'subtotal',
      title: 'SubTotal'
    }, {
      field: 'igv',
      title: 'Igv'
    }, {
      field: 'total',
      title: 'Total'
    }]
  })

  
  var $table = $('#table')
  