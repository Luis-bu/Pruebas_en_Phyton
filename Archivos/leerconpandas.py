import pandas as pd

#Asignando el contenido del csv a un dataframe y cambiamos el nombre de los encabezados
df = pd.read_csv("Archivos\\archivo.csv", names=["name", "age", "country", "sex"])

#Imprimimos todo el dataframe
#print(df)

#Obtenemos la columna con los nombres
nombres = df["name"]

#Ogranizamos los valores por la edad ascendentemente (no cambia el original, crea un nuevo)
df_ascendente = df.sort_values("age")

#Ahora organizamos descendentemente
df_descendente = df.sort_values("age", ascending=False)
#print (df_descendente)

#Concatenando los 2 dataframes (recibe una lista con los df)
df_concatenado = pd.concat([df_ascendente,df_descendente])
#print(df_concatenado)

#Accediendo a la primeras filas con head(cuantas filas quiero ver)
primeras_filas = df.head(0)
#print(primeras_filas)

#Accediendo a las ultimas filas con tail(cuantas filas quiero ver)
ultimas_filas = df.tail(1)
#print(ultimas_filas)

#Accediendo a la cantidad de filas y columnas con shape
filas,columnas = df.shape
#print(filas)
#print(columnas)

#Obteniendo data estadistica del dataframe:
estadistica = df.describe()
#print(estadistica)

#Accediendo a un elemento especifico del dataframe [indice, elemento]
elemento_seleccionado = df.loc[1, "age"]
#print(elemento_seleccionado)

#Accediendo a todos elementos de una columna con loc
nombre = df.loc[:,"name"]

#Accediento a todos los elementos de una fila
primerapersona = df.loc[1,:]

#Accediendo a un elemento en base a su indice (indice fila, indice columna)
elemento_seleccionado2 = df.iloc[2,1]
#print(elemento_seleccionado2)

#Accediendo a todos elementos de una columna con iloc
nombres = df.iloc[:,0]
#print(primerapersona)

#Accediendo a todos los elementos de una fila con iloc(igual a loc)
segundapersona=df.iloc[2,:]
#print(segundapersona)

#convertir una columna a valores numericos
df["age"] =pd.to_numeric(df["age"], errors="coerce")

#Acceder a las filas que tengan edad mayor a 30 (necesario lo)
mayor_que_30 = df.loc[df["age"]>30,:]

print(mayor_que_30)