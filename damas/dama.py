""" 
Juego de Damas: 

Tomar en cuenta:  

-Investigar en qué consiste el juego.  
-Que el proyecto sea hecho a partir de lo aprendido en el curso de programación.  
-No enfocarse en gráficos ni nada relacionado a eso, solo a nivel de lógica. 
-Calidad del código. 
-Funcionamiento. 

Estructura lógica: 

Debe desarrollar la lógica para repartir los Damas.
Debe implementar la lógica del juego de Damas.
Debe tener un sistema de turnos y jugadores.
Debe tener sistema de puntuación según lo establecen las reglas del juego.
Propósito: Aplicar toda la estructura lógica con a través del uso del paradigma de Orientación a Objetos.

Criterios de evaluación. 

No aceptamos plagio de código. 
Culminación total del ejercicio. 
Evaluar la lógica/resolución de problemas. 
Tiempo de culminación.  
Evaluaciones y cursos son en “ingles” totalmente. 
Debe hacer provecho del uso de GIT & Github.
"""

class Tablero:

    # Variable de clase
    tablero = [
            ['b', '-', 'b', '-', 'b', '-', 'b', '-'],
            ['-', 'b', '-', 'b', '-', 'b', '-', 'b'],
            ['b', '-', 'b', '-', 'b', '-', 'b', '-'],
            ['-', ' ', '-', ' ', '-', ' ', '-', ' '],
            [' ', '-', ' ', '-', ' ', '-', ' ', '-'],
            ['-', 'n', '-', 'n', '-', 'n', '-', 'n'],
            ['n', '-', 'n', '-', 'n', '-', 'n', '-'],
            ['-', 'n', '-', 'n', '-', 'n', '-', 'n']
    ]

    def valores(self):
        self.horizontal = "  | 0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |"
        print( self.horizontal, '\n' )
      
        for i, k in enumerate( self.tablero ):
            print( i, k )


