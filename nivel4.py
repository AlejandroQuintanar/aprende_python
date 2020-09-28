#Nivel4:Sacar de la bandeja de entrada de dos en dos y ponerlos en la bandeja
#de salida al reves
#Ejemplo:o,h,a,l=>h,o,l,a

from bandeja import Bandeja
bandeja = Bandeja("o", "h", "a", "l", 2,1 ,4,3,6,5,8,7,0,9)

while not bandeja.entrada_vacia():
    
    uno=bandeja.entrada()
    dos=bandeja.entrada()
    bandeja.salida(dos)
    bandeja.salida(uno)
    
