#Instrucciones:Sacar todos los valores de la bandeja de entrada y mandarlos a
#la bandeja de salida.
from bandeja import Bandeja
bandeja=Bandeja(1,2,3,4,5,6,7,8,9)
#En python no hay jump, usaremos el comando for ... in ...:
#Este comando repite las lineas indentadas abajo de el mientras
#la bandeja no este vacia.

for registro in bandeja.elementos:
    bandeja.salida(registro)
    print("siguiente elemento")
    #fin del cuerpo del for
#Esto ya no es parte del cuerpo del for
print("terminamos")
print("hasta luego")
