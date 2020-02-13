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

# class Tablero:
#     def __init__(self):
#         pass

#     def tablero(self):
#         self.horizontal = "| A | B | C | D | E | F | G | H |"
#         print(self.horizontal, "\n")

#         self.count = 0 
#         for t in range(64):
#             print('|', end=' - ')
#             self.count += 1
#             if self.count == 8:
#                 print('|', end='\n')
#                 self.count = 0
  
##################################


class Juego:

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
        self.horizontal = "  | A |  B |  C |  D |  E |  F |  G |  H |"
        print( self.horizontal, '\n' )
        
        # for i in range(1,8,2):
        #     self.tablero[0].insert(i, 'b')

        # for i in range(0,8,2):
        #     self.tablero[1].insert(i, 'b')
            
        # for i in range(1,8,2):
        #     self.tablero[2].insert(i, 'b')

        # for i in range(0,8,2):
        #     self.tablero[7].insert(i, 'n')

        # for i in range(1,8,2):
        #     self.tablero[6].insert(i, 'n')

        # for i in range(0,8,2):
        #     self.tablero[5].insert(i, 'n')

        # ad = self.tablero[0][0]
        # ga = ad.replace('b', 'h')
        # print( ga )
        
        # ah = self.tablero[0]
        # print( ah )

        for i, k in enumerate( self.tablero, start=1 ):
            print( i, k )


# t = Juego()

# print( t.valores() )

class Position( Juego ):
    def __init__(self, ficha, mover):
        self.ficha = ficha
        self.mover = mover

        self.pos = ficha.split(',')
        self.mov = mover.split(',')

        for fila in range(8):
            for col in range(8):
                if fila == int(self.pos[0]) and col == int(self.pos[1]):

                    if self.tablero[int(self.mov[0])][int(self.mov[1])] == ' ':
                        self.tablero[int(self.mov[0])][int(self.mov[1])] = 'n'
                        self.tablero[int(self.pos[0])][int(self.pos[1])] = ' '


po = Position('2,0', '3,1')

print( po.valores() )



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

# class Jugador( object ):
    
#     def __init__(self):

#         self.fichaI = FichaInicial(0, 0 )
            
#         value_row = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}    
#         rowv = input('Selecciona la fila inicial >>> ')
#         if rowv in value_row:
#             self.x = rowv 
#             colv = int( input( 'Selecciona la columna inicial >>> ' ) )
#             if colv in range(0,8):
#                 self.y = colv
#             else:
#                 print( "Columna fuera de rango. Intente de nuevo" )
#         else:
#             print( "Fila fuera de rango. Intente de nuevo" )



#     # print( 'Las letras representan las filas y los numeros las columnas.\nVas a seleccionar tu pieza, luego la moveras.' )
    
# g = Jugador()
# print( g )


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

# count = 0
# array = [ t for t in range(64) ] 
# print( array )

