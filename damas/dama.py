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
import os

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
        # Imprimir tablero
        self.horizontal = "  | 0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |"
        print( self.horizontal, '\n' )
      
        for i, k in enumerate( self.tablero ):
            print( i, k )
        return '' # Crear espacio en blanco luego del tablero
       

class Position( Tablero ):

    def __init__(self, ficha, mover, turno):
        self.ficha = ficha
        self.mover = mover
        self.turno = turno

        # Variables de entrada
        self.pos = ficha.split(',')
        self.mov = mover.split(',')

        # Definimos variables a utilizar
        self.ficha_n = 'n'
        self.ficha_b = 'b'
        self.ficha_reina_negra = 'N'
        self.ficha_reina_blanca = 'B'
        self.ficha_vacia = ' '
        self.ficha_nula = '-'
        self.select_ficha = ''
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
        self.movOriRow = int( self.pos[0] ) # MOVimientoORIginalROW
        self.movFinRow = int( self.pos[1] ) # MOVimientoFINalROW
        self.movOriCol = int( self.mov[0] ) # MOVimientoORIginalCOLum
        self.movFinCol = int( self.mov[1] ) # MOVimientoFINalCOLum

        self.numeroCasilla = abs( self.movOriRow - self.movOriCol )
        self.numeroCasilla1 = abs( self.movFinRow - self.movFinCol )
        
        # Comprueba si las coordenadas ingresadas son igual a 1
        if self.numeroCasilla == 1 and self.numeroCasilla1 == 1:
            # Determina el turno del jugador. | Jugador blancas 
            if self.turno == 0:
                # Movimiento en casillas ficha blancas
                if self.movimientoInicial == self.ficha_b:
                    if self.movOriCol > self.movOriRow:
                        self.movimientoValido = True

                # Movimiento en casillas reina blanca
                elif self.movimientoInicial == self.ficha_reina_blanca:
                    self.movimientoValido = True

            # Determina el turno del jugador. | Jugador negras    
            elif self.turno == 1:
                # Movimiento en casillas fichas negras
                if self.movimientoInicial == self.ficha_n:
                    if self.movOriCol < self.movOriRow:
                        self.movimientoValido = True
                
                # Movimiento en casillas reina negra
                elif self.movimientoInicial == self.ficha_reina_negra:
                    self.movimientoValido = True

            else:
                print('\t\tTurno no definido')
                self.movimientoValido = False

    def comerFicha(self):
        self.movimientoFichas()
        
        # Come fichas negras
        if self.tablero[ int( self.pos[0] ) ][ int( self.pos[1] ) ] == self.ficha_b:
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
        
        # Come fichas blancas
        elif self.tablero[ int( self.pos[0] ) ][ int( self.pos[1] ) ] == self.ficha_n:
            if self.movimientoFinal == self.ficha_b:
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
            self.tablero[ self.movOriCol ][ self.movFinCol ] = self.ficha_reina_blanca
        # Reina Negra
        elif self.ficha_n in self.tablero[0]: 
            self.tablero[ self.movOriCol ][ self.movFinCol ] = self.ficha_reina_negra
            
    def movimientoReina(self):
        self.convertirReina()                
        
        def comeArribaDerecha(self):
            self.tablero[ self.movOriCol ][ self.movFinCol ] = self.ficha_vacia
            self.tablero[ self.movOriRow ][ self.movFinRow ] = self.ficha_vacia 
            self.tablero[ self.movOriCol - 1 ][ self.movFinCol + 1 ] = self.movimientoInicial
        
        def comeArribaIzquierda(Self):
            self.tablero[ self.movOriCol ][ self.movFinCol ] = self.ficha_vacia
            self.tablero[ self.movOriRow ][ self.movFinRow ] = self.ficha_vacia 
            self.tablero[ self.movOriCol - 1 ][ self.movFinCol - 1 ] = self.movimientoInicial
        
        def comeAbajoIzquierda(self):
            self.tablero[ self.movOriCol ][ self.movFinCol ] = self.ficha_vacia
            self.tablero[ self.movOriRow ][ self.movFinRow ] = self.ficha_vacia 
            self.tablero[ self.movOriCol + 1 ][ self.movFinCol - 1 ] = self.movimientoInicial
        
        def comeAbajoDerecha(self):
            self.tablero[ self.movOriCol ][ self.movFinCol ] = self.ficha_vacia
            self.tablero[ self.movOriRow ][ self.movFinRow ] = self.ficha_vacia 
            self.tablero[ self.movOriCol + 1 ][ self.movFinCol + 1 ] = self.movimientoInicial
        
        # Comprueba si la reina negra puede comer
        if self.tablero[ int( self.pos[0] ) ][ int( self.pos[1] ) ] == self.ficha_reina_negra:
            if self.tablero[ int( self.mov[0] ) ][ int( self.mov[1] ) ] == self.ficha_b or self.tablero[ int( self.mov[0] ) ][ int( self.mov[1] ) ] == self.ficha_reina_blanca:
       
                # Comprueba si se come hacia abajo derecha
                if self.movOriCol > self.movOriRow and self.movFinCol > self.movFinRow:
                    if self.tablero[ int( self.mov[0] ) + 1  ][ int( self.mov[1] ) + 1 ] == self.ficha_vacia:
                        return comeAbajoDerecha(self)
                # Comprueba si se come hacia abajo izquierda
                elif self.movOriCol > self.movOriRow and self.movFinCol < self.movFinRow:
                    if self.tablero[ int( self.mov[0] ) + 1 ][ int( self.mov[1] ) - 1 ] == self.ficha_vacia:
                        return comeAbajoIzquierda(self)
                                   
                # Comprueba si se come hacia arriba izquierda
                if self.movOriCol < self.movOriRow and self.movFinCol < self.movFinRow:  
                    if self.tablero[ int( self.mov[0] ) - 1 ][ int( self.mov[1] ) - 1 ] == self.ficha_vacia:
                        return comeArribaIzquierda(self)    
                # Comprueba si se come hacia arriba derecha
                elif self.movOriCol < self.movOriRow and self.movFinCol > self.movFinRow:  
                    if self.tablero[ int( self.mov[0] ) - 1 ][ int( self.mov[1] ) + 1 ] == self.ficha_vacia:
                        return comeArribaDerecha(self)
        
        # Comprueba si la reina blanca puede comer
        elif self.tablero[ int( self.pos[0] ) ][ int( self.pos[1] ) ] == self.ficha_reina_blanca:
            if self.tablero[ int( self.mov[0] ) ][ int( self.mov[1] ) ] == self.ficha_n or self.tablero[ int( self.mov[0] ) ][ int( self.mov[1] ) ] == self.ficha_reina_negra:
                                
                # Comprueba si se come hacia abajo derecha
                if self.movOriCol > self.movOriRow and self.movFinCol > self.movFinRow:
                    if self.tablero[ int( self.mov[0] ) + 1  ][ int( self.mov[1] ) + 1 ] == self.ficha_vacia:
                        return comeAbajoDerecha(self)
                # Comprueba si se come hacia abajo izquierda
                elif self.movOriCol > self.movOriRow and self.movFinCol < self.movFinRow:
                    if self.tablero[ int( self.mov[0] ) + 1 ][ int( self.mov[1] ) - 1 ] == self.ficha_vacia:
                        return comeAbajoIzquierda(self)
                                   
                # Comprueba si se come hacia arriba izquierda
                if self.movOriCol < self.movOriRow and self.movFinCol < self.movFinRow:  
                    if self.tablero[ int( self.mov[0] ) - 1 ][ int( self.mov[1] ) - 1 ] == self.ficha_vacia:
                        return comeArribaIzquierda(self)    
                # Comprueba si se come hacia arriba derecha
                elif self.movOriCol < self.movOriRow and self.movFinCol > self.movFinRow:  
                    if self.tablero[ int( self.mov[0] ) - 1 ][ int( self.mov[1] ) + 1 ] == self.ficha_vacia:
                        return comeArribaDerecha(self)
        
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
                if self.ganar == self.ficha_n or self.ganar == self.ficha_reina_negra:
                    self.hay_negras = True 
                elif self.ganar == self.ficha_b or self.ganar == self.ficha_reina_blanca:
                    self.hay_blancas = True  

        if self.hay_blancas and self.hay_negras:
            return False
        else:
            return True                                   


