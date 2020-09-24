# Este programa intenta emular la funcionalidad de entrada (input) y salida (output) como en el juego
# Human Resource Machine.

class Bandeja:
    def __init__(self, *elementos):
        self.elementos = list(elementos)
        self.mutable = list(elementos)[::-1]
        self.resultados = []

    def entrada_vacia(self):
        # Checha si la bandeja de entrada esta vacia
        return len(self.mutable) == 0

    def entrada(self):
        # Saca un elemento de la "entrada" como en el juego, si no esta vacia
        # Regresa None si esta vacia
        if not self.entrada_vacia():
            return self.mutable.pop()

    def salida(self, cosa):
        # Pone un elemento en la "salida" como en el juego, no hay valor de "return"
        print(cosa)
        self.resultados.append(cosa)

    def verificar(self):
        pass
