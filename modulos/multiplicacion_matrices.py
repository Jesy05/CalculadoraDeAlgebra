import numpy as np
import streamlit as st
import fractions as frac

# Función para multiplicar matrices
def multiplicar_matrices(A, B):
    """
    Multiplica dos matrices A y B.
    - A: Matriz 2D (lista de listas).
    - B: Matriz 2D (lista de listas).
    Devuelve la matriz resultado como lista de listas.
    """
    # Verificar dimensiones
    if len(A[0]) != len(B):
        raise ValueError("El número de columnas de A debe ser igual al número de filas de B.")
    
    # Inicializar matriz resultado
    filas_A, columnas_B = len(A), len(B[0])
    resultado = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]
    
    # Calcular el producto
    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(len(B)):
                resultado[i][j] += A[i][k] * B[k][j]
    return resultado

# Interfaz con Streamlit
def multiplicacion_matrices_streamlit():
    st.title("Multiplicación de Matrices")
    st.write("Ingrese las matrices A y B para calcular su producto.")
    
    # Entrada para la matriz A
    filas_A = st.number_input("Número de filas de A", min_value=1, step=1)
    columnas_A = st.number_input("Número de columnas de A", min_value=1, step=1)
    A = []
    for i in range(int(filas_A)):
        fila = st.text_input(f"Fila {i+1} de A (separada por comas)", key=f"A{i}")
        if fila:
            A.append([float(x) for x in fila.split(",")])
    
    # Entrada para la matriz B
    filas_B = st.number_input("Número de filas de B", min_value=1, step=1)
    columnas_B = st.number_input("Número de columnas de B", min_value=1, step=1)
    B = []
    for i in range(int(filas_B)):
        fila = st.text_input(f"Fila {i+1} de B (separada por comas)", key=f"B{i}")
        if fila:
            B.append([float(x) for x in fila.split(",")])
    
    # Validación y cálculo
    if len(A) == filas_A and len(B) == filas_B:
        try:
            resultado = multiplicar_matrices(A, B)
            st.write("Matriz resultado:")
            st.write(np.array(resultado))
        except ValueError as e:
            st.error(str(e))
    else:
        st.info("Complete todas las filas de las matrices para calcular el resultado.")

# Ejecución en Streamlit
if __name__ == "__main__":
    multiplicacion_matrices_streamlit()
