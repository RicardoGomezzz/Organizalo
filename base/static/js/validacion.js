$(document).ready(function(){
    $("#crearCuenta").click(function(){
        var correo = $("#email").val();
        var contraseña = $("#password").val();
        var nombre = $("#name").val(); 
        
        
            
        
        
        if (nombre == "" || correo == "" || contraseña ==  "" ){alert("Formulario incompleto");
        }
        });
    });