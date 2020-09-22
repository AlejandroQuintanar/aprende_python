#Primer nivel del juego, sacar tres valores de la entrada y ponerlos en la salida
from bandeja import Bandeja

bandeja=Bandeja(1,5,"a")

primero=bandeja.entrada()
segundo=bandeja.entrada()
tercero=bandeja.entrada()

bandeja.salida (primero)
bandeja.salida(segundo)
bandeja.salida(tercero)

