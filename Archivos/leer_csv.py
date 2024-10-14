import csv
#Buscarlo
with open ("Archivos\\archivo.csv", encoding="UTF-8") as caja:
    print("Abierto correctamente")
    
    #Retorna un dato de tipo CSV, se recorre por filas
    leido=csv.reader(caja)
    for row in leido:
        print(row)