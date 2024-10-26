#Crear funcion que suma
def sumarxd():
    print(f"Escriba 2 numeros para poder sumarlos\n")
    #Bucle para asegurarnos de que todo salga bien
    while True:
        
        #Intentamos hacer esta parte del codigo
        try:
            num1 = int(input("num1: "))
            num2 = int(input("num2: "))
            resultado = num1 + num2
            
        #Si algo sale mal, enviamos este mensaje 
        except Exception as e:
            print("Te pedí un numero pedazo de anormal") 
            print(f"ERROR:{e}")
            
        #El bucle solo acaba si el try ocurre  correctamente (else)
        else: break
        
        #Este codigo se ejecuta siempre (es raro verlo)
        finally:
            print("Hola mundo")
    return resultado

print(sumarxd())