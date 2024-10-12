
#Funcion comprimida
cuadrado=lambda x:x*x

print(cuadrado(5))

#Usando Filter 
numeros=[1,2,3,4,5,6,7,8,9,10]
#Buscamos los pares
pares=(filter(lambda num:num%2==0,numeros))

print(pares)