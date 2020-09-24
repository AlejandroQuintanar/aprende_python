# Este programa intenta emular la funcionalidad de entrada (input) y salida (output) como en el juego
# Human Resource Machine.

class Bandeja:
    def __init__(self, *elementos):
        self.elementos = list(elementos)
        self.copia=list(elementos)[::-1]
        self.resultados = []

    def entrada(self):
        # Saca un elemento de la "entrada" como en el juego
        return self.copia.pop()


    def salida(self, cosa):
        # Pone un elemento en la "salida" como en el juego, no hay valor de "return"
        print(cosa)
        self.resultados.append(cosa)

    def verificar(self):
        pass
