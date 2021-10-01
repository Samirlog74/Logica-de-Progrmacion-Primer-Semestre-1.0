cond="si"
def primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True
while cond == "si":
    numero=int(input("ingrese un Número Deseado: "))
    if primo(numero):
        print("El número ingresado es primo")
    else:
        print("El nuúmero ingresado no es primo")
    cond=input("¿Desea ingresar otro Número? ¿si o no? ")
    if cond == "no":
        print("Hasta luego, vuelva pronto.")
