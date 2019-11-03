$(document).ready(function(){
     $('.ver_categorias').click(function(){

        var categoria = parseInt(jQuery(".categoria").css("height"));
        if(categoria == 0){
            $('.categoria').css({"height":40});

             $('.ver_categorias i').css({"transform":'rotate(180deg)'});
        }
         else{
             $('.categoria').css({"height":0});
            $('.ver_categorias i').css({"transform":'rotate(0deg)'});
         }
    });

    //Creamos un interval para x tiempo
    setInterval(function(){
        //Guardamos en una variable el ancho de el slider
        var ancho =  parseInt($('.repre').width());

        //Contamos la cantidad de divs que hay dentro del slider y le quitamos 1 invisible
        var cantidad = $(".slider").length;
        var cantidad = cantidad - 1;

        //Obtenemos el ancho de la linea desplazadora del slider y la transformamos a negativo
        var linea = ancho * cantidad;
        var linea = parseInt('-' + linea);

        //Sacamos cuanto margin-left tiene la linea
        var linea_margin = parseInt(jQuery(".repre_cont").css("margin-left"));

        //Guardamos en una variable el resultado de cada operacion
        var resultado = linea_margin - ancho;

        var resultado2 = 0;
        //Hacemos una condicion
        if(linea_margin <= linea){
            $('.repre_cont').css({"margin-left":resultado2});
        }
        else{
            $('.repre_cont').css({"margin-left":resultado});
        }
    }, 8000);

    $(".repre_right").click(function(){
        //Guardamos en una variable el ancho de el slider
        var ancho =  parseInt($('.repre').width());

        //Contamos la cantidad de divs que hay dentro del slider y le quitamos 1 invisible
        var cantidad = $(".slider").length;
        var cantidad = cantidad - 1;

        //Obtenemos el ancho de la linea desplazadora del slider y la transformamos a negativo
        var linea = ancho * cantidad;
        var linea = parseInt('-' + linea);

        //Sacamos cuanto margin-left tiene la linea
        var linea_margin = parseInt(jQuery(".repre_cont").css("margin-left"));

        //Guardamos en una variable el resultado de cada operacion
        var resultado = linea_margin - ancho;

        var resultado2 = 0;
         if(linea_margin <= linea){

        }
        else{
            $('.repre_cont').css({"margin-left":resultado});
        }
    });

     $(".repre_left").click(function(){
        //Guardamos en una variable el ancho de el slider
        var ancho =  parseInt($('.repre').width());

        //Contamos la cantidad de divs que hay dentro del slider y le quitamos 1 invisible
        var cantidad = $(".slider").length;
        var cantidad = cantidad - 1;

        //Obtenemos el ancho de la linea desplazadora del slider y la transformamos a negativo
        var linea = ancho * cantidad;
        var linea = parseInt('-' + linea);

        //Sacamos cuanto margin-left tiene la linea
        var linea_margin = parseInt(jQuery(".repre_cont").css("margin-left"));

        //Guardamos en una variable el resultado de cada operacion
        var resultado = linea_margin + ancho;

        var resultado2 = 0;
         if(linea_margin == resultado2){

        }
        else{
            $('.repre_cont').css({"margin-left":resultado});
        }
    });
});

function sinopsis(id, accion, frame){
  if(accion == 'cerrar'){
    $('#pelicula_repre'+id).css({"display":'none'});
  }
  else{
    $('#pelicula_repre'+id).css({"display":'-webkit-box'});
    $('#pelicula_repre'+id).css({"display":'-webkit-flex'});
    $('#pelicula_repre'+id).css({"display":'-ms-flexbox'});
    $('#pelicula_repre'+id).css({"display":'flex'});
    document.getElementById("iframe_yt"+id).innerHTML = "<iframe src='"+ frame +"' frameborder='0' allowfullscreen></iframe>";
  }
}
