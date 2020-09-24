#Para este nivel necesitamos sacar las letras B,U,G a la bandeja de salida no
#hay bandeja de entrada.

from bandeja import Bandeja

bandeja=Bandeja()

#Para poder ver las diferencias del juego y python utilizaremos variables primero
#y un arreglo despues.

#Version 1:solo variables.

a = "A"
b = 1
c = "Dos"
d = "B"
e = 3
f = "U"
g = 7
h = "G"

bandeja.salida(d)
bandeja.salida(f)
bandeja.salida(h)

#Version 2, usando un arreglo.

arreglo = ["U", "a", 1 , "Dos", "B", 3, 4, 10, "BB", "G"]


bandeja.salida(arreglo[4])
bandeja.salida(arreglo[0])
bandeja.salida(arreglo[9])
