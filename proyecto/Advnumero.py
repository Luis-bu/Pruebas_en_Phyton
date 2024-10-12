import random
def juego():
 
    intentos=15
    numero_secreto=random.randint(1, 1000)
    

    while intentos!=0:
        print(f"Tienes {intentos} intentos")
        numero_usuario=int(input("Ingrese el numero: "))
        booleano=verificarNumero(numero_usuario, numero_secreto) 
        if (booleano):
         print(f"Felicidades, {numero_secreto} era el numero!!")
         break
        intentos-=1
    if (intentos==0):print("Mala suerte, no lo adivinaste")        
       
def verificarNumero(numero_usuario, numero_secreto):
    if numero_usuario<numero_secreto:
        print("El numero es mayor")
    elif numero_usuario>numero_secreto:
        print("El numero es menor")
    else:
        return True
    return False
juego()