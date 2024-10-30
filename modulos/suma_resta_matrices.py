import streamlit as st

def ingresar_matrices():
    num_filas = st.number_input("Número de filas", min_value=1, max_value=5, value=3)
    num_columnas = st.number_input("Número de columnas", min_value=1, max_value=5, value=3)
    
    A, B = [], []
    st.write("Ingrese los elementos de la Matriz A:")
    for i in range(num_filas):
        fila = []
        for j in range(num_columnas):
            valor = st.number_input(f"A[{i+1},{j+1}]", key=f"A_{i}_{j}")
            fila.append(valor)
        A.append(fila)
    
    st.write("Ingrese los elementos de la Matriz B:")
    for i in range(num_filas):
        fila = []
        for j in range(num_columnas):
            valor = st.number_input(f"B[{i+1},{j+1}]", key=f"B_{i}_{j}")
            fila.append(valor)
        B.append(fila)
    
    return A, B

def sumar_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def restar_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mostrar_resultado_matriz(matriz, operacion="Resultado"):
    st.write(f"\nMatriz {operacion}:")
    for fila in matriz:
        st.write(" ".join(map(str, fila)))

def suma_resta_matrices():
    st.header("Suma y Resta de Matrices")
    A, B = ingresar_matrices()
    
    if A and B:
        suma = sumar_matrices(A, B)
        resta = restar_matrices(A, B)
        mostrar_resultado_matriz(suma, "Suma")
        mostrar_resultado_matriz(resta, "Resta")
