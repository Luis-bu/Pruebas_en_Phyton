
#Abriendo de forma optima
with open("Archivos\\texto.txt") as archivo:
      
    #Leemos el archivo
    contenido = archivo.read()
    print(contenido)
    
    
#No es necesario cerrarlo