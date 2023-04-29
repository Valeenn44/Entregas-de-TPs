# Escriba una función que muestre todos los números primos entre 1 y un número n que es 
# ingresado por parámetro.

"""n=int(input("Ingrese un número:"))
def mostrar_primos(n):
    for i in range(1, n+1):
        es_primo = True
        for j in range(2, i):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            print(i)       
mostrar_primos(n)"""

# Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta
# que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje
# avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del
# programa de acuerdo a estos criterios:
# • Use un test condicional en el ciclo while para detener la ejecución.
# • Use un test condicional dentro del ciclo para decidir si continuar la ejecución. 
"""def sándwich1():
    ingreso = ""
    while ingreso != "salir":
        ingreso = input("Ingrese un ingrediente para su sándwich:")
        if ingreso != "salir":
            print(f"Ya se agregó el ingrediente: {ingreso}")
sándwich1()"""

"""def sandwich():
    ingreso1 = True
    while ingreso1:
        ingreso1 = input("Ingrese un ingrediente para su sándwich:")
        if ingreso1 == 'salir':
            ingreso1 = False
        else:
            print("Agregando", ingreso1, "al sándwich")
sandwich()"""

# A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un
# tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje
# describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez
# usando argumentos por posición. Llámela una segunda vez usando argumentos por clave.
# B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por
# defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los
# valores por defecto, y la segunda con valores diferentes. 

# A
"""def hacer_remera(tamaño, mensaje):
    print(f"Tamaño de remera: {tamaño}\nMensaje de remera: {mensaje}")
hacer_remera("M","Si")
hacer_remera(mensaje="Sis", tamaño="S")"""

# B
"""def hacer_remera(tamaño='L', mensaje='Me gusta Python'):
    print(f"Tamaño de remera: {tamaño}\nMensaje de remera: {mensaje}")
hacer_remera()
hacer_remera("M","No me gusta python")"""

# Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros
# de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo
# número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …). 

"""def fibonacci(n):
    fibonacci = [0,1]
    for i in range (2,n):
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
    print (fibonacci)
n = int(input("Ingrese un número:"))
fibonacci(n)"""