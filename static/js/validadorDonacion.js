//Ahora voy a hacer las funciones que serviran para validar los formularios
const regionesSelect = document.getElementById("region");
const comunasSelect = document.getElementById("comuna");
//sigue la misma logica de validadorPedido
fetch("./region_comuna.json")
    .then((response) => response.json())
    .then((data) => {
        regionesSelect.addEventListener("change", (event) => {
            const rId = event.target.value;
            const region = data.regiones.find(region => region.id == Number(rId));
            comunasSelect.innerHTML = "";
            comunasSelect.disabled = rId === "";
            if (region) {
                for (const comuna of region.comunas) {
                    const option = document.createElement("option");
                    option.value = comuna.id;
                    option.textContent = comuna.nombre;
                    comunasSelect.appendChild(option);

                }
            } else {
                const option = document.createElement("option");
                option.value = "";
                option.textContent = "Debes seleccionar una región";
                comunasSelect.appendChild(option);
            }
        })

    });
//Hago el validador del formulario con la misma logica del validador pedido

const validateForm = () => {
        //lo primero es hacer que comuna y region sean obligatorios
        const validateRegion = (region) => {

            if (region == 0) return false; //si no pone region no podemos enviar el formulario
            return true;
        };

        //Analogo para las comunas que debe ser obligatoriop

        const validateComuna = (comuna) => {
            if (comuna == -1) return false;

            return true;

        };
        //Ahora valido la calle y numero que tambien es obligatoria
        const validateCalleNum = (callenumero) => {

            if (!callenumero) { //es obligatorio asi que primero veo que al menos tenga algo
                return false;
            }
            return true;

        };

        //ahora valido el tipo de donacion que tambien es obligatorio
        const validateTipo = (tipo) => {
            if (tipo == 0) return false; //si no hay se requiere
            return true;

        };

        //ahora valido la cantidad de donacion
        const validateCant = (cantidad) => {
            if (!cantidad) return false; //tambien es obligatorio


            return true;
        };


        //ahora debo hacer la validacion de la fecha de disponibilidad
        const validateDate = (fecha) => {
            // si no hay nada no puede pues es campo obligatorio
            if (!fecha) return false;
            // ahora reviso que cumpla el formato YYYY-MM-DD
            // si no lo cumple retorna falso
            // la función test de javascript revisa que en este caso "fecha" coincida con la expresión regular que en este caso define el formato YYYY-MM-DD
            if (!/^\d{4}-\d{2}-\d{2}$/.test(fecha)) return false;

            // ahora separo en partes para verificar que sea una fecha valida
            const [anho, mes, dia] = fecha.split('-');

            // Creo un objeto Date para obtener la fecha actual y compararla con la ingresada
            const fechaActual = new Date();
            // Creo un objeto Date para la fecha ingresada
            //el mes lo cuenta desde 0 a 11 por eso va el -1 propio de javascript
            const fechaEscrita = new Date(anho, mes - 1, dia);

            // Reviso si la fecha ingresada es menor a la actual debo entregar false
            if (fechaEscrita.getTime() < fechaActual.getTime()) {
                return false;
            }

            // Verifico que la fecha sea valida(coincida la ingresada con la separada)
            if (fechaEscrita.getFullYear() !== Number(anho) || fechaEscrita.getMonth() !== Number(mes) - 1 || fechaEscrita.getDate() !== Number(dia)) {
                return false;
            }

            //la fecha paso todos los validadores
            return true;
        };
        //test validador de fechas

        //console.log(validateDate('2023-13-01')); // debe imprimir "false"
        //console.log(validateDate('2023-08-14')); // debe imprimir "true"


        //ahora hago el validador para las fotos donde debe haber al menos una y maximo 3 y en inputs separados
        const validateFotoObligatoria = (foto1) => {
            if (!foto1) return false;
            //si no hay se requiere
            // aqui reviso que la foto sea pdf o algun tipo de imagen, si no lo es retorno false
            for (const file of foto1) {
                if (file.type.split("/")[0] !== "image" && file.type !== "application/pdf") {
                    return false;
                }
            }
            let largo = foto1.length == 1;

            // reviso que solo me entregue un archivo
            return largo;
        };


        //hago otro para las fotos no obligatorias
        const validateFotoNoObligatoria = (foto2) => {
            //revisa que cumpla formato pdf o imagen igual que en el validador anteriro

            if (foto2.length > 1) return false
            for (const file of foto2) {
                if (file.type.split("/")[0] !== "image" && file.type !== "application/pdf") {
                    return false;
                }
            }

            // valida que solo haya un archivo pues solo se puede 1 x input
            return true;

        }
        const validateNombre = (nombre) => {
            if (!nombre) return false; //es obligatorio el nombre
            let largoNombre = 3 <= nombre.length <= 80; // debe cumplir un maximo y un minimo el nombre
            return largoNombre;
        };



        const validateEmail = (email) => {
            if (!email) return false; //es obligatorio
            //sigue la misma logica que en el archivo de Pedido
            let expresion = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            let formatoValido = expresion.test(email); // revisa que cumpla con la expresion regular
            return formatoValido; //si es formato de email es true
        };


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
        let form = document.forms["formulario-agrega-donacion"];
        let region = form["region"].value;
        let comuna = form["comuna"].value;
        let calleNumero = form["calle-numero"].value;
        let tipo = form["tipo"].value;
        let cantidad = form["cantidad"].value;
        let fecha = form["fecha-disponibilidad"].value;
        let foto1 = form["foto-1"].files;
        let foto2 = form["foto-2"].files;
        let foto3 = form["foto-3"].files;
        let nombre = form["nombre"].value;
        let email = form["email"].value;
        let celular = form["celular"].value;
        let invalidInputs = [];
        let isValid = true;
        const setInvalidInput = (inputName) => {
            invalidInputs.push(inputName);
            isValid = false;
        };

        // Veo si hay algo invalido
        if (!validateRegion(region)) {
            setInvalidInput("Region");
        }
        if (!validateComuna(comuna)) {
            setInvalidInput("Comuna");
        }
        if (!validateCalleNum(calleNumero)) {
            setInvalidInput("Calle y numero");
        }
        if (!validateTipo(tipo)) {
            setInvalidInput("Tipo");
        }
        if (!validateCant(cantidad)) {
            setInvalidInput("Cantidad");
        }
        if (!validateDate(fecha)) {
            setInvalidInput("Fecha");
        }
        if (!validateFotoObligatoria(foto1)) {
            setInvalidInput("Foto1");
        }
        if (!validateFotoNoObligatoria(foto2)) {
            setInvalidInput("Foto2");
        }
        if (!validateFotoNoObligatoria(foto3)) {
            setInvalidInput("Foto3");
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
        //esto para que despues se muestre un cuadro con los campos invalidos
        let validationBox = document.getElementById("val-box");
        let validationMessageElem = document.getElementById("val-msg");
        let validationListElem = document.getElementById("val-list");

        //si no es valido muestro todos los campos
        if (!isValid) {
            validationListElem.textContent = "";

            for (input of invalidInputs) {
                let listElement = document.createElement("li");
                listElement.innerText = input;
                validationListElem.append(listElement);
            }

            validationMessageElem.innerText = "Los siguiente campos son invalidos:";

            //hago visible el mensaje
            validationBox.hidden = false;
        } else { //muestro el mensaje de confirmacion
            mensajeD(mensaje);

        }
    }
    //boton para agregar donacion
let submitBtn = document.getElementById("submit-btn");
submitBtn.addEventListener("click", validateForm);
//analogo del form de pedido
const mensajeD = (mensaje) => {
    mensaje.style.display = 'block';

};
const mensajeND = (mensaje) => {
    mensaje.style.display = 'none'
};
const confirmar = () => {

    mensajeND(mensaje);
    mensajeD(mensajeConfirmacion);

};
const rechazar = () => {
    mensajeND(mensaje);
};

let mensaje = document.getElementById("mensaje");
let confirma = document.getElementById("confirma");
let rechaza = document.getElementById("cancela");
rechaza.addEventListener("click", rechazar);
confirma.addEventListener("click", confirmar);
let mensajeConfirmacion = document.getElementById("mensaje-final");


//Recupero el id de la region

function seleccionarRegion() {
    var regionSelect = document.getElementById("region");
    var regionId = regionSelect.options[regionSelect.selectedIndex].value;
    window.location.href = "/agregar-donacion/" + regionId;

}