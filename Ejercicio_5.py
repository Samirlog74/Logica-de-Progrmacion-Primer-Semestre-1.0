# 5. Desarrollar un algoritmo que llene un arreglo de 20 posiciones con números al azar entre 15 y 86. Posteriormente deberá ordenar el vector de manera descendente e imprimir el vector antes y después del ordenamiento.

import random

print ("---------------------------------------------------")

contador = 0
nums = []

while contador < 20: 

    num_azar = random.randint(15,86)
    contador += 1
    nums.append(num_azar)


print("Arreglo generado inicialmente: ",nums)
nums.sort(reverse = True)
print("\nArreglo ordenador de manera descendente: ",nums)