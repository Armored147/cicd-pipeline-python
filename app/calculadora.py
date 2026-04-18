# app/calculadora.py
"""aplicacion calculadora"""

AUTORES = "???"  # IMPORTANTE: 
#Reemplaza con los usuarios de 
#correo de EAFIT de los estudiantes 
#que participaron en la entrega, 
#separados por comas.


def sumar(a, b):
    """suma los numeros"""
    return a + b


def restar(a, b):
    """resta los numeros"""
    return a - b


def multiplicar(a, b):
    """multiplica"""
    return a * b


def dividir(a, b):
    """divide"""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
