import re

#Con mayuscula se vuelve: todo menos...

# "\d" Buscar digitos númericos del 0 al 9

# "\w" Buscar  caracteres alfanúmericos[A-Z, a-z, 0-9, _]

# "\s" Busca espacios en blanco

# "." Busca TODO menos los saltos en linea.

# "\n" Busca los saltos en linea

# "\" Cancelar caracteres especiales (no alfanúmericos), sivre para buscar cierto caracter

# "^" Busca el comienzo de una linea

# "$" Busca el final de una linea

# {n} Busca n cantidad de veces uno de las condiciones anteriores

# {n, m} Busca minimoo n, como máximo m de una de las condiciones anteriores

# "|" Busca una cosa o la otra


texto = "Lorem ipsum dolor sit amet consectetur adipiscing elit euismod inceptos vestibulum, blandit ut auctor eget fusce venenatis quisque sociis penatibus, leo mollis augue ac rhoncus feugiat senectus laoreet varius. Non et aliquam ad pretium sociosqu dictumst, nostra tempus fames ut lacus sagittis, malesuada imperdiet nisi euismod aenean. Suscipit vel morbi natoque ligula commodo et, nam placerat duis aenean tristique lacinia montes, in gravida ad dictum quisque. Justo nascetur fames sodales nostra interdum per magnis ornare, lacinia dignissim sociosqu consequat lobortis ridiculus lacus at, proin euismod nam gravida urna integer ultrices."

#Encontrar UNA coincidencia (que buscar, donde buscarlo)
resultado = re.search("Lorem", texto)
print(resultado)

#Buscar multiples coincidencias (Retorna un Array)
buscar = re.findall(r"\d", texto)
print(buscar)