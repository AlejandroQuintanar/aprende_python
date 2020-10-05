#Debemos tomar los numeros de la bandeja de entrada tripicarlos y sacarlos a
#la bandeja de salida.

from bandeja import *
bandeja=Bandeja (0,1,2,3,4,5)
while not bandeja.entrada_vacia():
    baldosa=bandeja.entrada()
    baldosa1=baldosa+baldosa+baldosa
    bandeja.salida(baldosa1)
    
