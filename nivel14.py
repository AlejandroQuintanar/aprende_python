#Tomar los numeros de la bandeja de entrada de dos en dos, si son iguales
#enviar el que sea de los dos a la bandeja de salida, si uno es mayor que otro
#enviar al mayor.

from bandeja import *
bandeja=Bandeja(0,0,1,2,3,3,4,4,5,6)
while not bandeja.entrada_vacia():
    baldosa1=bandeja.entrada()
    baldosa2=bandeja.entrada()
    if baldosa1>=baldosa2:
        bandeja.salida(baldosa1)
    else:
        bandeja.salida(baldosa2)
