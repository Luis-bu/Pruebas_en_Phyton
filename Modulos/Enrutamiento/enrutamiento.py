import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Modulos.modulo_saludar

print(Modulos.modulo_saludar.saludo_raro("Carlos", "Peréz", "serio"))