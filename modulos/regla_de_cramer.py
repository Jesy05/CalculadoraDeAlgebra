# cramer_regla.py
import streamlit as st

def determinante_3x3_sarrus(matriz):
    """Calcula el determinante de una matriz 3x3 usando la regla de Sarrus."""
    return (matriz[0][0] * matriz[1][1] * matriz[2][2] +
            matriz[0][1] * matriz[1][2] * matriz[2][0] +
            matriz[0][2] * matriz[1][0] * matriz[2][1] -
            matriz[0][2] * matriz[1][1] * matriz[2][0] -
            matriz[0][0] * matriz[1][2] * matriz[2][1] -
            matriz[0][1] * matriz[1][0] * matriz[2][2])

def determinante_por_cofactores(matriz):
    """Calcula el determinante de una matriz cuadrada de tamaño NxN usando cofactores."""
    n = len(matriz)
    if n == 3:
        return determinante_3x3_sarrus(matriz)
    elif n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    det = 0
    for col in range(n):
        submatriz = [fila[:col] + fila[col+1:] for fila in matriz[1:]]
        cofactor = ((-1) ** col) * matriz[0][col] * determinante_por_cofactores(submatriz)
        det += cofactor
    return det

def cramer_regla(matriz, vector):
    """Implementa la regla de Cramer para resolver sistemas lineales Ax = b."""
    n = len(matriz)
    det_A = determinante_por_cofactores(matriz)
    if det_A == 0:
        st.write("El sistema no tiene solución única porque el determinante de la matriz es cero.")
        return None

    soluciones = []
    st.write(f"Determinante de la matriz A: {det_A}")
    for i in range(n):
        matriz_modificada = [fila[:] for fila in matriz]
        for j in range(n):
            matriz_modificada[j][i] = vector[j]

        det_Ai = determinante_por_cofactores(matriz_modificada)
        solucion_i = det_Ai / det_A
        soluciones.append(solucion_i)

        st.write(f"Matriz A con columna {i+1} reemplazada:")
        st.write(matriz_modificada)
        st.write(f"Determinante de la matriz A_{i+1}: {det_Ai}")
        st.write(f"Solución para x_{i+1}: {solucion_i}")

    return soluciones
