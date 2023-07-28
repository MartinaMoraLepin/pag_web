from flask import Flask, render_template, request,  url_for, redirect, jsonify
from database.db import get_fotos_info,get_region,get_info_donacion,get_pedidos,get_info_pedido,get_donaciones,get_a_pedidos,get_a_donaciones ,get_conn, get_comunas, get_ult_pedidos, get_ult_donaciones
from utils.validations import validateCalleNum,validateCant,validateCelular,validateComuna,validateDate,validateEmail,validateFotoNoObligatoria,validateFotoObligatoria,validateNombre,validateRegion,validateTipo,validateDes
import pymysql
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os
from flask_cors import CORS, cross_origin

#carpeta a la que iran las fotos
UPLOAD_FOLDER = 'static/uploads'
 
app = Flask(__name__)
CORS(app)
#maximo de tamanho para los archivos
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
#lo usare en la app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
##ruta al inicio de la pagina

##ahora aqui debo obtener la informacion de pedidos y donaciones para que se muestren

@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/get-all-donaciones')
@cross_origin(origin="localhost", supports_credentials=True)
def get_all_donaciones():

    c = get_conn()
    donaciones = get_a_donaciones(c)
    markers = []
    for donacion in donaciones:
        don_id = donacion.id
        don_tipo = donacion.tipo

        markers.append({
            "don_id": don_id,
            "don_tipo": don_tipo,
        })
    return jsonify(markers)
@app.route('/get-all-pedidos')
@cross_origin(origin="localhost", supports_credentials=True)
def get_all_pedidos():

    c = get_conn()
    pedidos = get_a_pedidos(c)
    markers = []
    for pedido in pedidos:
        ped_id = pedido.id
        ped_tipo = pedido.tipo

        markers.append({
            "ped_id": ped_id,
            "ped_tipo": ped_tipo,
        })
    return jsonify(markers)
@app.route('/get-info-pedidos', methods=["GET"])
def get_info_pedidos():
    c = get_conn()
    pedidos = get_ult_pedidos(c)
    markers = []
    for pedido in pedidos:
        ped_id = pedido.id
        ped_nombre_comuna = pedido.nombre_comuna
        ped_tipo = pedido.tipo
        ped_des = pedido.descripcion
        ped_cantidad = pedido.cantidad
        ped_nombre_solicitante = pedido.nombre_solicitante
        ped_email = pedido.email_solicitante
        ped_lng = pedido.longitud
        ped_lat = pedido.latitud
        
        markers.append({
            "ped_id": ped_id,
            "ped_nombre_comuna": ped_nombre_comuna,
            "ped_tipo": ped_tipo,
            "ped_des": ped_des,
            "ped_cantidad": ped_cantidad,
            "ped_nombre_solicitante": ped_nombre_solicitante,
            "ped_email": ped_email,
            "ped_lng": ped_lng,
            "ped_lat": ped_lat,
        })
    print(markers)
    return jsonify(markers)
@app.route('/get-info-donaciones', methods=["GET"])
def get_info_donaciones():
    c = get_conn()
    donaciones = get_ult_donaciones(c)
    markers = []
    for donacion in donaciones:
        don_id = donacion.id
        don_calle_numero = donacion.calle_numero
        don_tipo = donacion.tipo
        don_cantidad = donacion.cantidad
        don_fecha = donacion.fecha
        don_email = donacion.email
        don_lng = donacion.longitud
        don_lat = donacion.latitud
        
        markers.append({
            "don_id": don_id,
            "don_calle_numero": don_calle_numero,
            "don_tipo": don_tipo,
            "don_cantidad": don_cantidad,
            "don_fecha": don_fecha,
            "don_email": don_email,
            "don_lng": don_lng,
            "don_lat": don_lat,
        })
    print(markers)
    return jsonify(markers)

