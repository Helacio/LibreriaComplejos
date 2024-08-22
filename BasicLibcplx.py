import math

def sum_cplx(a, b):
    real = a[0] + b[0]
    imag = a[1] + b[1]
    return (real, imag)

def mult_cplx(a,b):
    real = a[0]*b[0] - a[1]*b[1]
    imag = a[0]*b[1] + a[1]*b[0]
    return (real, imag)

def diferencia_cplx(a, b):
    real = a[0] - b[0]
    imag = a[1] - b[1]
    return (real, imag)

def division_cplx(a, b):  #a/b
    denom = b[0] ** 2 + b[1] ** 2
    real = (a[0]*b[0] + a[1]*b[1]) / denom
    imag = (a[1]*b[0] - a[0]*b[1]) / denom
    return (real, imag)

def modulo(a):
    return (a[0] ** 2 + a[1] ** 2) ** (0.5)

def conjugado(a):
    return (a[0], -a[1])

#Pasar de coordenadas cartesianas a polares
def cartopolar(a):
    lnght = (a[0] ** 2 + a[1] ** 2) ** (0.5)
    angle = math.atan2(a[1], a[0])
    return (lnght, angle)

#Pasar de coordenadas polares a cartesianas
def polartocart(a):
    x = a[0] * math.cos(a[1])
    y = a[0] * math.sin(a[1])
    return (x, y)

def fase(a):
    return math.atan2(a[1], a[0])
