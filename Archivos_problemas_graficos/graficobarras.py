import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Archivos_problemas_graficos\\ingresos.csv")

sns.barplot(x="fuente",y="ingresos",data=df)

#Sumamos toda la columna con sus ingresos
total_ingresos=df["ingresos"].sum()
print(total_ingresos)

#Mostramos el gráfico
plt.show()
