#sacar de dos en dos los numeros de la bandeja de entrada y restar el primero
#menos el segundo y el segundo menos el primero y mandar ambos resultados a
#la bandeja de salida.

from bandeja import *
bandeja=Bandeja(5,7,2,3,0,1,0,0,10,5)
while not bandeja.entrada_vacia():

    loseta=bandeja.entrada()
    cosa=bandeja.entrada()
    bandeja.salida(loseta-cosa)
    bandeja.salida(cosa-loseta)
