# transpuesta.py
import streamlit as st
import numpy as np


def calcular_transpuesta(matriz):
    """
    Función que recibe una matriz nxn y devuelve su matriz transpuesta.
    
    :param matriz: Lista de listas (matriz nxn)
    :return: Lista de listas (matriz transpuesta)
    """
    # Convertir la matriz en un array de numpy
    matriz_np = np.array(matriz)
    
    # Obtener la transpuesta de la matriz
    matriz_transpuesta = matriz_np.T
    
    # Convertir la matriz transpuesta de nuevo a lista de listas
    return matriz_transpuesta.tolist()
