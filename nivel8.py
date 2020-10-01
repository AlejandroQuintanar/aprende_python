#Envia a la salida solo lo que sea cero.
#Para comparar un numero con otro o una variable con un numero o dos
#variables entre si, se usa el operador ==.
#El operador == de un lado debe de tener una cosa y del otro lado debe de tener
#la otra cosa1==cosa2
#El comparar una cosa con otra y preguntar si ambas son iguales puede ser
#verdad o no, en python se reprsenta la verdad como True y cuando es falso
#se representa con False. A estros valores se les llaman buleanos.
#En python el jump if zero se escribe con if buleano:
#si buleano es verdadero se ejecuta el codigo que este indentado debajo del if
# a ese codigo se le conoce como el cuerpo del if.
#Un modo de escribirlo seria :
#buleano=baldosa==0
#if buleano:
#bandeja.salida(baldosa)

from bandeja import *
bandeja=Bandeja(1,9,5,0,3,7,0,4)
while not bandeja.entrada_vacia():
    baldosa=bandeja.entrada()
    if baldosa==0:
        bandeja.salida(baldosa)
    

   
