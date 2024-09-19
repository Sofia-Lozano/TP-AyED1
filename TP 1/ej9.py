#Ej 9
    """Resolver el siguiente problema utilizando funciones:
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso 
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y 
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón 
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso 
de alguna naranja se encuentra fuera del rango indicado se la clasifica para 
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas 
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para 
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente 
reparto. Simular el peso de cada unidad generando un número entero al azar entre 
150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando que la ocupación
del camión no debe ser inferior al 80%; en caso contrario el camión no serán despachado por su alto costo.
"""

import random

def peso_naranja() -> int:
    """mediante la opción random, generamos un número entero entre 150 y 350 para simular
    el peso de las naranjas
    """
    return random.randint(150, 350)

def clasificar_naranjas(peso: int) -> str:
    """clasificamos las naranjas por peso para definir si se cargan en cajones
    o se convierten en jugo
    """
    if 200 <= peso <= 300:
        return "cajon"
    else:
        return "jugo"
    
def llenar_cajones(naranjas: list) -> tuple:
    """utilizando la función clasificar_naranjas, calculamos cuántos cajones se llenan, cuántas naranjas se
    convierten en jugo y si hay excedente para el próximo cargamento 
    """
    cajones = 0
    jugo = 0
    sobrante = 0
    for naranja in naranjas:
        if clasificar_naranjas(naranja) == "cajon":
            cajones += 1
            if cajones % 100 == 0:
                cajones -= 1
            else:
                sobrante += 1
        else:
            jugo += 1
    return cajones // 100, jugo, sobrante

def calcular_camiones(cajones: int) -> int:
    """recibiendo el parámetro de cajones, calculamos cuántos camiones se necesitan para transportar la cosecha
    """
    return (cajones // 5) 

def main() -> None:
    """se solicita al usuario el número de naranjas cosechadas y utilizando las funciones anteriores se
    crea un reporte completo
    """
    naranjas_cosechadas = int(input("Ingrese la cantidad de naranjas cosechadas: "))
    naranjas = [peso_naranja() for _ in range(naranjas_cosechadas)]
    cajones, jugo, sobrante = llenar_cajones(naranjas)
    camiones = calcular_camiones(cajones)
    print(f"Se pueden llenar {cajones} cajones.")
    print(f"Se necesitan {camiones} camiones para transportar la cosecha.")
    print(f"Se tienen {jugo} naranjas para jugo.")
    print(f"Se tienen {sobrante} naranjas sobrantes para el siguiente reparto.")