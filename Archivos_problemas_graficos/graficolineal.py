import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Archivos_problemas_graficos\\pedos.csv")

#Creamos el gráfico("variable independiente", "variable dependiente", de donde lo saca)
sns.lineplot(x="fecha",y="pedos",data=df)

#Mostramos un punto en la fech con más pedos
plt.plot("01-09",17,"o")

#Mostramos el gráfico
plt.show()