# Ejecuta el programa 
def main():

    print( '\nBienvenidos al juego de damas.')
    print( 'Primero seleccione la columna luego la fila deseada.\nLos numeros deben estar separados por coma\n' )

    # Imprime el tablero de tablero estandar
    board = Tablero()
    print( board.valores() )
    turnox = 0 # Determina el turno del jugador

    # Corre el juego 
    while True:        

        if turnox == 0:
            turnox = 1
            print('Mueven las negras')
        elif turnox == 1:
            turnox = 0
            print('Mueven las blancas')        


        posicion_inicial = input('Selecciona la posicion inicial >>> ') 
        while True:
            if len(posicion_inicial) != 3 or posicion_inicial[1] != ',' or ( posicion_inicial[0] < '0' or posicion_inicial[0] > '7') or ( posicion_inicial[2] < '0' or posicion_inicial[2] > '7' ):
                print( 'Coordenadas ingresadas son incorrectas. Intentelo de nuevo' )
                posicion_inicial = input('Selecciona la posicion inicial >>> ') 
            else:
                break

        posicion_final = input('Selecciona la posicion final >>> ')
        while True:
            if len(posicion_final) != 3 or posicion_final[1] != ',' or ( posicion_final[0] < '0' or posicion_final[0] > '7') or ( posicion_final[2] < '0' or posicion_final[2] > '7' ):
                print( 'Coordenadas ingresadas son incorrectas. Intentelo de nuevo' )
                posicion_final = input('Selecciona la posicion final >>> ')           
            else:
                break

        print( ) # Crea espacio en blanco
        po = Position( posicion_inicial, posicion_final, turnox )
        po.player()        
        os.system ("cls") # Limpia la consola            
        print( po.valores() )
        
        if po.victoria():
            if (po.jugador == po.ficha_n) or (po.jugador == po.ficha_reina_negra):
                print(" --- GANAN LAS NEGRAS ! --- ")
                break
            else:
                print( " --- GANAN LAS BLANCAS ! --- ")
                break

if __name__ == "__main__":
    main()
