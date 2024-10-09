diccionario ={
    'nombre':"Luis",
    'apellido':"Bueno",
    'edad':17
}

#nos da las claves de lo diccionarios (se puede aplicar a una sola)
claves=diccionario.keys()

#obtiene un elemento según su key (no tira error)
obtener=diccionario.get("nombre")

#Eliminar todo el diccionario
diccionario.clear()
print(diccionario)