# 8. Desarrollar un algoritmo que imprima el siguiente patrón utilizando un arreglo bidimensional:

import numpy as np

print("Patrón:")
print ("---------------------------------------------------")

cruz = np.zeros((9,9), dtype= int)
cruz[4] = 1
cruz[::, 4] = 1


print(cruz)
print ("---------------------------------------------------")