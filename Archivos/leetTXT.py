
#Guarda una variable de tipo archivo
archivo_sin_leer = open("Archivos\\texto.txt")

#Leer el archivo completo (es un string)
#archivo = archivo_sin_leer.read()

#Guarda todas las lineas en un array
#lineas =archivo_sin_leer.readlines()

#Leer una sola línea (cantidad de caracteres a leer)
linea1=archivo_sin_leer.readline()

print(linea1)