@app.route('/agregar-pedido/<int:region_id>',methods=['POST', 'GET'])
def agregar_pedido(region_id): 
    error = [] #lista para los errores
    regiones = None 
    comunas = None
    region = request.form.get("region")
    comuna = request.form.get("comuna")
    tipo =request.form.get("tipo")
    descripcion = request.form.get("descripcion")
    cantidad = request.form.get("cantidad")
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    celular = request.form.get("celular")

    c = get_conn() 
    if request.method=="POST":
        if not validateRegion(region):
            error.append("Error con la region")
        
        if not validateComuna(comuna):
            error.append("Error en la comuna")
              
        if not validateTipo(tipo):
            error.append("Error de tipo")

        if not validateDes(descripcion):
            error.append("Error en la descripcion")
     
        if not validateCant(cantidad):
            error.append("Error en la cantidad")
       
        if not validateNombre(nombre):
            error.append("Error en el nombre")
         
        if not validateEmail(email):
            error.append("Error en el email")
            
        if not validateCelular(celular):
            error.append("Error en el celular")    
        
        print(error)                 
        if not error:
            
            agrega_pedido(c,comuna,tipo,descripcion,cantidad,nombre,email,celular)
            return redirect(url_for('index'))

    regiones = get_region(c, region_id)
    comunas = get_comunas(c, region_id)          
    return render_template('agregar-pedido.html', regiones=regiones,error=error, comunas=comunas)
#ruta para agregar donacion
@app.route('/agregar-donacion/<int:region_id>',methods=['POST', 'GET'])
def agregar_donacion(region_id):
    error = [] #quiero hacer una lista con los errores al agregar la donacion para que los muestre
    comunas = None
    regiones = None 
    c = get_conn()
    if request.method=="POST":
        name = request.form.get("nombre")
        region = request.form.get("region")
        comuna = request.form.get("comuna")
        calle = request.form.get("calle-numero")
        tipo = request.form.get("tipo")
        condiciones = request.form.get("condiciones")
        descripcion = request.form.get("descripcion")
        cantidad = request.form.get("cantidad")
        fecha = request.form.get("fecha-disponibilidad")
        email = request.form.get("email")
        celular = request.form.get("celular")
        foto1 = request.files.get("foto-1")
        foto2 = request.files.get("foto-2")
        foto3 = request.files.get("foto-3")
        if not validateNombre(name):
            error.append("Error en el nombre")
        if not validateRegion(region):
            error.append("Error en la region")    
        if not validateComuna(comuna):
            error.append("Error en la comuna")
        if not validateCalleNum(calle):
            error.append("Error en la direccion")
        if not validateTipo(tipo):
            error.append("Error en el tipo de donación")
        if not validateCant(cantidad):
            error.append("Error en la cantidad")
        if not validateDate(fecha):
            error.append("Error en la fecha")
        if not validateEmail(email):
            error.append("Error en el email")
        if not validateCelular(celular):
            error.append("Error celular")   
        if not validateFotoObligatoria(foto1):
            error.append("Error foto 1")
        if foto2:
          if not validateFotoNoObligatoria(foto2):
              error.append("Error foto-2")
        if foto3:      
            if not validateFotoNoObligatoria(foto3):
                error.append("Error foto 3")    
        print(error)      
        if not error:
            donacion_id  = agrega_donaciones(c,comuna,calle,tipo,cantidad,fecha,descripcion,condiciones,name,email,celular)
            if foto2:
                if foto3:
                    nombref3=add_img(foto3)
                    foto3.save(os.path.join(app.config['UPLOAD_FOLDER'],nombref3))
                    ruta3= os.path.join(app.config['UPLOAD_FOLDER'],nombref3)
                    ruta3 = ruta3.replace('\\', '/')
                    agrega_foto(c,ruta3,nombref3, donacion_id)
                    
                nombref2=add_img(foto2)
                foto2.save(os.path.join(app.config['UPLOAD_FOLDER'],nombref2))
                ruta2= os.path.join(app.config['UPLOAD_FOLDER'], nombref2)
                ruta2 = ruta2.replace('\\', '/')
                agrega_foto(c,ruta2, nombref2, donacion_id)                    
                    
            nombref1=add_img(foto1)
            foto1.save(os.path.join(app.config['UPLOAD_FOLDER'],nombref1))
            ruta1 = os.path.join(app.config['UPLOAD_FOLDER'], nombref1)
            ruta1 = ruta1.replace('\\', '/')
            agrega_foto(c,ruta1, nombref1, donacion_id)                    
              
            return redirect(url_for('index'))

    regiones = get_region(c, region_id)
    comunas = get_comunas(c, region_id)
    return render_template('agregar-donacion.html', regiones=regiones, comunas=comunas, error=error)
