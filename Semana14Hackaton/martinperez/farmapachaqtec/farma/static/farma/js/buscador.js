
  function __init()
  {
      var Products = Productos 
      $('#search_input')
          .val('')
          .focus()
          .keyup(function(){
              if(!$.trim($(this).val())){
                  $('.results .error').empty().hide();
                  $('.results .wrapper').empty();
              }
          });
  
      $('#search_input').autocomplete({
          minLength: 1,
          select: function( event, ui ) {
              return false;
          },
          open: function() {
              //$('.results .wrapper').html($(this).autocomplete("widget").html());
              $('.results .form-control').html($(this).autocomplete("widget").html());
              $(this).autocomplete("widget").hide();
          },
          source: function( request, response ) {
              var data = [];
              for(var x in Products)
              {
                  if(Products[x].nombre.match(request.term.toUpperCase()) || Products[x].ingredienteActivo.match(request.term.toUpperCase()))
                      data.push(Products[x]);
              }
              response(data);
          },
          response: function(event, ui) {
  
              if (ui.content.length === 0) {
                  $('.results .error').html('No se encontraron resultados').show();
                  $('.results .wrapper').empty();
              }
              else
                  $('.results .error').empty().hide();
          }
      }).autocomplete('instance')._renderItem = function(ul, item) {
        return $('<option value="'+item.id+'">'+item.nombre+'  <b>stock: '+item.stock+'</b>  ingrediente-Activo: '+item.ingredienteActivo+'</option>')
            .data('item.autocomplete', item)
            .appendTo(ul);
          
        //   var prod_tmpl = $('<div />') 
        //                 // .addClass('prod')
        //                 // .append('<a href="#" />').find('a').addClass('nombre').html(item.nombre)
        //                 // .parent()
        //                 // .append('</a><br><span class="ingrediente"><strong>INGREDIENTE:</strong><span></span></span>')
        //                 // .find('.ingrediente > span').append(item.ingredienteActivo)
        //                 // .parent().parent()
        //                 // .append('&nbsp;&nbsp;<span class="costo"><strong>Costo:</strong><span></span></span>')
        //                 // .find('.costo > span').append(item.costo)
        //                 // .parent().parent(); 
        //                 .addClass('prod')
        //                 .append('<option value="'+item.id+'">'+item.nombre+'</option>')
        //                 .parent() 
        //   return $('<div></div>')
        //       .data('item.autocomplete', item)
        //       .append(prod_tmpl)
        //       .appendTo(ul);
      };
  }
  
  $(document).ready(__init);
  