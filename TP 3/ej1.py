#Ej 1
"""Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada función:
a. Cargar números enteros en una matriz de N x N, ingresando los datos desde 
teclado. 
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como 
parámetro.
g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo 
una lista con los números de las mismas.
NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera 
sea el valor ingresado.
"""
#A

def cargar_matriz(n: int) -> list:
    """con el dato n proporcionado por el usuario, cargamos una matriz de tamaño n x n.
    """
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(int(input(f"Ingrese el elemento ({i}, {j}): ")))
        matriz.append(fila)
    return matriz

#B
        

def ordenar_filas(matriz: list) -> None:
    """ordena las filas de la matriz proporcionada en orden ascendente.
    """
    for fila in matriz:
        fila.sort()
        
        
#C

def intercambiar_filas(matriz: list, fila1: int, fila2: int) -> None:
    """
   intercambia las filas de la matriz proporcionada, en las posiciones indicadas por el usuario
    """
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]
    
#D

def intercambiar_columnas(matriz: list, col1: int, col2: int) -> None:
    """
    intercambia las columnas de la matriz proporcionada, en las posiciones indicadas por el usuario.
    """
    for fila in matriz:
        fila[col1], fila[col2] = fila[col2], fila[col1]
        
        
#E

def transponer_matriz(matriz: list) -> None:
    """intercambia cada elemento de la matriz proporcionada por sí mismo.
    """
    matriz[:] = [[fila[j] for fila in matriz] for j in range(len(matriz[0]))]
    
    
#F

def calcular_promedio_fila(matriz: list, fila: int) -> float:
    """calcula el promedio de los elementos en la fila de la matriz indicada por el usuario.
    """
    return sum(matriz[fila]) / len(matriz[fila])


#G

def calcular_porcentaje_impar_columna(matriz: list, col: int) -> float:
    """calcula los elementos impares en la columna de la matriz indicada por el usuario.
    """
    count = sum(1 for fila in matriz if fila[col] % 2 != 0)
    return (count / len(matriz)) * 100


#H

def es_simetrica_principal(matriz: list) -> bool:
    """controla si la matriz proporcionada por el usuario es simétrica respecto a su diagonal principal.
    """
    for i in range(len(matriz)):
        for j in range(i, len(matriz[0])):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True


#I

def es_simetrica_secundaria(matriz: list) -> bool:
    """controla si la matriz proporcionada por el usuario es simétrica respecto a su segunda diagonal.
    """
    for i in range(len(matriz)):
        for j in range(i, len(matriz[0])):
            if matriz[i][j] != matriz[-j-1][-i-1]:
                return False
    return True

#J

def encontrar_palindromos(matriz: list) -> list:
    """encuentra los palíndromos en la matriz proporcionada por el usuario
    """
    palindromos = []
    for col in range(len(matriz[0])):
        columna = [fila[col] for fila in matriz]
        if columna == columna[::-1]:
            palindromos.append(col)
    return palindromos

def main() -> None:
    """se solicitan los datos al usuario. utilizamos las funciones previas para mostrar en pantalla las operaciones realizadas
    """
    n = int(input("Ingrese el tamaño de la matriz (n): "))
    matriz = cargar_matriz(n)
    print("Matriz original:")
    imprimir_matriz(matriz)

    ordenar_filas(matriz)
    print("Matriz con filas ordenadas:")
    imprimir_matriz(matriz)

    fila1 = int(input("Ingrese el número de fila 1 para intercambiar: "))
    fila2 = int(input("Ingrese el número de fila 2 para intercambiar: "))
    intercambiar_filas(matriz, fila1, fila2)
    print("Matriz después de intercambiar filas:")
    imprimir_matriz(matriz)

    col1 = int(input("Ingrese el número de columna 1 para intercambiar: "))
    col2 = int(input("Ingrese el número de columna 2 para intercambiar: "))
    intercambiar_columnas(matriz, col1, col2)
    print("Matriz después de intercambiar columnas:")
    imprimir_matriz(matriz)

    transponer_matriz(matriz)
    print("Matriz transpuesta:")
    imprimir_matriz(matriz)

    fila = int(input("Ingrese el número de fila para calcular promedio: "))
    promedio = calcular_promedio_fila(matriz, fila)
    print(f"Promedio de la fila {fila}: {promedio}")

    col = int(input("Ingrese el número de columna para calcular porcentaje de impares: "))
    porcentaje = calcular_porcentaje_impar_columna(matriz, col)
    print(f"Porcentaje de impares en la columna {col}: {porcentaje}%")

    if es_simetrica_principal(matriz):
        print("La matriz es simétrica con respecto a su diagonal principal.")
    else:
        print("La matriz no es simétrica con respecto a su diagonal principal.")

    if es_simetrica_secundaria(matriz):
        print("La matriz es simétrica con respecto a su diagonal secundaria.")
    else:
        print("La matriz no es simétrica con respecto a su diagonal secundaria.")

    palindromos = encontrar_palindromos(matriz)
    if palindromos:
        print(f"Columnas palíndromas: {palindromos}")
    else:
        print("No hay columnas palíndromas.")
        
if  __name__ == "__main__":
    main()
