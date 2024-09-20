#Ej 1
"""Desarrollar una función que determine si una cadena de caracteres es capicúa, sin 
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita 
verificar su funcionamiento.
"""
def es_capicua(s: str) -> bool:
    """verifica si la cadena brindada por el usuario es capicúa o no, retorna booleanos.
    """
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def main() -> None:
    """solicita al usuario una cadena de caracteres y lo valida utilizando la función es_capicua,
    muestra el resultado en pantalla
    """
    s = input("Ingrese una cadena de caracteres: ")
    if es_capicua(s):
        print("La cadena es capicúa.")
    else:
        print("La cadena no es capicúa.")
        
if  __name__ == "__main__":
    main()
