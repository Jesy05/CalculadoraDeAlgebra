import streamlit as st
from sympy import sympify, Matrix

def ingresar_matrices():
    st.write("Ingrese las dimensiones de las matrices:")
    filas = st.number_input("Número de filas:", min_value=1, max_value=10, value=3, step=1)
    columnas = st.number_input("Número de columnas:", min_value=1, max_value=10, value=3, step=1)

    st.write("Ingrese los valores de la Matriz A:")
    matriz_a = []
    for i in range(filas):
        fila = []
        cols = st.columns(columnas)
        for j in range(columnas):
            entrada = cols[j].text_input(f"A[{i+1},{j+1}]", value="0")
            fila.append(sympify(entrada))
        matriz_a.append(fila)

    st.write("Ingrese los valores de la Matriz B:")
    matriz_b = []
    for i in range(filas):
        fila = []
        cols = st.columns(columnas)
        for j in range(columnas):
            entrada = cols[j].text_input(f"B[{i+1},{j+1}]", value="0")
            fila.append(sympify(entrada))
        matriz_b.append(fila)

    matriz_a = Matrix(matriz_a)
    matriz_b = Matrix(matriz_b)
    return matriz_a, matriz_b

def suma_resta_matrices():
    st.header("Suma y Resta de Matrices")
    A, B = ingresar_matrices()  # Matrices ingresadas como listas de sympy

    if A and B:
        suma = A + B
        if suma:
            st.subheader("Resultado de la Suma:")
            st.write(suma)

        resta = A - B
        if resta:
            st.subheader("Resultado de la Resta:")
            st.write(resta)
