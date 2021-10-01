cond="si"
def frecuencia(numero):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       cantidad+=1
       numero=numero//10
   return cantidad
while cond=="si":
    hi=input("""¿Qué desea ingresar:
    1.Cedula de ciudadania.
    2.Tarjeta de identidad.
    : """)
    num=int(input("ingrese el número de identificación: "))
    if frecuencia(num)<4 and frecuencia(num)<12:
        print("El número de identificación es invalido.")
    else:
        print("El número de identificación es valido.")
        cond="no"
    cond=input("¿Quieres volver a ingresar un número de identificación?= ¿si o no? ")
    if cond =="no":
        print("Hasta la proxima.")
