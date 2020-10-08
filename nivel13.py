#Tomar de dos en dos de la entrada y comparar cada par de numeros
#si el par es igual, llevar el que sea de los dos numeros a la salida.
#Ignorar los pares que no sean iguales.


from bandeja import *
bandeja=Bandeja(0,0,1,2,3,3,4,4,5,6)
while not bandeja.entrada_vacia():
    baldosa1=bandeja.entrada()
    
    baldosa2=bandeja.entrada()
    if baldosa1==baldosa2:
        bandeja.salida(baldosa1)
        
