#Enviar todos los numeros a la salida, pero si uno es negativo, cambiarlo
#a positivo.



from bandeja import *
bandeja=Bandeja(0,-1,2,-3,3,-4,-4,5,-6)
while not bandeja.entrada_vacia():
    loseta=bandeja.entrada()
#    if loseta<0:
#El if anterior se puede eliminiar pues la funcion abs hace el trabajo
#por nosotros.
    loseta=abs (loseta)
    bandeja.salida(loseta)
     