#ruta para informacion de donaciones
@app.route('/informacion-donacion')
@app.route("/informacion-donacion/<donacion_id>")
def informacion_donacion(donacion_id):
    print(donacion_id)    
    
    c = get_conn()
    donaciones = get_info_donacion(c, donacion_id)
    fotos = get_fotos_info(c,donacion_id)
    print(donaciones[0].nombre_archivo)
    return render_template('informacion-donacion.html', donaciones=donaciones,fotos=fotos)
#ruta para informacion pedido
@app.route('/informacion-pedido')
@app.route("/informacion-pedido/<pedido_id>")
def informacion_pedido(pedido_id): 

    c = get_conn()
    pedidos = get_info_pedido(c, pedido_id)
    print(pedidos[0].nombre_region)
    return render_template('informacion-pedido.html', pedidos=pedidos)

#ruta para ver donaciones
@app.route('/ver-donaciones')
@app.route('/ver-donaciones/<int:inicio>')
def ver_donaciones(inicio=0):
    c = get_conn()
    donaciones = get_donaciones(c, inicio)
    print(donaciones[1].fotos)
    
    return render_template('ver-donaciones.html', donaciones= donaciones , inicio=inicio)
#ruta para ver pedidos
@app.route('/ver-pedidos')
@app.route('/ver-pedidos/<int:inicio>')
def ver_pedidos(inicio=0):
    c = get_conn()
    pedidos = get_pedidos(c, inicio)
    return render_template('ver-pedidos.html', pedidos = pedidos , inicio = inicio)


#Funcion que se encarga de agregar donaciones a la bd
def agrega_donaciones(c,comuna,calle,tipo, cantidad, fecha, descripcion,condicion,nombre,email,celular ):
     sql = "INSERT INTO donacion (comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)";
     cursor = c.cursor()
     try:
         resultado = cursor.execute(sql,(comuna, calle, tipo, cantidad, fecha, descripcion, condicion, nombre, email, celular))

         c.commit()
         donacion_id = cursor.lastrowid
         if resultado ==1:         
             return donacion_id
         else:
             return False 
     except pymysql.Error as e:
         app.logger.error("Error con base de datos: {}".format(str(e)))
     return False
 
 #funcion que agrega pedidos a la bd
def agrega_pedido(c,comuna,tipo, descripcion ,cantidad, nombre, email,celular):
     sql= "INSERT INTO pedido (comuna_id, tipo,descripcion,cantidad, nombre_solicitante, email_solicitante, celular_solicitante) VALUES (%s, %s, %s, %s, %s, %s, %s)";
     cursor = c.cursor()
     try:
         resultado = cursor.execute(sql,(comuna, tipo, descripcion, cantidad, nombre, email, celular))
         c.commit()
         return resultado == 1;
     except pymysql.Error as e:
         app.logger.error("Error con base de datos: {}".format(str(e)))
     return False    
    
##    funcion que cambia los nombres para agregar una foto
def add_img(im):
    _filename = hashlib.sha256(
    secure_filename(im.filename).encode("utf-8")
    ).hexdigest()
    _extension = filetype.guess(im).extension
    img_filename = f"{_filename}.{_extension}"
    return img_filename

#funcion que agrega una foto a la bd 
def agrega_foto(c,ruta,nombre,donacion_id):
    sql= "INSERT INTO foto (ruta_archivo, nombre_archivo, donacion_id) VALUES (%s, %s, %s)";
    cursor = c.cursor()
    try:
        resultado = cursor.execute(sql,(ruta,nombre,donacion_id))
        c.commit()
        return resultado == 1
    except pymysql.Error as e:
        app.logger.error("Error con base de datos: {}".format(str(e)))
    return False
    


if __name__ == '__main__':
    app.run(debug=True)
