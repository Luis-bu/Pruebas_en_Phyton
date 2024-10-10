#datos
otros_cursos_min=2.5
otros_cursos_max=7
otros_cursos_prom=4
estecurso=1.5

#Crudos
crudo_promedio=5
crudo_estecurso=3.5



#calculo de las diferencias
diferencia_min= 100 - estecurso/otros_cursos_min *100
diferencia_max= 100 - estecurso * 1000//otros_cursos_max /10
diferencia_prom= 100 - estecurso/otros_cursos_prom*100

#Calulando tiempo vacio
tiempo_vacio_promedio= 100- otros_cursos_prom *1000 //crudo_promedio /10
tiempo_vacio_dalto=100-estecurso * 1000 //crudo_estecurso /10

#diferencias de duración
print(f"El  curso de dalto dura un {diferencia_min} % menos que el más rápido")

print(f"El curso de dalto dura un {diferencia_max}% menos que el más lento")

print(f"El curso de dalto dura un {diferencia_prom} % menos que el promedio de otros cursos")

#espacios vacios que se remueven
print(f"El curso promedio elimina un {tiempo_vacio_promedio}% del tiempo vacio")

print(f"Este curso elimina un {tiempo_vacio_dalto}% del tiempo vacio")

#Mostrar diferencias de cursos si son de 10 horas
print(f"Ver 10 horas de este curso equivalen a ver {otros_cursos_prom/estecurso*10} horas de este curso")
print(f"Ver 10 horas de otros cursos equivalen a ver {estecurso/otros_cursos_prom*10} horas de este curso")