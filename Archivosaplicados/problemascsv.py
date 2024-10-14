import pandas as pd
    
#cambiar el tipo de dato de una columna
df=pd.read_csv("Archivosaplicados\\archivo.csv")

#convertimos todos los datos a String
df["edad"]=df["edad"].astype(str)

print(type(df["edad"][1]))

#Cabiar coincidencias en una columna("que cambiar","con que cambiarlo", inplace=True)
df["sexo"].replace("No binario", "Gay", inplace=True)
print(df)

#Si hay datos que faltan en una fila, borra la fila comleta del Dataframe, es posible eliminar una columna con (axis=1) pero es raro
df.dropna()

#Elimina las filas repetidas
df.drop_duplicates()

#Crear un csv con los cambios aplicados
df.to_csv("Archivosaplicados\\datos_limpios.csv")
