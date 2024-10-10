conjunto1= {1, 3, 5, 7}
conjunto2={8, 0, 2}

#(bool) verificar si un conjuto es un subconjunto de otro
resultado = conjunto2.issubset(conjunto1)

#(bool) Verificar si un conjunto es un superconjunto de otro
resultado2 = conjunto1.issuperset(conjunto2)

#verificar si NO hay números en común (si hay=False, No hay = True)
resultado3 = conjunto2.isdisjoint(conjunto1)


print(resultado)
print(resultado2)
print(resultado3)