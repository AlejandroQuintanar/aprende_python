#Por cada elemento de la bandeja de entrada sacarlo, multiplicarlo por 40
#3 y sacar el resultado a la bandeja de salida.

from bandeja import *
bandeja=Bandeja(0,1,2,3,4,5,6)
while not bandeja.entrada_vacia():
    
    bandeja.salida(bandeja.entrada()*40)
    
