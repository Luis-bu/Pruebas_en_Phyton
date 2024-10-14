nombres=["Luis","Carlos","David","Daniel","Santiago"]
apellidos=["Bueno","Valbuena","Eslava","Castro","Acevedo"]

with open ("Archivosaplicados\\nombres_y_apellidos.txt", "w") as archivo:
    archivo.write("Estos son los datos:\n\n")
    for nombre,apellido in zip(nombres, apellidos):
        archivo.write(f"Nombre: {nombre}\nApellido: {apellido}\n------------------------------\n")
    