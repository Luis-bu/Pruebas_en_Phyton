#arreglo convencional
lista = ["Luis",True,1.85]
print(lista[2])

#la tupla no se puede modificar con "()"
tupla = ("Bueno", False, 3.14,)
print(tupla[0])

#set
#no tienen un orden, el set se puede redefinir
#Los valores repetidos se omiten
conjunto={"Solano",'a',5555,}

#se pueden redefinir completamente
conjunto={"Te cague jajaja master"}
print(conjunto)


#diccionarios
diccionario ={
    'nombre':"luis bueno",
    'edad':17,
    'carrera':"ingenieria de sistemas"
}
print(diccionario["edad"]+3)
