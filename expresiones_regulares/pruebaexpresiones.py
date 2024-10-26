import re

#Buscar coincidencias numericas
texto = "Hay 12 perros y 3 gatos"

resultado = re.findall(r"\d{1,}", texto)

#print(resultado)


#Confirmar fecha

fecha = "30/03/2024"

confirmar = re.search(r"\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(18[0-9]{2}|19[0-9]{2}|20[0-4][0-9]|2050)\b", fecha)

#print(confirmar)


#Eliminar no letras

text = "Hola! ¿que tal va todo?123 "

text = re.sub(r"[^a-zA-Z]","", text)

print(text)

#Dividir en palabras

oracion = "hola123 a?? todos!! como!! vamos!!"

coincidencias = re.findall(r"[a-zA-Z]{1,}", oracion)

print(coincidencias)

#Ocltar un numero

txt = "Mi numero es +57 3159832222"

regex = r"\+\d{2} \d{10}"

mensaje = "Numero oculto"

arreglado = re.sub(regex, mensaje, txt)

print(arreglado)