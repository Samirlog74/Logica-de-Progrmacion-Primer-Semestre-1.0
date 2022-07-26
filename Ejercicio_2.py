# 2. Leer una cantidad variable conocida de números e indicar finalmente cual fue el mayor número leído y cuantas veces fue ingresado.

from itertools import count


print ("---------------------------------------------------")

cantidad = int(input("¿Qué cantidad de números desea ingresa?: "))

numeros = []
contador = 0

while contador < cantidad:
    try:
        valor = int(input("Ingresa un número entero: "))
        numeros.append(valor)
        contador += 1
    except ValueError:
        print("El dato ingresado es invalido.")

valorMayor = max(numeros)
cantidadValor = numeros.count(valorMayor)

print ("\n---------------------------------------------------")
print("El mayor valor ingresado fue: ", valorMayor,
"\nEl maximo valor se repite: " , cantidadValor , " veces.")
print ("---------------------------------------------------")