class Position( Tablero ):

    def __init__(self, ficha, mover):
        self.ficha = ficha
        self.mover = mover

        # Variables de entrada
        self.pos = ficha.split(',')
        self.mov = mover.split(',')

        # Definimos variables
        self.ficha_n = 'n'
        self.ficha_b = 'b'
        self.ficha_reina_negra = 'N'
        self.ficha_reina_blanca = 'B'
        self.ficha_vacia = ' '
        self.ficha_nula = '-'
        self.select_ficha = ' '
        self.movimientoInicial = self.tablero[ int( self.pos[0] ) ][ int( self.pos[1] ) ]
        self.movimientoFinal = self.tablero[ int( self.mov[0] ) ][ int( self.mov[1] ) ]
        self.movimientoValido = False
        self.jugador = self.select_ficha

    def selecFicha(self):
        # Detecta a que ficha pertenecen las coordenas ingresadas.
        
        if  self.movimientoInicial != self.ficha_nula:
            if self.movimientoInicial == 'n': 
                self.select_ficha = self.ficha_n
            elif self.movimientoInicial == 'b': 
                self.select_ficha = self.ficha_b
            elif self.movimientoInicial == 'B':
                self.select_ficha = self.ficha_reina_blanca
            elif self.movimientoInicial == 'N':
                self.select_ficha = self.ficha_reina_negra
            else:
                self.select_ficha = self.ficha_vacia
        else:
            print('Accion no permitida. Intentelo de nuevo')

    def movimientoFichas(self):
        self.selecFicha()
        
        # Movimiento En filas y Columnas
        self.movOriRow = int( self.pos[0] )  
        self.movFinRow = int( self.pos[1] ) 
        self.movOriCol = int( self.mov[0] ) 
        self.movFinCol = int( self.mov[1] ) 

        self.numeroCasilla = abs( self.movOriRow - self.movOriCol )
        self.numeroCasilla1 = abs( self.movFinRow - self.movFinCol )

        # Comprueba si las coordenadas ingresadas son igual a 1
        if self.numeroCasilla == 1 and self.numeroCasilla1 == 1:
            # Movimiento en casillas ficha blancas            
            if self.movimientoInicial == self.ficha_b:
                if self.movOriCol > self.movOriRow:
                    self.movimientoValido = True
            # Movimiento en casillas fichas negras
            elif self.movimientoInicial == self.ficha_n:
                if self.movOriCol < self.movOriRow:
                    self.movimientoValido = True
            # Movimiento en casillas reina blanca
            elif self.movimientoInicial == self.ficha_reina_blanca:
                self.movimientoValido = True
            # Movimiento en casillas reina negra
            elif self.movimientoInicial == self.ficha_reina_negra:
                self.movimientoValido = True


    def comerFicha(self):
        self.movimientoFichas()
        
        # Come fichas negras
        if  self.movimientoFinal == self.ficha_n:
            # Come a la derecha
            if self.tablero[ self.movOriRow + 2 ][ self.movFinRow + 2 ] == self.ficha_vacia:
                self.tablero[ self.movOriCol ][ self.movFinCol ] = self.ficha_vacia
                self.tablero[ self.movOriRow ][ self.movFinRow ] = self.ficha_vacia 
                self.tablero[ self.movOriRow + 2 ][ self.movFinRow + 2 ] = self.movimientoInicial
            # Come a la izquierda
            elif self.tablero[ self.movOriRow + 2 ][ self.movFinRow - 2 ] == self.ficha_vacia:
                self.tablero[ self.movOriCol ][ self.movFinCol ] = self.ficha_vacia
                self.tablero[ self.movOriRow ][ self.movFinRow ] = self.ficha_vacia 
                self.tablero[ self.movOriRow + 2 ][ self.movFinRow - 2 ] = self.movimientoInicial

        # # Come fichas blancas
        elif self.movimientoFinal == self.ficha_b:
            # Come a la izquierda
            if self.tablero[ self.movOriRow - 2 ][ self.movFinRow - 2 ] == self.ficha_vacia:
                self.tablero[ self.movOriCol ][ self.movFinCol ] = self.ficha_vacia
                self.tablero[ self.movOriRow ][ self.movFinRow ] = self.ficha_vacia
                self.tablero[ self.movOriRow - 2 ][ self.movFinRow - 2 ] = self.movimientoInicial 
            # Come a la derecha
            elif self.tablero[ self.movOriRow - 2 ][ self.movFinRow + 2 ] == self.ficha_vacia:
                self.tablero[ self.movOriCol ][ self.movFinCol ] = self.ficha_vacia
                self.tablero[ self.movOriRow ][ self.movFinRow ] = self.ficha_vacia
                self.tablero[ self.movOriRow - 2 ][ self.movFinRow + 2 ] = self.movimientoInicial     


    def convertirReina(self):
        self.movimientoFichas()
        
        # Reina Blanca
        if self.ficha_b in self.tablero[7]:
            self.tablero[ self.movOriCol ][ self.movFinCol ] = 'B'
        # Reina Negra
        elif self.ficha_n in self.tablero[0]:
            self.tablero[ self.movOriCol ][ self.movFinCol ] = 'N'

    def movimientoReina(self):
        self.convertirReina()

        if self.movimientoFinal == self.ficha_reina_negra or self.movimientoFinal == self.ficha_reina_blanca:
            
            # Come arriba a la derecha
            if self.tablero[ self.movOriRow + 2 ][ self.movFinRow + 2 ] == self.ficha_vacia:
                self.tablero[ self.movOriCol ][ self.movFinCol ] = self.ficha_vacia
                self.tablero[ self.movOriRow ][ self.movFinRow ] = self.ficha_vacia 
                self.tablero[ self.movOriRow + 2 ][ self.movFinRow + 2 ] = self.movimientoInicial
            # come arriba a la izquierda
            elif self.tablero[ self.movOriRow + 2 ][ self.movFinRow - 2 ] == self.ficha_vacia:
                self.tablero[ self.movOriCol ][ self.movFinCol ] = self.ficha_vacia
                self.tablero[ self.movOriRow ][ self.movFinRow ] = self.ficha_vacia 
                self.tablero[ self.movOriRow + 2 ][ self.movFinRow - 2 ] = self.movimientoInicial
            # Come abajo a la izquierda
            elif self.tablero[ self.movOriRow - 2 ][ self.movFinRow - 2 ] == self.ficha_vacia:
                self.tablero[ self.movOriCol ][ self.movFinCol ] = self.ficha_vacia
                self.tablero[ self.movOriRow ][ self.movFinRow ] = self.ficha_vacia
                self.tablero[ self.movOriRow - 2 ][ self.movFinRow - 2 ] = self.movimientoInicial 
            # Come abajo a la derecha
            elif self.tablero[ self.movOriRow - 2 ][ self.movFinRow + 2 ] == self.ficha_vacia:
                self.tablero[ self.movOriCol ][ self.movFinCol ] = self.ficha_vacia
                self.tablero[ self.movOriRow ][ self.movFinRow ] = self.ficha_vacia
                self.tablero[ self.movOriRow - 2 ][ self.movFinRow + 2 ] = self.movimientoInicial     


    def player(self):
        self.movimientoFichas()
        
        if self.movimientoValido:
            for fila in range(8):
                for columna in range(8):
                    self.selecFicha()
                    # Inserta las fichas. 
                    if ( fila == int( self.pos[0] ) and columna == int( self.pos[1] ) ) != self.ficha_nula:
                        # Selecciona y coloca las fichas
                        if self.movimientoFinal == self.ficha_vacia:
                            self.tablero[ self.movOriCol ][ self.movFinCol ] = self.select_ficha
                            self.tablero[ self.movOriRow ][ self.movFinRow ] = self.ficha_vacia
                        self.comerFicha()
                        self.movimientoReina()                        
                        
        else:
            print('Movimiento NO valido. Intentelo de nuevo\n')


    def victoria(self):
        self.selecFicha()

        self.hay_negras = False
        self.hay_blancas = False

        for self.victorias in self.tablero:
            for self.ganar in self.victorias:
                if self.ganar == self.ficha_n:
                    self.hay_negras = True 
                elif self.ganar == self.ficha_b:
                    self.hay_blancas = True                                     

