#Iterar un diccionario

diccionario=dict(nombre="pepe", apellido="Jose", salario=130000)

#Al hacer el bucle normal, imprime las keys
for valor in diccionario:
    print(valor)
    
#Con .items obtenemos una tupla de la forma (key, valor)
for value in diccionario.items():
    key, valor=value
    print(f"{key}: {valor}")