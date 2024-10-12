
import math
def es_primo(num, contador=0):
    for i in range(2,int(math.sqrt(num))):
        if num%i==0:
           return False
       
    return True
   

def primos_hasta(n):
    for i in range(2, n):
        if(es_primo(i)):
            print(i)
            

primos_hasta(1000)