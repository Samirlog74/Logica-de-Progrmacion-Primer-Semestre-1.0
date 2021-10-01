def sumaDigitos(numero):
  suma=0
  while numero!=0:
      digito=numero%10
      suma=suma+digito
      numero=numero//10
  return suma

#programa principal
cantidad=0
mayor=-1
numero=int(input("Ingrese un Número positivo a procesar, si quiere finalizar el proceso ingrese -1: "))
while numero>=0:
    suma=sumaDigitos(numero)
    if suma > mayor:
          mayor=suma
          n_mayorsuma=numero
    if suma < 10:
        cantidad+=1
    numero=int(input("Ingrese un Número positivo a procesar, si quiere finalizar el proceso ingrese -1: "))
print("Número con Sumatoria de dígitos mayor",n_mayorsuma,":",mayor)
print("Cantidad de numeros con una sumatoria de digitos55 menor a 10:",cantidad)
print("Hasta luego,vuelva pronto.")