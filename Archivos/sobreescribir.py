#Escribir en un archivo, (sino lo encuentra, lo crea)
with open("Archivos\\texto.txt", "w") as archivo:
    
    #Sobre escribimos el archivo
    #pide un ITERABLE
    archivo.writelines(["Hola crack que me cuentas  de la vida\n", "Que me cuentas de la vida"])
