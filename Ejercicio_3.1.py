#Numeros primos

import math

numPrimos = []
num = 2
contador = 0
res = ""

cantidad = int(input("Digite que cantidad de números primos desea imprimir: "))


while contador < cantidad:
    fact = math.factorial(num - 1)
    
    if (fact%num == (num - 1)):
        numPrimos.append(num)
        contador+=1
    num+=1

for j in range(len(numPrimos)):
    
    if res== "":
        res =str(numPrimos[j])
    else:
        res+= ", " + str(numPrimos[j])
        
print(f"\nlos primeros {cantidad} son: ")
print(res)