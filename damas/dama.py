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
    def __init__(self):
        
        self.tablero = [
            ['O', '-', 'O', '-', 'O', '-', 'O', '-'],
            ['-', 'O', '-', 'O', '-', 'O', '-', 'O'],
            ['O', '-', 'O', '-', 'O', '-', 'O', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', 'X', '-', 'X', '-', 'X', '-', 'X'],
            ['X', '-', 'X', '-', 'X', '-', 'X', '-'],
            ['-', 'X', '-', 'X', '-', 'X', '-', 'X']]



t = Tablero()

print( t.tablero[7] )
print( t.tablero[6] )
print( t.tablero[5] )
print( t.tablero[4] )
print( t.tablero[3] )
print( t.tablero[2] )
print( t.tablero[1] )
print( t.tablero[0] )

# print( t.tablero[2][4])
# print( t.tablero[3][5])
