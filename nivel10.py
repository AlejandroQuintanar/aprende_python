#Sacar los numeros uno por uno, multiplicarlos por 8 y sacarlo a la salida.

from bandeja import *
bandeja=Bandeja(0,1,2,3,4,5,6)
while not bandeja.entrada_vacia():
    baldosa=bandeja.entrada()
    baldosa1=baldosa*8
    bandeja.salida(baldosa1)
    
    
    
