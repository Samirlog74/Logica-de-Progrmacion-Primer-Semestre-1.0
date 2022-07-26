# 4. Desarrollar un algoritmo que genere al azar N números entre 1 y 100. La cantidad N debe ser solicitada al usuario y los valores deben ser impresos separados por coma. Al finalizar se debe indicar cuál es el mayor y el menor número generado y el promedio de dichos números.

import random

print ("---------------------------------------------------")

cantidad = int(input("¿Cuántos números al azar desea generar? (1 -100): "))
        
contador = 0
nums = []

while contador < cantidad: 

    if cantidad >= 0:
        num_azar = random.randint(1,100)
        contador += 1
        nums.append(num_azar)
        
    else:
        break

valorMayor = max(nums)
valorMenor = min(nums)
promedio = sum(nums) / cantidad


print("Los números generados fueron: ",nums,"\n\nEl maximo valor fue: ", valorMayor, "\nEl valor mas bajo fue: ",valorMenor,"\nEl promedio de los números generados es: ", "{0:g}".format(promedio),".")

