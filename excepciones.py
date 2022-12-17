# El manejo de excepciones nos permite continuar con el programa aún cuando surja un error interno 


try: 
    numero = int(input("Inserte un número: "))
except: 
    raise Exception("El valor introducido no es un número")
else: 
    print("Gracias por insertar el formato correcto!")
finally: 
    print("Procesando...")

'''
Localiza el error en el siguiente bloque de código. 
Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

suma = 10 + "12"
'''
'''
Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
resultado = 10/0
'''

'''
Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
colores['blanco']
'''

'''
Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. 
La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este 
elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:
'''

def agregar_una_vez(lista, elemento):
    if elemento in lista: 
        raise ValueError("Ese elemento ya está en la lista")
    else: 
        lista.append(elemento)
    return lista

lista = [1]

lista = agregar_una_vez(lista, 2)
print(lista)