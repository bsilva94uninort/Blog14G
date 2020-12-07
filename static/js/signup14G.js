function validarFormulario(){
    let usuario = document.formulario.nombreUsuario;
    let contrasena = document.formulario.pass;
    do{
        if(usuario.value.length==0 || usuario.value.length<5){
            alert("El usuario debe tener mínimo 5 caracteres");
            return false}
        if(contrasena.value.length==0 || contrasena.value.length<10){
            alert("La contraseña debe tener mínimo 10 caracteres");
            return false}
    }while(false)
    alert("Se ha enviado correo de autenticación a "+document.formulario.email.value)
    window.open("login14G.html");
    window.close();
    return
}

