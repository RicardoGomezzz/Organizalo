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
  $("#formregister").validate({ 
    rules:{ 
        email: {
            required: true,
            email: true
          },
        nombre: {
            required: true,
            minlength: 10,
            maxlength: 80
    },
        password: {
            required: true,
            minlength: 8
      },
    },
    messages: {
        email: "Favor ingresar correo",
        nombre: "Favor ingresar nombre"
    }
  });




