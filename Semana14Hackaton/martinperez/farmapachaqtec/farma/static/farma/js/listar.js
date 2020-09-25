 

$('#table').bootstrapTable({
    columns: [{
    field: 'item',
    title: 'ITEM'
    },{
    field: 'id',
    title: 'COD'
    },
    {
    field: 'fecha',
    title: 'FECHA'
    }, {
    field: 'subtotal',
    title: 'SUBTOTAL'
    }, {
    field: 'igv',
    title: 'IGV'
    }, {
    field: 'total',
    title: 'TOTAL'
    }, {
    field: 'cliente',
    title: 'CLIENTE'
    }, {
    field: 'transportista',
    title: 'TRANSPORTISTA'
    }]
})
var $table = $('#table')


$(document).ready(
    dibujarCliente()
);

function dibujarCliente(){
    var itemG = 0
    pedidos.forEach(element => {
        itemG=itemG+1
        $table.bootstrapTable('insertRow', {
            index: 1,
            row: {
            item: itemG,
            id: element.id,
            fecha: element.fecha,
            subtotal: element.subtotal,
            igv: element.igv,
            total: element.total, 
            cliente: element.cliente_id, 
            transportista: element.transportista_id
            }
        })
        dataDetalle = $table.bootstrapTable('getData') 
        
    });

        
    var tableData = document.getElementById('table').getElementsByTagName('tbody').item(0);
    var rowData = tableData.getElementsByTagName('tr');            
    for(var i = 0; i < rowData.length - 1; i++){
        for(var j = 0; j < rowData.length - (i + 1); j++){
            if(parseInt(rowData.item(j).getElementsByTagName('td').item(0).innerHTML) > parseInt(rowData.item(j+1).getElementsByTagName('td').item(0).innerHTML)){
                tableData.insertBefore(rowData.item(j+1),rowData.item(j));
        }
        }
    }
    
}