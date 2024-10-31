# input_helpers.py
import streamlit as st

def recibir_matriz():
    num_filas = st.number_input("Número de filas", min_value=1, max_value=5, value=3)
    num_columnas = st.number_input("Número de columnas", min_value=1, max_value=5, value=4)
    
    matriz = []
    for i in range(num_filas):
        fila = []
        for j in range(num_columnas):
            valor = st.number_input(f"Elemento ({i+1},{j+1})", format="%.2f")
            fila.append(valor)
        matriz.append(fila)
    
    return matriz
