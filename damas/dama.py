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


# t = Tablero()
# print( t.valores() )

class Position( Tablero ):
    def __init__(self, ficha, mover):
        self.ficha = ficha
        self.mover = mover

        self.pos = ficha.split(',')
        self.mov = mover.split(',')

        self.ficha_n = 'n'
        self.ficha_b = 'b'
        self.ficha_vacia = ' '
        self.ficha_nula = '-'
        self.select_ficha = None

        for fila in range(8):
            for columna in range(8):

                # Detecta a que ficha pertenecen las coordenas ingresadas.
                if self.tablero[ int( self.pos[0] ) ][ int( self.pos[1] ) ] == 'n': self.select_ficha = self.ficha_n
                elif self.tablero[ int( self.pos[0] ) ][ int( self.pos[1] ) ] == 'b': self.select_ficha = self.ficha_b

                # Mueve las fichas. 
                if fila == int( self.pos[0] ) and columna == int( self.pos[1] ):
                    if self.tablero[ int( self.mov[0] ) ][ int( self.mov[1] ) ] == self.ficha_vacia:
                        self.tablero[ int( self.mov[0] ) ][ int( self.mov[1] ) ] = self.select_ficha
                        self.tablero[ int( self.pos[0] ) ][ int( self.pos[1] ) ] = self.ficha_vacia

                    if self.tablero[ int( self.mov[0] ) ][ int( self.mov[1] ) ] == self.ficha_nula or self.tablero[ int( self.mov[0] ) ][ int( self.mov[1] ) ] == self.ficha_vacia : 
                        print("Seleccionar una ficha 'b' o 'n'")


                        


                    


# izq = input('>> ')
# der = input(">>> ")
# po = Position( izq, der )
# print( po.valores() )                


# class FichaInicial( Juego ):

#     def __init__(self, row, col):
#         self.row = row
#         self.col = col
        
#     def __repr__(self):
#         return self.tablero[ self.row ][ self.col ] 


# f = FichaInicial(1, 1)
# print( f.valores() )

# class FichaFinal( Juego ):

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return self.tablero[ self.x ][ self.y ]

# # c = Columna(2,4)
# # print( c )     
        


#     # print( 'Las letras representan las filas y los numeros las columnas.\nVas a seleccionar tu pieza, luego la moveras.' )


def main():

    i = 0
    while i < 9:
        po_izquierda = input('Selecciona la posicion inicial >>> ')
        po_derecha = input('Selecciona la posicion final >>> ')

        po = Position( po_izquierda, po_derecha )
        # movimientoValido = True

        print( po.valores () )

        i += 1

        print( )
    # def posicion_ficha():
    #     po_izquierda = input('Selecciona la fila inicial >>> ')
    #     po_derecha = input('Selecciona la columna inicial >>> ')
        
    
    # while movimientoValido:

    #     print( po.valores() )





        # if jugador == 'n': 
        #     print('Mueven las negras.')
        #     jugador = input('Que jugador eres: ')

        # elif jugador == 'b':
        #     print('Mueven las blancas.')
        #     jugador = input('Que jugador eres: ')

        # elif jugador == 'q': 
        #     break

        # else:
        #     print("Ingrese 'n', 'b' o 'q'")
        #     jugador = input('Que jugador eres: ')

        


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
