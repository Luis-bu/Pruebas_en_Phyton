
#Usamos def para DEFINIR una función
def saludar(nombre):
    print(f"Hablaaaa {nombre}, ponte Crack")
    
def crearContraseña(num):
    chars="abcdefghij"
    num_entero=str(num)
    num=int(num_entero)
    c1=num-10
    c2=num+3
    c3=num+5
    c4=num-2
    c5=num+4
    contraseña=f"{chars[c1]}{chars[c2]}{chars[c3]}{chars[c4]}{chars[c5]}{num/2}"
    return contraseña
    
password=crearContraseña(3)
texto=f"Tu contraseña es: {password} felicidades"    


#Utilizando *args para parametros ilimitados (lo vuelve un iterable) -va al final
def suma(*numeros):
   return sum(numeros)
    
#print(suma(3,2,34,6,4,2,1,3,4,5,3,2))

#Parametro ya definido (se puede cambiar)
def frase(nombre, adjetivo="Inteligente"):
    return f"Hola {nombre}, eres muy {adjetivo}"

nom=input("Ingresa tu nombre: \n")
print(frase(nom))