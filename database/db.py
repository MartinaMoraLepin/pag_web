import pymysql
from utils.clases import Region, Comuna,Foto ,Donacion, Pedido, Pedido2, Donacion2, Pedido3,Donacion3,Pedido4,Donacion4
import json
from flask import send_from_directory
from werkzeug.utils import secure_filename

#datos para conexion abd
DB_NAME = "tarea2"
DB_USERNAME = "cc5502"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"


#conecto a  la bd
def get_conn():
	conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
	return conn





#obtengo la region seleccionada para enviarla a comunas 

def get_region(c, region_id):
    sql = "SELECT * FROM region WHERE id = %s";
    sql1= " SELECT * FROM region WHERE id != %s"; 
    cursor = c.cursor()
    cur = c.cursor()
    cursor.execute(sql, (region_id))
    cur.execute(sql1, (region_id ))
    c.commit()
    region = cursor.fetchone()    
    regiones = cur.fetchall()
    listaRegiones = []
    listaRegiones.append(Region(region[0], region[1]))
    if len(regiones) > 0:
        for reg in regiones:
            regionBD = Region(reg[0], reg[1])
            listaRegiones.append(regionBD)
    return listaRegiones


#funcion para obtener las comunas en funcion de la region seleciconada
#debe recibir la conexion a la bd y el id de la region seleccionada para que muestre
def get_comunas(c, region_id):
    sql = "SELECT    region_id  ,id, nombre FROM comuna WHERE region_id = %s";
    cursor = c.cursor()
    cursor.execute(sql, (region_id,))
    c.commit()
    comunas = cursor.fetchall()
    listaComunas = []
    if len(comunas) > 0:
        for comuna in comunas:
            comunaBD = Comuna(comuna[0], comuna[1], comuna[2])
            listaComunas.append(comunaBD)
    return listaComunas


#funcion que obtiene las donaciones, la idea es partir desde un inicio y como limite ponga solo 5, eso se hace aprovechando la query
def get_donaciones(c, inicio, termino=5):
    sql = """
    SELECT don.id, com.nombre, don.calle_numero, don.tipo, don.cantidad, don.fecha_disponibilidad, don.descripcion, don.condiciones_retirar, don.nombre, don.email, don.celular
    FROM donacion AS don
    INNER JOIN comuna AS com ON don.comuna_id = com.id
    GROUP BY don.id
    ORDER BY don.id
    LIMIT %s OFFSET %s
    """

    cursor = c.cursor()
    cursor.execute(sql, (termino, inicio))
    donaciones = cursor.fetchall()
    listaDonaciones = []
    if len(donaciones) > 0:
        for donacion in donaciones:

            donacionBD = Donacion(donacion[0], donacion[1], donacion[2], donacion[3], donacion[4], donacion[5], donacion[6], donacion[7], donacion[8], donacion[9], donacion[10])
            listaDonaciones.append(donacionBD)
    return listaDonaciones
#obtengo los pedidos de manera analoga
def get_pedidos(c,inicio, termino =5):
    sql = "SELECT ped.id, com.nombre, ped.tipo, ped.cantidad, ped.descripcion, ped.nombre_solicitante, ped.email_solicitante, ped.celular_solicitante " \
          "FROM pedido AS ped " \
          "INNER JOIN comuna AS com ON ped.comuna_id = com.id " \
          "ORDER BY ped.id LIMIT %s OFFSET %s"
    cursor = c.cursor()
    cursor.execute(sql, (termino, inicio))
    pedidos = cursor.fetchall()
    listaPedidos = []
    if len(pedidos) > 0:
        for pedido in pedidos:
            pedidoBD = Pedido(pedido[0], pedido[1], pedido[2], pedido[3], pedido[4], pedido[5], pedido[6], pedido[7])
            listaPedidos.append(pedidoBD)
    return listaPedidos


#obtengo la informacion de pedido con una query y usando la clase Pedido2
def get_info_pedido(c, id_pedido):
    sql = "SELECT p.id, r.nombre AS nombre_region, co.nombre AS nombre_comuna, p.tipo, p.cantidad, p.descripcion, p.nombre_solicitante, p.email_solicitante, p.celular_solicitante FROM pedido p JOIN comuna co ON p.comuna_id = co.id JOIN region r ON co.region_id = r.id WHERE p.id = %s"

    cursor = c.cursor()
    cursor.execute(sql, (id_pedido,))
    pedido = cursor.fetchone()
    print(pedido)

    pedidoBD = Pedido2(pedido[0], pedido[1], pedido[2], pedido[3], pedido[4], pedido[5], pedido[6], pedido[7], pedido[8])
    print(pedidoBD)
    listaPedidos = [pedidoBD]
    print(listaPedidos)
    return listaPedidos

