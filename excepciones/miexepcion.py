#Creo mi propia excepción
class MiExcepcion(Exception):
    def __init__(self, error):
        print(f"Has cometido un error y es el siguiente: {error}")
    
#Lanzando mi propia excepcion
#raise MiExcepcion("Jajajajaja, persona de poca formacion academica")

#Manejarla
try:
    raise MiExcepcion("Meterte a ver este git")
except:
    print("Obviamente ha ocurrido una excepcion")