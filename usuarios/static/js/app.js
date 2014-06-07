$(document).ready(function(){ //cuando el html fue cargado iniciar

    //añado la posibilidad de editar al presionar sobre edit
    $('.editar').on('click',function(){
        //this = es el elemento sobre el que se hizo click en este caso el link
        //obtengo el id que guardamos en data-id
        var id=$(this).attr('data-id');
        //preparo los parametros
        params={};
        params.id=id;
        params.action="editClient";

        if($("#result").height()== 60){
            $( "#result" ).load( "/usuarios/edituser/"+ id +"/");
        }
        else{   
            $("#result").animate({ height: "60px"}, 400 );
            $( "#result" ).load( "/usuarios/edituser/"+ id +"/");
         }
        
    })
    
});