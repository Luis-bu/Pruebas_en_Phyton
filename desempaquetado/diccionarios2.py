#Crear diccionario con función
diccionario = dict(nombre="Luis", apellido="Bueno", edad=17)


#Las listas no pueden ser keys de mi diccionario
# diccionario=(["hola", "mundo"]: "xd") <---ERROR
#Con tuplas si se puede

#Creado diccionario con .fromkeys()
#Sirve para settear las keys al dar como parametro un elemento ITERABLE, TODOS los elementos seran None
diccionario=dict.fromkeys(["Apellido", "hola"])


#lo mismo, solo que ahora el segundo parametro sera el valor de TODAS las keys
diccionario=dict.fromkeys("ABCDEF", "Valor arbitrario")

print (diccionario)