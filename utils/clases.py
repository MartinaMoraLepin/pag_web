#clases para usar la bd

#Region para usar en el desplegable
class Region:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
#Comuna para usar en el otro despeglable y que dependa de la region
class Comuna:
    def __init__(self,region_id, id, nombre ):

        self.region_id = region_id
        self.id = id
        self.nombre = nombre
#clase para agregar donaciones        
class Donacion:
    def __init__(self, id, comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular, fotos=None):
        self.id = id
        self.comuna_id = comuna_id
        self.calle_numero = calle_numero
        self.tipo = tipo
        self.cantidad = cantidad
        self.fecha_disponibilidad = fecha_disponibilidad
        self.descripcion = descripcion
        self.condiciones_retirar = condiciones_retirar
        self.nombre = nombre
        self.email = email
        self.celular = celular
        self.fotos = fotos 
#clase para mostrar lista de pedidos
class Pedido:
    def __init__(self, id, comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante):
        self.id = id    
        self.comuna_id = comuna_id
        self.tipo = tipo
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.nombre_solicitante = nombre_solicitante
        self.email_solicitante = email_solicitante
        self.celular_solicitante = celular_solicitante    
            
#clase para mostrar los pedidos a profundidad            
class Pedido2:
    def __init__(self, id, nombre_region, nombre_comuna, tipo, cantidad, descripcion, nombre_solicitante, email_solicitante, celular_solicitante):
        self.id = id
        self.nombre_region = nombre_region
        self.nombre_comuna = nombre_comuna
        self.tipo = tipo
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.nombre_solicitante = nombre_solicitante
        self.email_solicitante = email_solicitante
        self.celular_solicitante = celular_solicitante  
        
#clase para mostrar la donacion a profundidad               
class Donacion2:
    def __init__(self, nombre_region, nombre_comuna, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre_solicitante, email, celular, nombre_archivo, fotos=None):
        self.nombre_region = nombre_region
        self.nombre_comuna = nombre_comuna
        self.calle_numero = calle_numero
        self.tipo = tipo
        self.cantidad = cantidad
        self.fecha_disponibilidad = fecha_disponibilidad
        self.descripcion = descripcion
        self.condiciones_retirar = condiciones_retirar
        self.nombre = nombre_solicitante
        self.email = email
        self.celular = celular
        self.nombre_archivo = nombre_archivo
        self.fotos = fotos or []
    
    
#clase para mostrar las fotos en info donaciones    
class Foto:
    def __init__(self,nombre_archivo,ruta_archivo):

        self.nombre_archivo = nombre_archivo
        self.ruta_archivo = ruta_archivo
            
            
#clase pedido 3
class Pedido3:
    def __init__(self, id, nombre_comuna, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, latitud, longitud):
        self.id = id
        self.nombre_comuna = nombre_comuna
        self.tipo = tipo
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.nombre_solicitante = nombre_solicitante
        self.email_solicitante = email_solicitante
        self.latitud = latitud
        self.longitud = longitud
#clase donaciones 3
class Donacion3:
    def __init__(self, id, calle_numero, tipo, cantidad,fecha, email, latitud, longitud):
        self.id = id
        self.calle_numero = calle_numero
        self.tipo = tipo
        self.cantidad = cantidad
        self.fecha = fecha
        self.email = email
        self.latitud = latitud
        self.longitud = longitud
        
        
#clase pedido 4
class Pedido4:
    def __init__(self, id,tipo):
        self.id = id
        self.tipo = tipo
#clase donacion 4
class Donacion4:
    def __init__(self, id,tipo):
        self.id = id
        self.tipo = tipo
