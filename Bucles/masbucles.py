frutas = ["Banana", "Manzana", "Fresa", "Mora", "Ciruela", "Pera", "Naranja"]


#Continue hace que el bucle salte directaente a la siguiente iteración, sin hacer el resto de codigo
for fruta in frutas:
    if fruta=="Ciruela":
        continue
    print(f"Me voy a comer una {fruta}")

#Con Break hace que ACABE totalmente el bucle
for elemento in frutas:
    if elemento=="Pera":
        print("Las Peras me dan diarrea, ya no quiero nada más")
        break
    print(f"Me voy a comer una {elemento}")
    

#Nuevo array
Numeros=[2,5,8,10]
#Comprensión de listas
numeros_cuadrado=[x**2 for x in Numeros]
print (numeros_cuadrado)
