#Tomar dos elementos de la bandeja de entrada sumarlos y ponerlos en la bandeja
#de salida.

from bandeja import *
bandeja=Bandeja(0,1,2,3,4,5,6,7)

while not bandeja.entrada_vacia():
    
    uno=bandeja.entrada()
    dos=bandeja.entrada()
    
    bandeja.salida(dos+uno)
