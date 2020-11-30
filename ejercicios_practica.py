#Tomar dos elementos de la entrada, sumarlos y ponerlos en la bandeja
#de salida.

from bandeja import *
bandeja=Bandeja (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

while not bandeja.entrada_vacia():
    uno=bandeja.entrada()
    dos=bandeja.entrada()
    bandeja.salida(uno+dos)

    
def factorial (n):
    if n==0:
        return 1
    else:
        recursivo =factorial (n-1)
        resultando = n * recursivo
        return resultado



from bandeja import Bandeja
bandeja=Bandeja(1,2,3,4,5,6,7,8,9)

for registro in bandeja.elementos:
    bandeja.salida(registro)
    

print ("terminamos")
print ("hasta luego")