#obtengo la info  donacion y uso Donacion2
def get_info_donacion(c, id_donacion):
    print(id_donacion)
    sql = "SELECT r.nombre, c.nombre, d.calle_numero, d.tipo, d.cantidad, d.fecha_disponibilidad, d.descripcion, d.condiciones_retirar, d.nombre, d.email, d.celular, f.nombre_archivo FROM donacion d INNER JOIN comuna c ON d.comuna_id = c.id INNER JOIN region r ON c.region_id = r.id LEFT JOIN foto f ON d.id = f.donacion_id WHERE d.id = %s"
    cursor = c.cursor()
    cursor.execute(sql, (id_donacion,))
    donacion = cursor.fetchone()
    print(donacion)

    if donacion:
        donacionBD = Donacion2(donacion[0], donacion[1], donacion[2], donacion[3], donacion[4], donacion[5], donacion[6], donacion[7], donacion[8], donacion[9], donacion[10], donacion[11])
        print(donacionBD)
        listaDonacion = [donacionBD]
        print(listaDonacion)
        return listaDonacion
    
#obtengo las fotos para poner en info donacion    
def get_fotos_info(c,id_donacion):
    sql = "SELECT nombre_archivo FROM foto WHERE donacion_id=%s";
    cursor = c.cursor()
    cursor.execute(sql, (id_donacion,))
    fotos = cursor.fetchall() 
    listaFotos=[]
    if len(fotos) > 0:
        for foto in fotos:
            fotoBD = Foto(foto[0], '')
            listaFotos.append(fotoBD)
    return listaFotos
        
 ##5 ults pedidos       
def get_ult_pedidos(c):
    sql = "SELECT p.id, c.nombre AS nombre_comuna, p.tipo, p.descripcion, p.cantidad, p.nombre_solicitante, p.email_solicitante, c.lat, c.lng FROM pedido p INNER JOIN comuna c ON p.comuna_id = c.id ORDER BY p.id DESC LIMIT 5"
    cursor = c.cursor()
    cursor.execute(sql)
    pedidos = cursor.fetchall()
    listaPedidos = []

    if len(pedidos) > 0:
        for pedido in pedidos:
            print(pedido)
            if len(pedido) == 9:

                pedidoBD = Pedido3(pedido[0], pedido[1], pedido[2], pedido[3], pedido[4], pedido[5], pedido[6], pedido[7], pedido[8])
            else:

                print(f"Error: Tupla de pedido inválida: {pedido}")
                continue
            
            listaPedidos.append(pedidoBD)
    return listaPedidos
 ##5 ults donaciones     
def get_ult_donaciones(c):
    sql = "SELECT d.id, d.calle_numero, d.tipo, d.cantidad, d.fecha_disponibilidad, d.email, c.lat, c.lng FROM donacion AS d INNER JOIN comuna AS c ON d.comuna_id = c.id ORDER BY d.id DESC LIMIT 5;"
    cursor = c.cursor()
    cursor.execute(sql)
    donaciones = cursor.fetchall()
    listaDonaciones = []

    if len(donaciones) > 0:
        for donacion in donaciones:
            print(donacion)
            if len(donacion) == 8:
                donacionBD = Donacion3(donacion[0], donacion[1], donacion[2], donacion[3], donacion[4], donacion[5], donacion[6], donacion[7])
            else:
                print(f"Error: Tupla de donacion inválida: {donacion}")
                continue
            
            listaDonaciones.append(donacionBD)
    return listaDonaciones
def get_a_pedidos(c):
    sql = "SELECT id, tipo FROM pedido;"
    cursor = c.cursor()
    cursor.execute(sql)
    pedidos = cursor.fetchall()
    listaPedidos = []

    if len(pedidos) > 0:
        for pedido in pedidos:
            print(pedido)
            if len(pedido) == 2:
               
                pedidoBD = Pedido4(pedido[0], pedido[1])
            else:

                print(f"Error: Tupla de pedido inválida: {pedido}")
                continue
            
            listaPedidos.append(pedidoBD)
    return listaPedidos


def get_a_donaciones(c):
    sql = "SELECT id, tipo FROM donacion;"
    cursor = c.cursor()
    cursor.execute(sql)
    donaciones = cursor.fetchall()
    listaDonaciones = []

    if len(donaciones) > 0: 
        for donacion in donaciones:  
            print(donacion)
            if len(donacion) == 2:
       
                donacionBD = Donacion4(donacion[0], donacion[1])
            else:
               
                print(f"Error: Tupla de donacion inválida: {donacion}")
                continue
            
            listaDonaciones.append(donacionBD)
    return listaDonaciones
