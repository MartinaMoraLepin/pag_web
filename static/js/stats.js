Highcharts.chart("container", {
    chart: {
        type: 'bar'
    },
    title: {
        text: 'Cantidad de pedidos en función del tipo'
    },
    xAxis: {
        categories: ['Fruta', 'Verdura', 'Otro']
    },
    yAxis: {
        title: {
            text: 'Cantidad de pedidos'
        }
    },
    series: [{
        name: 'Cantidad',
        data: [],
        color: "#FC2865",
    }]
});

fetch("http://127.0.0.1:5000/get-all-pedidos")
    .then((response) => response.json())
    .then((data) => {
        console.log(data);

        let parsedData = [
            { name: 'Fruta', y: 0 },
            { name: 'Verdura', y: 0 },
            { name: 'Otro', y: 0 }
        ];

        data.forEach((item) => {
            const tipo = item.ped_tipo;

            switch (tipo) {
                case 'fruta':
                    parsedData[0].y += 1;
                    break;
                case 'verdura':
                    parsedData[1].y += 1;
                    break;
                default:
                    parsedData[2].y += 1;
            }
        });

        console.log(parsedData);

        const chart = Highcharts.charts.find(
            (chart) => chart && chart.renderTo.id === "container"
        );

        chart.update({
            series: [{
                data: parsedData,
                color: "#FF00FF"
            }],
        });
    })
    .catch((error) => console.error("Error:", error));

Highcharts.chart("container1", {
    chart: {
        type: 'bar'
    },
    title: {
        text: 'Cantidad de donaciones en función del tipo'
    },
    xAxis: {
        categories: ['Fruta', 'Verdura', 'Otro']
    },
    yAxis: {
        title: {
            text: 'Cantidad de donaciones'
        }
    },
    series: [{
        name: 'Cantidad',
        data: [],
        color: "#FC2865",
    }]
});

fetch("http://127.0.0.1:5000/get-all-donaciones")
    .then((response) => response.json())
    .then((data) => {
        console.log(data);

        let parsedData = [
            { name: 'Fruta', y: 0 },
            { name: 'Verdura', y: 0 },
            { name: 'Otro', y: 0 }
        ];

        data.forEach((item) => {
            const tipo = item.don_tipo;

            switch (tipo) {
                case 'fruta':
                    parsedData[0].y += 1;
                    break;
                case 'verdura':
                    parsedData[1].y += 1;
                    break;
                default:
                    parsedData[2].y += 1;
            }
        });

        console.log(parsedData);

        const chart = Highcharts.charts.find(
            (chart) => chart && chart.renderTo.id === "container1"
        );

        chart.update({
            series: [{
                data: parsedData,
                color: "#FFC0CB"
            }],
        });

    })
    .catch((error) => console.error("Error:", error));