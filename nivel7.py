#Envia a la bandeja de salida todo lo que no sea cero.
#Para saber si una cosa es cero en python tenemos el comando == 0.
#Ejemplo: 1==0, 0==0,  variable ==0
#Este comando regresa un valor de tipo buleano cuyos unicos dos valores son
#True y False

from bandeja import *
bandeja=Bandeja(1,9,5,0,3,7,0,4)
while not bandeja.entrada_vacia():
    baldosa=bandeja.entrada()
    if baldosa==0:
        continue #este comando salta al inicio del while sin ejecutar lo siguiente
    bandeja.salida(baldosa)
