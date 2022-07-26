# 1. Leer una cantidad variable de números e indicar cuanto suman todos los números, cuanto los números positivos y cuanto los números negativos.

print ("---------------------------------------------------")

cantidad = int(input("¿Qué cantidad de números desea ingresa?: "))

sumTotal = 0
sumNegativos = 0
sumPositivos = 0
contador = 0

while contador < cantidad:
    try:
        numero = int(input("Ingresa un número entero: "))
        sumTotal += numero

        if numero < 0:
            sumNegativos += numero

        else:
            sumPositivos += numero
        contador += 1

    except ValueError:
        print("El dato ingresado es invalido.")

print ("\n---------------------------------------------------")
print("La suma total de los números ingresados es: ", sumTotal,
"\nLa suma total entre todos los positivos es: ", sumPositivos,
"\nLa suma total entre todos los negativos es: " , sumNegativos)
print ("---------------------------------------------------")
