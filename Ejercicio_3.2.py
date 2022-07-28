#Numeros primos

def num_primes(n):
    
    for i in range (2,n):
        if n%i ==0 :
            return False
    return True
    
    

print("_______________________________")

numPrimos =  []
i = 2
try:
    cantidad = int(input("Ingrese que cantidad de números primos desea imprimir: "))
    
    while True:
        if (num_primes(i)):
            numPrimos.append(i)
            
            if (len(numPrimos) == cantidad):
                break
        i+=1
        
    
    print(numPrimos)
    
    
except ValueError:
    print("El dato ingresado es invalido")


