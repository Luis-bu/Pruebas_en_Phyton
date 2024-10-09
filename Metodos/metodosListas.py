lista = list(["Hola","mundo",32, True])


#retorna la cantidad de elementos de la lista
cantidad_elementos=len(lista)

#agregar un elemento a la lista
lista.append(3.14)

#agregar un elemento en base al indice (desplaza los demás elementos)
lista.insert(0, "carlitos")

#agregar varios elementos de una lista a otra lista (van al final)
lista.extend([False, 0, "jajaja"])

#eliminar un elemento segun su indice (Con -1 elimina el último)
lista.pop(1) 

#eliminar un elemento por su valor
lista.remove(True)

#deja VACIA la lista
#lista.clear()

#Ograniza de forma ascendente (Con reverse=True se organizan de forma descendente)
#lista.sort()

#invierte los elementos de la lista
lista.reverse()

#busca un elemento en la lista según el valor
buscar = lista.index("mundo")


print(buscar)