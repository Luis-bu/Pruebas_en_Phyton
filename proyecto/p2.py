texto= input ("Ingresa tu texto: \n")
array=texto.split(" ")
totalpalabras=len(array)
tiempo=totalpalabras/2

print(f"Tardarías {tiempo} segundos en decir esa palabra teniendo en cuenta una velocidad de 150 Palabras/minutos")

print(f"Dijiste {totalpalabras} palabras!!!")

if(tiempo>60):print("Tampoco te pedí la biblia crack")

tiempo_dalto=totalpalabras/(2*1.3)
print(f"Dalto tardaría solamente {tiempo_dalto} segundos!!")