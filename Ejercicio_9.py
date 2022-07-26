# 9. Desarrollar una aplicación que posea una función que reciba un arreglo y un valor y verifique si dicho valor existe en el arreglo. Para probar su funcionamiento el usuario debe generar un arreglo de tamaño variable que contiene números al azar entre 1 y 50 e indicar el número que desea buscar en el arreglo.

import random

print ("---------------------------------------------------")

def verificar_num(list,n1):

        if n1 in list:
            print("El número pertenece a la lista generada.")

        else:
            print("El número no pertenece a la lista generada.")

cantidad = int(input("¿Cuántos números al azar desea generar? (1 -50): "))     
contador = 0
nums = []

while contador < cantidad: 

    if cantidad >= 0:
        num_random = random.randint(1,50)
        contador += 1
        nums.append(num_random)
        
    else:
        break

valor = int(input("¿Qué número desea verificar si se encuentra en los números generados? "))

    
print("\nLos números generados fueron: ", nums)
print ("---------------------------------------------------")
print(verificar_num(nums,valor))