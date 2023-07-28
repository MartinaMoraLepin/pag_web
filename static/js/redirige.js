//envia el id a informacion-pedido

function redirigirConId(id) {
    localStorage.setItem("idElemento", id); //guarda el id
    window.location.href = "/informacion-pedido/" + id;
}