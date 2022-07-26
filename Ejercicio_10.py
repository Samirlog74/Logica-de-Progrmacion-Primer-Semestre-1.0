# 10.Un BOING 747 tiene una capacidad de carga para equipaje de aproximadamente 18.000 kg. Desarrolle un algoritmo que controle la recepción de equipajes para este avión, sabiendo:
 # a. Un bulto no puede exceder la capacidad de carga del avión ni tampoco exceder los 500 Kg.
 #b. El valor por kilo del bulto es :
#- de 0 a 25 Kg. cero pesos
#- de 26 a 300 Kg., $1500 pesos por kilo de equipaje.
#- de 301 a 500 Kg. $2500 pesos por kilo de equipaje

#Para un vuelo cualquiera se pide:
#a. Número total de bultos ingresados para el vuelo
#b. Peso del bulto más pesado y del más liviano
#c. Peso promedio de los bultos
#d. Ingreso en pesos y en dólares por concepto de carga.

#Construya una tabla de seguimiento con no menos de 15 bultos para realizar la prueba del algoritmo 



print ("---------------------------------------------------")
print("Le damos la bienvenida a la recepción de equipaje.")

while True:
    try:
        cantidad = int(input("Cuantos bultos desea almacenar: "))
        break
    
    except ValueError:
        print("El dato ingresado es invalido.")

pesoMax = 18000
contador = 0
precio_total = []
bultos_list = []
table = " "
while contador < cantidad:

    try:
        print("\nNOTA: El bulto solo puede pesar entre (1-500kg).")
        bultos = float(input("Por favor ingrese el peso del bulto(kg): "))
        precio_almacen = 0
        if bultos <= 500 and bultos > 0:
            bultos_list.append(bultos)
            
            if sum(bultos_list) <= 18000:
                
                contador += 1
                if bultos <= 25 and bultos > 0:
                    precio_almacen += 0
                    precio_total.append(precio_almacen)


                elif bultos <= 300 and bultos > 26:
                    precio_almacen += 1500*bultos
                    precio_total.append(precio_almacen)


                elif bultos <= 500 and bultos > 301:
                    precio_almacen += 2500*bultos
                    precio_total.append(precio_almacen)


            else:
                print("El bulto debe tener un peso menor debido a que esta casi lleno el avión.")
                continue
            table = table + "\n   " + str(contador) + "      " + str(bultos) + "Kg    $" + str(precio_almacen) + "    $" + str(precio_almacen*0.00022)
        else:
            print("El peso ingresado no es valido.")
            continue
    
    except ValueError:
        print("El dato ingresado es invalido.")


print("\n---------------------------------------------------",
        "\nLista de seguimiento: ",
        "\nBulto #: " + " Peso(Kg): " + " Valor COP: " + " Valor USD: ")
print(table)


print ("\n---------------------------------------------------")
print("La cantidad de bultos ingresados fueron: ",cantidad)
print("Bulto más pesado: ", "{0:g}".format(max(bultos_list)),"Kg", " Bulto más liviano: ", "{0:g}".format(min(bultos_list)),"Kg." )
print("Promedio de peso: ","{0:g}".format(sum(bultos_list)/cantidad), "Kg.")
print("Ingresos totales: ", "COP: $","{0:g}".format(sum(precio_total)), " USD: $", "{0:g}".format(sum(precio_total)*0.00022))
print ("---------------------------------------------------")