#Tomar los numeros de la entrada uno por uno y para cada uno imprimir el
#numero y sumarlo o restarlo imprimiendo uno por uno hasta llegar a cero.
#ejemplo: 3 2 1 0
#ejemplo: -2 -1 0
#Ejemplo: 0

from bandeja import *
bandeja = Bandeja(10,0,-10,2,-3,5,-3)
for valor in bandeja.elementos:
    loseta = valor
    while loseta != 0:
        bandeja.salida(loseta)    
        if loseta<0:
            loseta=loseta+1
        elif loseta>0:
            loseta=loseta-1
    bandeja.salida(loseta)
    
