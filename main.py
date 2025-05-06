from tablero import Tablero
from personaje import Personaje

def main():

    personaje = Personaje(5)

    tablero = Tablero(5)
    tablero.generar_matriz()
    tablero.mostrar_matriz_oculta()
    
    while True:
        fila = int(input('Ingresa una fila:'))
        columna = int(input('Ingresa una columna:'))
        tablero.descubrir_casilla(fila, columna)
        tablero.mostrar_matriz_oculta()
        print(f'Vidas: {tablero.vidas}')

if __name__ == "__main__":
    main()
