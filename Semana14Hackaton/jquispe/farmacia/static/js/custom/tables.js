$(document).ready(function() {
    /* CHECKBOX */
    var lista = []; // lista de elementos con checks

    /* Select/Deselect all checkboxes in tables */
    $('thead input:checkbox').click(function() {
        var checkedStatus   = $(this).prop('checked');
        var table           = $(this).closest('table');

        $('tbody input:checkbox', table).each(function() {
            $(this).prop('checked', checkedStatus);
        });

        lista = [];

        $('#datatable tbody input:checkbox').first().change();
    });

    $('#datatable tbody input:checkbox').change(function(event) {
        lista = [];

        $('#datatable tbody input:checkbox:checked').each(function(index, el) {
            lista.push($(this).closest('tr').attr('data-id'));
        });
    });


    /* ELIMINAR ITEMS DE LA LISTA */
    $('#delete-button').click(function(event) {
        event.preventDefault();
        var url = $(this).attr('href'),
            url_redirect = $(this).attr('data-redirect');

        if (lista.length > 0) {
            window.location.replace(url_redirect + '?items=' + lista.join(','));
        }
    });

    /* EXPORTAR */
    $('#export-xls').click(function(event) {
        event.preventDefault();
        var url = $(this).attr('href');
        if (lista.length > 0) {
            window.location.replace(url + '?items=' + lista.join(','));
        }
    });

    // cambio en el numero de items por página
    $('#input_num_pag').change(function(event) {
        event.preventDefault();
        var pag_num = $(this).val(),
            q       = $('#search-input').val();

        actualiza_filtros(pag_num, 1, q)
    });

    // cambio en el número de página
    $('.pag').click(function(event) {
        event.preventDefault();
        var pag_num = $('#input_num_pag').val(),
            pag     = $(this).attr('data-page'),
            q       = $('#search-input').val(),
            tipo = $('#filtro-tipo').val();

        actualiza_filtros(pag_num, pag, q, tipo)
    });

    // inicializa el paginado actual
    var paginas_por_pantalla = $('#input_num_pag').attr('data-page');
    $('#input_num_pag').val(paginas_por_pantalla)

    // búsqueda
    $('#search-input').keyup(function(e){
        var pag_num = $('#input_num_pag').val(),
            pag     = 1,
            q       = $(this).val();

        if(e.keyCode == 13)
        {
            actualiza_filtros(pag_num, pag, q)
        }
    });

    $('.btn-icon-search').click(function(event) {
        var pag_num = $('#input_num_pag').val(),
            pag     = 1,
            q       = $('#search-input').val();

        actualiza_filtros(pag_num, pag, q)
    });
});