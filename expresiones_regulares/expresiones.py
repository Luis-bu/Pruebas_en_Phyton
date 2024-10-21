import re

# /d Buscar digitos númericos del 0 al 9



texto = "Lorem ipsum dolor sit amet consectetur adipiscing elit euismod inceptos vestibulum, blandit ut auctor eget fusce venenatis quisque sociis penatibus, leo mollis augue ac rhoncus feugiat senectus laoreet varius. Non et aliquam ad pretium sociosqu dictumst, nostra tempus fames ut lacus sagittis, malesuada imperdiet nisi euismod aenean. Suscipit vel morbi natoque ligula commodo et, nam placerat duis aenean tristique lacinia montes, in gravida ad dictum quisque. Justo nascetur fames sodales nostra interdum per magnis ornare, lacinia dignissim sociosqu consequat lobortis ridiculus lacus at, proin euismod nam gravida urna integer ultrices."

#Encontrar UNA coincidencia (que buscar, donde buscarlo)
resultado = re.search("Lorem", texto)
print(resultado)

#Buscar multiples coincidencias
#Retorna un Array
buscar = re.findall(r"\D", texto)
print(buscar)