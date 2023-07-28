#validaciones  para los formularios
import re
import filetype
import datetime
#Agregio las validaciones de una forma muy parecida a las que hice en js
def validateRegion(region):
    if region == 0:
        return False
    return True

def validateComuna(comuna):
    if comuna == -1:
        return False
    return True

def validateCalleNum(callenumero):
    if not callenumero:
        return False
    return True

def validateTipo(tipo):
    if tipo == 0:
        return False
    return True

def validateCant(cantidad):
    if not cantidad:
        return False
    return True

def validateDate(fecha):
    if not fecha:
        return False
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', fecha):
        return False

    anho, mes, dia = map(int, fecha.split('-'))
    fechaActual = datetime.date.today()
    fechaEscrita = datetime.date(anho, mes, dia)

    if fechaEscrita < fechaActual:
        return False
    if fechaEscrita.year != anho or fechaEscrita.month != mes or fechaEscrita.day != dia:
        return False

    return True

def validateFotoObligatoria(foto1):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    if foto1 is None:
        return False

    if foto1.filename == "":
        return False

    ftype_guess = filetype.guess(foto1)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False

    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True



def validateFotoNoObligatoria(foto2):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    if foto2 is None:
        return True
    else: 
        ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
        ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}       

        if foto2.filename == "":
            return False
    

        ftype_guess = filetype.guess(foto2)
        if ftype_guess.extension not in ALLOWED_EXTENSIONS:
            return False

        if ftype_guess.mime not in ALLOWED_MIMETYPES:
            return False
        return True



def validateNombre(nombre):
    if not nombre:
        return False
    largoNombre = 3 <= len(nombre) <= 80
    return largoNombre

def validateEmail(email):
    if not email:
        return False
    expresion = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    formatoValido = re.match(expresion, email)
    return formatoValido

def validateCelular(celular):
    if not celular:
        return True
    expresion = re.compile(r'^\+569\d{8}$')
    formatoValido = re.match(expresion, celular)
    return formatoValido


def validateDes(descripcion):
    if not descripcion:
        return False  
    largo = len(descripcion) <= 250  
    return largo


