var map = L.map('map').setView([-35.675147, -71.542969], 5);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var markerClusterGroup = L.markerClusterGroup().addTo(map); //Creo grupo de marcadores en el mapa
let marker1 = L.icon({
    iconUrl: '/static/media/locationmorado.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41]
});
fetch("http://127.0.0.1:5000/get-info-pedidos")
    .then((response) => response.json())
    .then((parsedData) => {
        console.log(parsedData); //veo que entregue bien el json
        for (let pedido of parsedData) {
            let lat = pedido["ped_lat"];
            let lng = pedido["ped_lng"];

            const onMarkerClick = (e) => {
                L.popup()
                    .setLatLng([lat, lng])
                    .setContent(`<h1>Id pedido:${pedido["ped_id"]}</h1><br>Tipo:${pedido["ped_tipo"]}<br>Cantidad:${pedido["ped_cantidad"]}<br>email solicitante:${pedido["ped_email"]}`)
                    .openOn(map);
            };

            let marker = L.marker([lat, lng], { icon: marker1 });
            marker.on("click", onMarkerClick);
            markerClusterGroup.addLayer(marker); //Agrego el marker al grupo de marcadores

        }
    });
let marker2 = L.icon({
    iconUrl: '/static/media/locationrosa.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41]
});
fetch("http://127.0.0.1:5000/get-info-donaciones")
    .then((response) => response.json())
    .then((parsedData) => {
        console.log(parsedData); //veo que entregue bien el json
        for (let donacion of parsedData) {
            let lat = donacion["don_lat"];
            let lng = donacion["don_lng"];

            const onMarkerClick = (e) => {
                L.popup()
                    .setLatLng([lat, lng])
                    .setContent(`<h1>Id donacion:${donacion["don_id"]}</h1><br>Calle: ${donacion["don_calle_numero"]}<br>Tipo:${donacion["don_tipo"]}<br>Cantidad:${donacion["don_cantidad"]}<br>Fecha disponibilidad: ${donacion["don_fecha"]}<br>email donante:${donacion["don_email"]}`)
                    .openOn(map);
            };

            let marker = L.marker([lat, lng], { icon: marker2 });
            marker.on("click", onMarkerClick);
            markerClusterGroup.addLayer(marker); //Agrego el marker al grupo de marcadores

        }
    });