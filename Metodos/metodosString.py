
texto="hola mundo"


#MÉTODOS


#convierte a mayusculas
mayus=texto.upper()

#convierte a minusculas
minus=texto.lower()

#convierte todo a minus pero la primera letra en mayus
capitalizado=texto.capitalize();

#buscar un string adentro de otro
buscar = texto.find("h")

buscar2=texto.index("h") #si no encuentra, tira error


#Es numerico? (bool), sirve en string (tener en cuenta el espacio)
es_numerico=texto.isnumeric()

#Es alfanúmerico? (bool), sirve para string (tener en cuenta el espacio)
es_alfa=texto.isalpha()

#Contar cuantas veces encuentra una cadena dentro de otra
contar=texto.count("o")

#Empieza con? (bool) 
empieza=texto.startswith("ho")

#Termina con? (bool)
acaba=texto.endswith("do")

#Reemplaza un pedazo de cadena con otro (si no la encuentra no hace nada)
reemplazar =texto.replace("mundo", "Luis")

#Convierte la cadena en un ARRAY segun un paramétro
array = texto.split(" ")



#FUNCIÓN


#Cuenta el total de caracteres de una cadena
totalletras = len(texto)

dir = dir(texto)
print(dir)