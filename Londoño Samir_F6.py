def factorial(numero):
   f=1
   if numero!=0:
       for i in range(1,numero+1):
           f=f*i
   return f
cantidad=0
num=int(input("ingrese un Número, si quiere finalizar el proceso ingrese -1: "))
while num!=-1:
    print("Factorial:", factorial(num))
    cantidad+=1
    num=int(input("ingrese un Número, si quiere finalizar el proceso ingrese -1: "))
print("Se leyeron",cantidad,"números ingresados")
