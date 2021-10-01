def validar(email):
    b= a.count("@")
    if b>=1:
        return True
    return False

a=input("Por favor ingrese su correo electronico:")  
if validar(a):
    print("Dirección de correo electronico valida")
else:   
    print("Dirección de correo electronico invalida")
