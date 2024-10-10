
#For in
mi_array=["Hola", "Mundo!!!", "Hello", "World!!!", "Español", "Ingles"]
numeros=[1, 2, 3, 4, 5, 6]


for palabra in mi_array:
    print(f"ahora mi texto es: {palabra}")

for numero in numeros:
    print(f"Mi numero multiplicado por 10 es: {numero*10}")

#Iterar dos o más listas a la vez (deben tener la misma cantidad de elementos) for x,y,z in zip(listas)
for texto,numero in zip(mi_array,numeros):
    print(f"La palabra numero: {numero} es: {texto}")


#Usando rango (para cierto número de veces)

for num in range(5,10):
    print(num)
    
#Forma de recorre una lista con su indice (el iterador se vuelve una tupla de la forma (indice,elemento))
for dato in enumerate(numeros):
    indice, valor =dato
    print(f"El indice es: {indice} y el dato que contiene es {valor}")
    
    
#For else (el else se ejecuta solo si el ciclo no fue interrumpido por un break)
for data in numeros:
    print(f"el numero es: {data}")
else:
    print ("El bucle llego a su fin con normalidad")
    
    
#LO ANTERIOR FUNCIONA EXACTAMENTE IGUAL PARA TUPLAS Y SETS