
print("Bienvenido a la calculadora!!!")
opcion=-1
while opcion!=0:
    print("Seleccione una opción: ")
    print("1) suma ")
    print("2) resta")
    print("3) multiplicacion")
    print("4) división")
    opcion = int(input())


    if opcion in [1, 2, 3, 4]:  
        num1 = int(input("Ahora ingrese el primer número: "))
        num2 = int(input("Ahora ingrese el segundo número: "))
        
    if opcion==1:
       print(f"La suma es {num1+num2}")
    elif opcion==2:
        print(f"La resta es: {num1-num2}")
    elif opcion==3:
        print(f"la multiplicación es: {num1*num2}")
    elif opcion==4:
        if (num2==0):
            print("Lo siento, no es posible dividir entre 0")
        else:
            print(f"La division es: {num1/num2}")
            
    elif opcion==0:
        print("Gracias por usar la calculadora")
    else:
        print("Opción no valida")
                            
            