def main():

    # print( 'Primero seleccione la columna luego la fila deseada.\n' )

    # po_izquierda = input('Selecciona la posicion inicial >>> ')
    # po_derecha = input('Selecciona la posicion final >>> ')
    # print( )
    # po = Position( po_izquierda, po_derecha )
    # po.player()    

    # while po.movimientoValido:
    #     if po.jugador == po.ficha_n:
    #         po.jugador = po.ficha_b
    #         print('Mueven las blancas: ')
    #     else:
    #         po.jugador = po.ficha_n
    #         print('Mueven las negras: ')

    #     print( po.valores () )
    


    i = 0
    while i < 25:

        po_izquierda = input('Selecciona la posicion inicial >>> ')
        po_derecha = input('Selecciona la posicion final >>> ')
        print( )

        po = Position( po_izquierda, po_derecha )
        po.player()
            
        print( po.valores () )

        i += 1

        print( )       

if __name__ == "__main__":
    main()



######################

# print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
# for i in range(0,8):
#             print("-"*32)
#             print(chr(i+97),end="| ")
#             for j in range(0,8):
#                 item = ((i,j)," ")
#                 print(str(item)+' |', end = " ")
#             print()
#             print("-"*32)



# count = 0 
# for t in range(64):
#     print('|', end=' - ')
#     count += 1
#     if count == 8:
#         print('|', end='\n')
#         count = 0

