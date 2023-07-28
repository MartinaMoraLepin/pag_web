//Ahora voy a hacer las funciones que serviran para validar los formularios
//DE aca obtengo region y comuna
const regionesSelect = document.getElementById("region");
const comunasSelect = document.getElementById("comuna");
//aca cargo el json considerando solo la comuna ya que las regiones las puse con el mismo id del json oara asociarlo a sus comunas respectivas
fetch("./region_comuna.json")
    .then((response) => response.json())
    .then((data) => {
        regionesSelect.addEventListener("change", (event) => {
            const rId = event.target.value; //obtengo el id de la region
            const region = data.regiones.find(region => region.id == Number(rId));
            comunasSelect.innerHTML = ""; //use innerHTML porque el text no me funciono
            comunasSelect.disabled = rId === "";
            if (region) { //reviso las comunas de cada region si es que ya se escoge una
                for (const comuna of region.comunas) {
                    const option = document.createElement("option");
                    option.value = comuna.id;
                    option.textContent = comuna.nombre;
                    comunasSelect.appendChild(option);

                }
            } else { //si no esta en la parte que dice que debes seleccionar de una region
                const option = document.createElement("option");
                option.value = "";
                option.textContent = "Debes seleccionar una región";
                comunasSelect.appendChild(option);
            }
        })

    });
//hago la funcion para validar el formulario
const validateForm = () => {
        //lo primero es hacer que comuna y region sean obligatorios
        const validateRegion = (region) => {

            if (region == 0) return false; //si no pone region no podemos enviar el formulario
            return true;
        };

        //Analogo para las comunas

        const validateComuna = (comuna) => {
            if (comuna == -1) return false; //si no pone comuna no se puede enviar

            return true;

        };

        //ahora valido el tipo de donacion
        const validateTipo = (tipo) => {
            if (tipo == 0) return false; //si no hay tipo no se puede enviar el formulario

            return true;

        };
        //valido la descripcion
        const validateDes = (descripcion) => {
            if (!descripcion) return false; //si no esta es falso porque aqui es obligatorio
            let largo = descripcion.length <= 250;
            //si cumple el largo retorna true si no, false
            return largo;

        };
        //ahora valido la cantidad de donacion
        const validateCant = (cantidad) => {
            if (!cantidad) return false; //tambien es obligatoria


            return true;
        };
        //valido el nombre
        const validateNombre = (nombre) => {
            if (!nombre) return false; //es obligatorio el nombre
            let largoNombre = 3 <= nombre.length <= 80; // debe cumplir un maximo y un minimo el nombre
            return largoNombre;
        };


        //Valido el email
        const validateEmail = (email) => {
            if (!email) return false; //es obligatorio
            //hago la expresion regular que simula email
            let expresion = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            let formatoValido = expresion.test(email); // revisa que cumpla con la expresion regular
            return formatoValido; //si es formato de email es true
        };


        //Valido el celular 
        const validateCelular = (celular) => {
            //es opcional
            //debe cumplir el formato de telefono
            //poner que lo pongan desde el 9 o despues y con el +56
            if (!celular) return true;
            else {
                let expresion = /^\+569\d{8}$/; //expresiones regulares que pueden ser numeros
                let formatoValido = expresion.test(celular);
                return formatoValido;
            }

        };
        //traigo los inputs a ingresar para pasarlos por sus respectivos validadores
        let form = document.forms["formulario-agrega-pedido"];
        let region = form["region"].value;
        let comuna = form["comuna"].value;
        let tipo = form["tipo"].value;
        let descripcion = form["descripcion"].value;
        let cantidad = form["cantidad"].value;
        let nombre = form["nombre"].value;
        let email = form["email"].value;
        let celular = form["celular"].value;
        let invalidInputs = [];
        let isValid = true;
        const setInvalidInput = (inputName) => {
            invalidInputs.push(inputName);
            isValid = false;
        };

        // veo si hay algo invalido
        if (!validateRegion(region)) {
            setInvalidInput("Region");
        }
        if (!validateComuna(comuna)) {
            setInvalidInput("Comuna");
        }

        if (!validateTipo(tipo)) {
            setInvalidInput("Tipo");
        }
        if (!validateDes(descripcion)) {
            setInvalidInput("Descripción");
        }
        if (!validateCant(cantidad)) {
            setInvalidInput("Cantidad");
        }
        if (!validateNombre(nombre)) {
            setInvalidInput("Nombre");
        }
        if (!validateEmail(email)) {
            setInvalidInput("Email");
        }
        if (!validateCelular(celular)) {
            setInvalidInput("Celular");
        }
        //tengo esto para que muestre lo invalido
        let validationBox = document.getElementById("val-box");
        let validationMessageElem = document.getElementById("val-msg");
        let validationListElem = document.getElementById("val-list");
        //si es invalido meto los campos invalidos a la lista
        if (!isValid) {
            validationListElem.textContent = "";
            // add invalid elements to val-list element.
            for (input of invalidInputs) {
                let listElement = document.createElement("li");
                listElement.innerText = input;
                validationListElem.append(listElement);
            }

            validationMessageElem.innerText = "Los siguiente campos son invalidos:";


            validationBox.hidden = false;
        } else { //si no muestro mensaje de confimarcion
            //form.submit(); no tengo que enviar el formulario aun 
            mensajeD(mensaje);

        }
    }
    //Creo boton para agregar el pedido
let submitBtn = document.getElementById("submit-btn1");
submitBtn.addEventListener("click", validateForm);
//funciones para confirmar o rechazar el envio del formulario
const mensajeD = (mensaje) => {
    mensaje.style.display = 'block';

};
const mensajeND = (mensaje) => {
    mensaje.style.display = 'none'
};
const confirmar = () => {

    mensajeND(mensaje);
    mensajeD(mensajeConfirmacion); //mensaje final a confirmar

};
const rechazar = () => {
    mensajeND(mensaje);
};
//Extraigo la informacion marcada
let mensaje = document.getElementById("mensaje");
let confirma = document.getElementById("confirma");
let rechaza = document.getElementById("cancela");
rechaza.addEventListener("click", rechazar);
confirma.addEventListener("click", confirmar);
let mensajeConfirmacion = document.getElementById("mensaje-final");

function seleccionarRegion() {
    var regionSelect = document.getElementById("region");
    var regionId = regionSelect.options[regionSelect.selectedIndex].value;
    window.location.href = "/agregar-pedido/" + regionId;

}