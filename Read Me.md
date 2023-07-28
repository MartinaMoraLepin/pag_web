## READ ME

Martina Mora

Rut:20.832.775-5

-Al desarrollar esta tarea había intentado usar un template, por lo que hay ciertas clases con el nombre del template.

-Usé el codigo que subio el profe solo en la foto de cerezas de informacion-donaciones para que se agrande porque no me dio el tiempo
(intenté hacerlo para otras fotos  pero no funcionó ,por ejemplo en el caso de los champiñones, por eso esta como ese codigo en el css estilodonaciones y en en el html de informacion-donacion)
-El codigo cuenta con 5 archivos .css (para darle estilo al agrandar la foto también usé lo del ejemplo del profe)
-7 html
-6 javascript
- Hay 2 redirige porque debo redirigir a archivos distintos

**Desarrollo tarea 2** 

-Lo primero a notar en el desarrollo de esta tarea es que el  username de mi base de datos es cc5502, no cc5002, esto es porque me equivoqué y me di cuenta muy tarde :c 

-Los menús de comuna y región ahora usan la base de datos y no el .json

-En las tablas de ver donaciones hay donaciones que se ven sin fotos, esto es por bugs que se produjeron cuando estaba desarrollando la tarea, ya que cambié de posición la carpeta Uploads, y mientras probaba se bugueó un poco el desarrollo. 

-En el caso de ver donaciones, no pude hacer que se vean las fotos, pero informacion si
-Hay un bug cuando coloco correos sugeridos en el formulario de agregar donaciones, y no logré encontrar el porque se producía este bug.

-Agregué botones de volver a inicio, pues desde el inicio se  puede ir de buena forma a todas las página

**Desarrollo tarea 3**

-Para desarrollar esta tarea lo primero que hice fue pasar el archivo json que venía con el enunciado a un comando sql (por eso se creo el archivo communaChile.sql)para crear una tabla que tenga las comunas con latitud y longitud, con esto después le puse estas columnas a la tabla comuna original. Tuve que hacer esto pues no pude cargar el json de otra forma. Además habían nombres o caracteres que hicieron problemas, de forma que estos los llené a mano desde WorkBench. 

-Para el mapa se usó Leaflet y  markerCluster para prevenir las colisiones entre marcadores. (los marcadores en foto fueron íconos que cree para que se diferencien por color entre donaciones y pedidos)

-Para la creación de los gráficos  se utilizó Highcharts.


-Para pasarle la información desde la base de datos a los mapas y los gráficos se hizo un proceso ánalogo al de la tarea 2, usar clases, funciones que con querys de SQL extraigan la información y usar funciones que pongan esto en  un json para recibirlas desde javascript y ahí poder utilizar esta información.



