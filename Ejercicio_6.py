# 6.  Desarrollar un algoritmo que llene dos arreglos A y B de 10 posiciones con números al azar entre 200 y 1000.  Posteriormente imprimir cada uno de los vectores y reemplazar los valores de A únicamente con los números  pares encontrados en B y reemplazar en B únicamente con los números impares encontrados en A.

import random

print ("---------------------------------------------------")

contador = 0
nums_A= []
nums_B = []
nums_A1= []
nums_B1 = []

while contador < 10: 
    num_random1 = random.randint(200,1000)
    num_random2 = random.randint(200,1000)
    contador += 1
    nums_A.append(num_random1)
    nums_B.append(num_random2)

for x in nums_B:
        if x % 2 == 0:
            nums_A1.append(x)

for x in nums_A:
        if x % 2 != 0:
            nums_B1.append(x)


print ("\n---------------------------------------------------")
print("Arreglos generados: ", "\nA: ",nums_A,"\nB: ", nums_B, "\nArreglos reemplazados: ", "\nA: ",nums_A1,"\nB: ", nums_B1)
