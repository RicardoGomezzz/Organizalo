$("#formlogin").validate({
    rules:{
      email: "required",
      password: "required"
    },
    messages: {
      email: "Favor ingresar el correo",
      password: "Favor ingresar la contraseña"
    } 
  });


