#Ej 2
"""Las siguientes matrices responden distintos patrones de relleno. Desarrollar funciones que generen cada una de ellas
sin intervención humana y escribir un programa que las invoque e imprima por pantalla.
El tamaño de las matrices debe establecerse como N x N, donde N se ingresa a través del teclado.
"""

#A

def generar_matriz_a(n: int) -> list:
    matriz = [[0] * n for _ in range(n)]
    matriz[0][0] = 1
    for i in range(1, n):
        matriz[i][i] = 3 * i
    return matriz

#B

def generar_matriz_b(n: int) -> list:
    matriz = [[0] * n for _ in range(n)]
    matriz[1][1] = 9
    matriz[2][2] = 3
    matriz[3][3] = 27
    return matriz

#C

def generar_matriz_c(n: int) -> list:
    matriz = [[0] * n for _ in range(n)]
    matriz[0][0] = 4
    for i in range(1, n):
        matriz[i][0] = 3 * i
    return matriz

#D

def generar_matriz_d(n: int) -> list:
    matriz = [[8] * n for _ in range(n)]
    for i in range(1, n):
        matriz[i][i] = 4
    return matriz

#E

def generar_matriz_e(n: int) -> list:
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        matriz[i][i] = i + 1
    return matriz

#F

def generar_matriz_f(n: int) -> list:
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        matriz[i][n - i - 1] = i + 1
    return matriz

#G

def generar_matriz_g(n: int) -> list:
    matriz = [[i + j + 1 for j in range(n)] for i in range(n)]
    return matriz


#H

def generar_matriz_h(n: int) -> list:
    matriz = [[i * j + 1 for j in range(1, n + 1)] for i in range(1, n + 1)]
    return matriz


#I

def generar_matriz_i(n: int) -> list:
    matriz = [[i * j + 2 * i for j in range(1, n + 1)] for i in range(1, n + 1)]
    return matriz



def main() -> None:

    """ solicitamos al usuario el valor de n y lo aplicamos a cada una de las funciones anteriores para obtener
    las matrices deseadas
    """

    n = int(input("Ingrese el tamaño de la matriz (n): "))


    print("Matriz a:")
    matriz_a = generar_matriz_a(n)
    for fila in matriz_a:
        print(fila)

    print("Matriz b:")
    matriz_b = generar_matriz_b(n)
    for fila in matriz_b:
        print(fila)

    print("Matriz c:")
    matriz_c = generar_matriz_c(n)
    for fila in matriz_c:
        print(fila)

    print("Matriz d:")
    matriz_d = generar_matriz_d(n)
    for fila in matriz_d:
        print(fila)

    print("Matriz e:")
    matriz_e = generar_matriz_e(n)
    for fila in matriz_e:
        print(fila)

    print("Matriz f:")
    matriz_f = generar_matriz_f(n)
    for fila in matriz_f:
        print(fila)

    print("Matriz g:")
    matriz_g = generar_matriz_g(n)
    for fila in matriz_g:
        print(fila)

    print("Matriz h:")
    matriz_h = generar_matriz_h(n)
    for fila in matriz_h:
        print(fila)

    print("Matriz i:")
    matriz_i = generar_matriz_i(n)
    for fila in matriz_i:
        print(fila)
        
if  __name__ == "__main__":
    main()
