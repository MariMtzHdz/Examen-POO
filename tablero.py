import random

class Tablero:
    def __init__(self, vidas):
        self.matriz = [[0]*6 for i in range (6)]
        self.matriz_oculta = [[' ']*6 for i in range (6)]
        self.emojis = {0:'🗻',1:'🥭', 2:'🦂', 3:'🐍', 4:'🐊', 5:'🔑'}
        self.vidas = vidas

    def generar_matriz(self):
        valores = [1]*3 + [2]*2 + [3]*2 + [4]*1 + [5]*1

        random.shuffle(valores)

        posiciones = random.sample(range(36), len(valores))

        for idx, pos in enumerate(posiciones):
            fila, columna = divmod(pos, 6)
            self.matriz[fila][columna] = valores[idx]
    
    def mostrar_matriz(self):
        for fila in self.matriz:
            print(fila)

    def mostrar_matriz_oculta(self):
        print()
        print("Tablero oculto")
        for fila in self.matriz_oculta:
            print(' '.join(map(str, fila)))

    def descubrir_casilla(self, fila, columna):
        if 0 <= fila < 6 and 0 <= columna < 6:
            valor = self.matriz[fila][columna]
            self.matriz_oculta[fila][columna] =self.emojis[valor]

            if valor == 1:
                self.vidas += 1
            elif valor == 2:
                self.vidas -= 1
            elif valor == 3:
                self.vidas -= 1
            elif valor == 4:
                self.vidas = 0
            elif valor == 5:
                print('Ganaste')
        else:
            print("Coordenadas fuera del rango")

    def mostrar_matriz_real(self):
        print('Tablero real:')
        for fila in self.matriz:
            print(' '.join(self.emojis[val].ljust(2) for val in fila))
