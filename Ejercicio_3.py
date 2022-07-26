# 3. Desarrolle un algoritmo que imprima los primeros N números primos. La cantidad N debe ser solicitada al usuario y los valores deben ser impresos separados por coma.


from kiwisolver import Constraint


print ("---------------------------------------------------")
num = int(input("¿Qué cantidad de números primos desea mostrar en pantalla? (número entero): "))

nums_primes = []
contador = 0

if contador < num:

    for i in range(2,num):
        creciente = 2
        prime = True

        while prime and creciente < i:
            if i % creciente ==  0:
                prime = False
            
            else:
                creciente += 1


        if prime:
            contador += 1
            nums_primes.append(i)
else:
    print("Número invalido.")



print("Los primeros " ,num, "números primos son: " , nums_primes)