"""import time
inicio = time.time()"""
# Coloque el módulo del ejercicio anterior dentro de un paquete. En un
# módulo que esté fuera de ese paquete, cree una función de suma de
# decimales que redondee el resultado haciendo uso de la función
# redondear() del paquete recién creado.

"""import Redondear

def Suma(A,B):
    resultado = A + B
    return resultado
resultado = Suma(2.5,3.9)
print(Redondear.redondear(resultado))"""

# Usando el módulo datetime, escribe un programa que muestre la fecha
# y hora actuales del sistema.

import datetime
"""print(datetime.datetime.now())"""

# Escriba un programa que devuelva un número par al azar entre 2 y 10
# (pista: para comprobar si se pueden generar todos los números, pruebe
# ejecutar el programa dentro de un ciclo infinito).

import random
from random import randint
"""salida = 1
while salida%2 != 0:
    salida = randint(2,10)
print (salida)"""

# Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
# para la adivinación o para buscar consejo. Su mecanismo es muy simple:
# ante una pregunta del usuario, la bola responde con una de 8 posibles
# respuestas:
# - Es seguro que sí
# - Las chances son buenas
# - Puedes contar con ello
# - Pregúntame de nuevo más tarde
# - Concéntrate y pregunta de nuevo
# - No veo con claridad, intenta de nuevo
# - Mi respuesta es no
# - Mis fuentes me dicen que no
# Escriba una función en Python para similar la bola mágica

"""input("Pregúntale algo a la bola mágica:")
respuesta = randint(1,8)
if respuesta == 1:
    print("Es seguro que sí")
elif respuesta == 2:
    print("Las chances son buenas")
elif respuesta == 3:
    print("Puedes contar con ello")
elif respuesta == 4:
    print("Pregúntame de nuevo más tarde")
elif respuesta == 5:
    print("Concéntrate y pregunta de nuevo")
elif respuesta == 6:
    print("No veo con claridad, intenta de nuevo")
elif respuesta == 7:
    print("Mi respuesta es no")
elif respuesta == 8:
    print("Mis fuentes me dicen que no")"""

# Encuentre el tiempo de ejecución de los programas de los ejercicios
# anteriores (pista: use el módulo time)

"""fin= time.time()
tiempo_ejecutando = inicio - fin
print(f"El tiempo que dura toda la ejecución de este programa es {tiempo_ejecutando}")"""