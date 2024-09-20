#Ej 4
"""Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas 
en cada una de sus plantas durante una semana. De este modo, cada columna representa el día de la semana
y cada fila a una de sus fábricas.
Se solicita:
a. Crear una matriz con datos generados al azar para N fábricas durante una 
semana, considerando que la capacidad máxima de fabricación es de 150 
unidades por día y puede suceder que en ciertos días no se fabrique ninguna. 
b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica. 
c. Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).
d. Cuál es el día más productivo, considerando todas las fábricas combinadas.
e. Crear una lista por comprensión que contenga la menor cantidad fabricada 
por cada fábrica.
"""

import random
#A

def generar_matriz_fabricacion(n: int) -> list:
    """tomamos el parámetro n brindado por el usuario y con la biblioteca random creamos una matriz cargando
    la producción de cada fábrica en una semana.
    """
    matriz = []
    for i in range(n):
        fila = [random.randint(0, 150) for _ in range(6)]
        matriz.append(fila)
    return matriz


def main() -> None:
    """solicitamos al usuario el valor de n y mostramos en pantalla los reportes.
    """    
    n = int(input("Ingrese el número de fábricas (n): "))

    print("Matriz de fabricación:")
    matriz = generar_matriz_fabricacion(n)
    for i, fila in enumerate(matriz):
        print(f"Fábrica {i+1}: {fila}")

    #B 
    print("Cantidad total de bicicletas fabricadas por cada fábrica:")
    for i, fila in enumerate(matriz):
        total = sum(fila)
        print(f"Fábrica {i+1}: {total}")

    #C
    """mostramos cuál es la fábrica que más produjo en un solo día, con detalle de día y fábrica.
    """    
    max_produccion = 0
    max_fabrica = 0
    max_dia = 0
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor > max_produccion:
                max_produccion = valor
                max_fabrica = i + 1
                max_dia = j + 1
    print(f"La fábrica que más produjo en un solo día es la fábrica {max_fabrica} con {max_produccion} bicicletas el día {max_dia}")

    #D
    """mostramos cuál fue el día más productivo, considerando todas las fábricas combinadas
    """    
    dias = [sum([fila[j] for fila in matriz]) for j in range(6)]
    max_dia_productivo = max(dias)
    print(f"El día más productivo es el día {dias.index(max_dia_productivo) + 1} con {max_dia_productivo} bicicletas")

    #E
    """mostramos la menor cantidad producida por cada fábrica
    """    
    menor_cantidad = [min(fila) for fila in matriz]
    print("Menor cantidad fabricada por cada fábrica:")
    for i, valor in enumerate(menor_cantidad):
        print(f"Fábrica {i+1}: {valor}")
        
if  __name__ == "__main__":
    main()
