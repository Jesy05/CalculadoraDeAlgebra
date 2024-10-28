import streamlit as st
import numpy as np

# Función de eliminación Gaussiana
def gaussian_elimination(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        if matrix[i][i] == 0:
            st.error("Elemento de pivote es 0. El sistema puede no tener solución única.")
            return None
        for j in range(i + 1, rows):
            ratio = matrix[j][i] / matrix[i][i]
            matrix[j] = matrix[j] - ratio * matrix[i]
    
    # Resolución hacia atrás
    solutions = np.zeros(rows)
    for i in range(rows - 1, -1, -1):
        solutions[i] = (matrix[i, -1] - np.dot(matrix[i, i+1:rows], solutions[i+1:rows])) / matrix[i, i]
    return solutions

# Título principal de la página
st.title("Calculadora de Álgebra")

# Sección 1: Calculadora cuadrática
with st.expander("Calculadora cuadrática", expanded=True):
    st.header("Resolución de ecuaciones cuadráticas")
    a = st.number_input("Valor de a", value=1.0)
    b = st.number_input("Valor de b", value=1.0)
    c = st.number_input("Valor de c", value=1.0)
    
    if st.button("Calcular raíces"):
        discriminante = b**2 - 4*a*c
        if discriminante >= 0:
            root1 = (-b + np.sqrt(discriminante)) / (2*a)
            root2 = (-b - np.sqrt(discriminante)) / (2*a)
            st.write("Raíces reales:")
            st.write(f"Raíz 1: {root1}")
            st.write(f"Raíz 2: {root2}")
        else:
            st.write("No hay raíces reales.")

# Sección 2: Eliminación Gaussiana
with st.expander("Eliminación Gaussiana"):
    st.header("Resolución de Sistemas de Ecuaciones con Eliminación Gaussiana")
    st.write("Introduce una matriz aumentada para resolver el sistema.")

    # Configuración de la matriz aumentada
    rows = st.number_input("Número de ecuaciones", min_value=2, max_value=5, step=1, value=3)
    matrix = []
    
    for i in range(int(rows)):
        row = []
        for j in range(int(rows) + 1):
            val = st.number_input(f"Elemento ({i+1}, {j+1})", value=0.0, key=f"{i}-{j}")
            row.append(val)
        matrix.append(row)
    
    # Botón para resolver el sistema
    if st.button("Resolver con Gauss"):
        # Convertir a matriz de numpy
        matrix = np.array(matrix)
        solution = gaussian_elimination(matrix)  # Llamar a la función de eliminación gaussiana
        if solution is not None:
            st.write("Solución del sistema:")
            st.write(solution)
