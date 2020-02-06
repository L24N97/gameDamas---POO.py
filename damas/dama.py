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
    def __init__(self, xCord, yCord):
        self.xCord = xCord
        self.yCord = yCord     

    def imprimirTablero(self):
        self.horizontal = "| A | B | C | D | E | F | G | H |"
        print(self.horizontal, "\n")

        self.count = 0 
        for t in range(64):
            print('|', end=' - ')
            self.count += 1
            if self.count == 8:
                print('|', end='\n')
                self.count = 0



class Juego:
    def __init__(self):      
        self.tablero = [
            [' ', '-', ' ', '-', ' ', '-', ' ', '-'],
            ['-', ' ', '-', ' ', '-', ' ', '-', ' '],
            [' ', '-', ' ', '-', ' ', '-', ' ', '-'],
            ['-', ' ', '-', ' ', '-', ' ', '-', ' '],
            [' ', '-', ' ', '-', ' ', '-', ' ', '-'],
            ['-', ' ', '-', ' ', '-', ' ', '-', ' '],
            [' ', '-', ' ', '-', ' ', '-', ' ', '-'],
            ['-', ' ', '-', ' ', '-', ' ', '-', ' ']]

    def valores(self):
        self.horizontal = "    A |  B |  C |  D |  E |  F |  G |  H |"
        print(self.horizontal, "\n")

        for i in range(1,8,2):
            self.tablero[0].insert(i, 'b')

        for i in range(0,8,2):
            self.tablero[1].insert(i, 'b')
            
        for i in range(1,8,2):
            self.tablero[2].insert(i, 'b')

        for i in range(0,8,2):
            self.tablero[7].insert(i, 'n')

        for i in range(1,8,2):
            self.tablero[6].insert(i, 'n')

        for i in range(0,8,2):
            self.tablero[5].insert(i, 'n')

        for i, k in enumerate( self.tablero ):
            print( i, k)


    def posicion(self):
        self.tablero[0] = {1: 'b', 2: '-', 3: 'b', 4: '-', 5: 'b', 6: '-', 7: 'b', 8: '-' }
        self.tablero[1] = []
        self.tablero[2] = []
        self.tablero[3] = []
        self.tablero[4] = []
        self.tablero[5] = []
        self.tablero[6] = []
        self.tablero[7] = []
                        
# t = Juego()
# t.valores()
# # t.posicion()

# print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
# for i in range(0,8):
#             print("-"*32)
#             print(chr(i+97),end="| ")
#             for j in range(0,8):
#                 item = ((i,j)," ")
#                 print(str(item)+' |', end = " ")
#             print()
#             print("-"*32)



# def startBoard():
#         colorPos = [[None] * 8 for i in range(8)] # [[None]*8]*8
#         print(colorPos)
# startBoard()
