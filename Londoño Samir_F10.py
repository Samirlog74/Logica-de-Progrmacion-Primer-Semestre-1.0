def lenUltimaPalabra(frase):
   if len(frase)==0:
       return 0
   cantidad=0
   for i in range(len(frase)):
       if frase[i]!=' ':
           cantidad+=1
       else:
           if i<len(frase)-1 and frase[i+1]!=' ':
               cantidad=0
   return cantidad
cadena = input("Ingrese la cadena o frase a procesar: ")
if lenUltimaPalabra(cadena):
    print(lenUltimaPalabra(cadena))
    print("Hasta luego, que vuelva pronto.")