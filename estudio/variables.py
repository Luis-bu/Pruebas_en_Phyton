#DECLARO MIS VARIABLES
nombre = "Pedro"
saludo= "Hola " + nombre + " ¿Como estas?"

#borramos la variable
del nombre

#F STRING QUE PASA todo TIPO DE DATOS A TEXTO
personaQueNoCreoQueNadieSeLlameAsi=False
saludo2= f"Hola {personaQueNoCreoQueNadieSeLlameAsi} como estas?"

#imprimimos
print(saludo)
print(saludo2)

#Operadores de pertenencia (in / not in)
#Vemos si el String "Pedro" esta en mi variable saludo (booleano)
print("Pedro" in saludo)        #True

#"Mario" no esta en mi variable bienvenida? (booleano)
print("Mario" not in saludo2)    #False


