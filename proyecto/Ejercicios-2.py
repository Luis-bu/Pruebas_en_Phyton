
compañeros=[]

for i in range(3):
    compañero=(input(f"Ingrese el nombre del alumno {i+1}: \n"))
    valor=(int(input(f"Ingrese la edad del compañero {i+1}: \n")))
    alumno=(compañero, valor)
    compañeros.append(alumno)
compañeros.sort(key=lambda x:x[1])
profesor=compañeros[0][0]
asistente=compañeros[-1][0]
print(f"El profesor es {profesor} y el asistente es {asistente}")