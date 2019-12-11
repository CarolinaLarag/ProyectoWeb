
function validar() {
	var nombre,apellido,correo,telefono,texto;

	nombre = document.getElementById("nombre").value;
	apellido = document.getElementById("apellido").value;
	correo = document.getElementById("correo").value;
	telefono = document.getElementById("contacto").value;
	texto = document.getElementById("recomendacion").value;

	if(nombre === ""){
		alert("El campo nombre es obligatorio");
		return false;
	}
	else if (apellido === ""){
		alert("El campo apellido es obligatorio");
		return false;
	}
	else if (correo === ""){
		alert("El campo correo es obligatorio");
		return false;
	}
	else if (telefono === ""){
		alert("El telefono es obligatorio");
		return false;
	}
	else if (texto ===""){
		alert ("El texto es obligatorio");
		return false;
	}
	else{

		alert ("El mensaje del cliente : "+ nombre +" "+ apellido + " será atendido pronto,espere nuestra respuesta");
		alert ("Gracias por su preferencia!");
		return location.reload();
	}

}

function limpiarFormulario() {
    document.getElementById("formulario").reset();
  }

