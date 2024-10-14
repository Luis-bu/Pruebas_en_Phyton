import pandas as pd

#Asignando el contenido del csv a un data frame y cambiamos el nombre de los encabezados
df = pd.read_csv("Archivos\\archivo.csv", names=["Name", "Age", "Country", "Sex"])

#todo el csv
print(df)

#Obtenemos la columna con los nombres
nombres = df["Name"]    