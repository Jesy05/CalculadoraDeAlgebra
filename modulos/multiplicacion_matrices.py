from fractions import Fraction
import streamlit as st

def recibir_matriz_local(key_prefix="matriz"):
    filas = st.number_input("Ingrese el número de filas:", min_value=1, step=1, key=f"{key_prefix}_filas")
    columnas = st.number_input("Ingrese el número de columnas:", min_value=1, step=1, key=f"{key_prefix}_columnas")
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = st.number_input(f"Ingrese el valor para la posición ({i+1}, {j+1}):", key=f"{key_prefix}_{i}_{j}")
            fila.append(valor)
        matriz.append(fila)
    return matriz

def multiplicar_matrices(A, B):
    if len(A[0]) != len(B):
        st.write("Error: El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda matriz.")
        return None

    resultado = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    return resultado

def multiplicacion_matrices():
    st.write("### Multiplicación de Matrices")
    A = recibir_matriz_local("matriz_A")
    B = recibir_matriz_local("matriz_B")
    
    if st.button("Multiplicar"):
        resultado = multiplicar_matrices(A, B)
        if resultado:
            st.write("Resultado de la multiplicación de matrices:")
            st.write(resultado)
