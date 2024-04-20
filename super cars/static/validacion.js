const correo = document.getElementById("id_correo");

function allowOnlyLetters(event){
    const key = event.key 
    const regex = /^[a-zA-Z\s]*$/;
    if (!regex.test(key)){
        event.preventDefault();
    }
}
function validarCorreo(element) {
    element.addEventListener('blur', ()=>{
    const regex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/;
    if (!regex.test(element.value)){
        element.style.borderColor = 'salmon';
    } else{
        element.style.borderColor = 'green';
        
    }
    })
  }

validarCorreo(correo)

//   document.getElementById("id_correo").addEventListener('keydown', validarCorreo); 
document.getElementById("id_nombre").addEventListener('keydown', allowOnlyLetters); 
document.getElementById("id_apellido").addEventListener('keydown', allowOnlyLetters);  

//con esta validacion al momento de enviar el formulario muestra un alert que indica que se envio y refresca el formulario
const formulario = document.getElementsByClassName('formulario')[0];

formulario.addEventListener('submit', function(event) {
    

    const elementosFormulario = document.getElementsByClassName('formulario');
    for (let i = 0; i < elementosFormulario.length; i++) //oculta los elementos del formulario iterando sobre ellos 

    alert('¡Formulario enviado exitosamente');
}) 