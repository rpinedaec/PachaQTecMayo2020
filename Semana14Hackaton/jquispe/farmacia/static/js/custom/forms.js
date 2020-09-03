$(document).ready(function() {

    /* GUARDAR Y CONTINUAR EDITANDO */
    $('#btn-save-edit').click(function(event) {
        event.preventDefault();
        $('#form').attr('action', '?next=self');
        $('#form').submit();
    });

    /* GUARDAR Y CONTINUAR ACTIVAR */
    $('#btn-save-activate').click(function(event) {
        event.preventDefault();
        $('#form').attr('action', '?next=activar');
        $('#form').submit();
    });

    /* GUARDAR Y REGISTRAR OTRO */
    $('#btn-save-new').click(function(event) {
        event.preventDefault();
        var tipo = $(this).attr('data-tipo');
        var tipo2 = ""
        if (tipo) {
            tipo2="&tipo="+tipo;
        };
        $('#form').attr('action', '?next=new'+tipo2);

        $('#form').submit();
    });

    /* DATEPICKER */
    $('.input-datepicker-custom, .input-daterange-custom').datepicker({
        weekStart: 1,
        todayBtn: 'linked',
        language: 'es',
        endDate: '+0d'
    });

    $('.input-datepicker-close-custom').datepicker({
        weekStart: 1,
        todayBtn: 'linked',
        language: 'es',
    }).on('changeDate', function(e){ $(this).datepicker('hide'); });

    // no se aceptan fechas futuras
    $('.input-datepicker-close-max-today').datepicker({
        weekStart: 1,
        todayBtn: 'linked',
        language: 'es',
        endDate: 'today'
    }).on('changeDate', function(e){ $(this).datepicker('hide'); });

    $('.input-datepicker-close-min-today').datepicker({
        weekStart: 1,
        todayBtn: 'linked',
        language: 'es',
        startDate: 'today'
    }).on('changeDate', function(e){ $(this).datepicker('hide'); });
});

// reemplaza todas las coincidencias en vez de solo la primera
function replaceAll(text, busca, reemplaza){
    while (text.toString().indexOf(busca) != -1)
        text = text.toString().replace(busca, reemplaza);
    return text;
}