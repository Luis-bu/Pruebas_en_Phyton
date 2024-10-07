#DECLARO MIS VARIABLES
nombre = "Pedro"
saludo= "Hola " + nombre + " ¿Como estas?"

#borramos la variable
del nombre

#F STRING QUE PASA TODO TIPO DE DATOS A TEXTO
personaQueNoCreoQueNadieSeLlameAsi=False
saludo2= f"Hola {personaQueNoCreoQueNadieSeLlameAsi} como estas?"

#imprimimos
print(saludo)
print(saludo2)

#Vemos si el String "Pedro" esta en mi variable saludo (booleano)
print("Pedro" in saludo)        #True

#"Mario" no esta en mi variable bienvenida? (booleano)
print("False" not in saludo2)    #False

#Operadores de pertenencia (in / not in)
