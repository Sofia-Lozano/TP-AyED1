#Ej 3
    """Desarrollar un programa para rellenar una matriz de N x N con números enteros al 
azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita. Imprimir la matriz por pantalla.
    """
    
import random

def generar_matriz_aleatoria(n: int) -> list:
    """tomando el parámetro n y con el uso de la biblioteca random, creamos una matriz de
    n x n  con números enteros al azar no repetidos comprendidos en el intervalo [0,N2).
    """
    matriz = []
    nums = list(range(n**2))
    random.shuffle(nums)
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(nums[i * n + j])
        matriz.append(fila)
    return matriz

def main() -> None:
    """solicitamos al usuario y el valor de n y lo aplicamos en la función anterior, mostrando
    el resultado por pantalla.
    """
    n = int(input("Ingrese el tamaño de la matriz (n): "))
    print("Matriz aleatoria:")
    matriz = generar_matriz_aleatoria(n)
    for fila in matriz:
        print(fila)
        
if  __name__ == "__main__":
    main()
