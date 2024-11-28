import streamlit as st


def multiplicar_matriz_por_escalar(matriz, escalar):
    """
    Multiplica una matriz por un escalar.
    
    Parámetros:
        matriz (list of list): La matriz que será multiplicada.
        escalar (float): El número por el cual se multiplicará cada elemento de la matriz.
    
    Retorna:
        list of list: La matriz resultante después de la multiplicación.
    """
    # Validar que la matriz es una lista de listas
    if not isinstance(matriz, list) or not all(isinstance(fila, list) for fila in matriz):
        raise ValueError("La matriz debe ser una lista de listas.")
    
    # Validar que todos los elementos de la matriz son números
    if not all(isinstance(elemento, (int, float)) for fila in matriz for elemento in fila):
        raise ValueError("Todos los elementos de la matriz deben ser números.")
    
    # Multiplicar cada elemento de la matriz por el escalar
    matriz_resultante = [[elemento * escalar for elemento in fila] for fila in matriz]
    return matriz_resultante

# Ejemplo de uso directo:

