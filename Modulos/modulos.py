#Nos sirve para implementar cosas de otro archivo
#import modulo_saludar as sal

#saludo = sal.saludar("luis","Bueno","Inteligente")
#print(saludo)

#Si queres unicamente ciertas cosa del modulo
from modulo_saludar import saludar,saludo_raro

print(saludar("Pedro","Gonzales","Crack"))
print(saludo_raro("José", "Mendoza","Pendejo"))

