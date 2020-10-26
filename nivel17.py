#Tomar todos los numeros de par en par y por cada par si el signo de ambos
#es igual sacar 0 a la bandeja de salida, si los signos son distintos sacar
#sacar el numero 1.


from bandeja import *
bandeja=Bandeja(0,0,-1,2,-3,3,-4,-4,5,-6,10,-3)
while not bandeja.entrada_vacia():
    loseta1=bandeja.entrada()
    loseta2=bandeja.entrada()
    if loseta1<0:
        if loseta2<0:
            bandeja.salida(0)
        else:
            bandeja.salida(1)
    else:
        if loseta2<0:
            bandeja.salida(1)
        else:
            bandeja.salida(0)
        
    

