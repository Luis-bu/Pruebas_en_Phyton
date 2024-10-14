import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Archivos_problemas_graficos\\dispersion.csv")

sns.scatterplot(x="tiempo",y="dinero",data=df)


#Mostramos el gráfico
plt.show()
