# 7. Desarrollar un algoritmo que llene un arreglo de 20 posiciones con números al azar entre 0 y 10. Posteriormente deberá mover todos los ceros que aparezcan al final del arreglo, manteniendo el orden relativo de los números que no son cero. Se deberá imprimir el arreglo antes y después del cambio.

import random

print ("---------------------------------------------------")

contador = 0
nums = []

while contador < 20: 

    num_random = random.randint(0,10)
    contador += 1
    nums.append(num_random)


print("Arreglo generado inicialmente: ",nums)

i = 0
for x in nums:
    if x:
        nums[i] = x
        i = i + 1

for x in range(i, len(nums)):
        nums[x] = 0

print("\nArreglo después del cambio: ",nums)