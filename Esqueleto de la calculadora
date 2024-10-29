# Calculadora1.py

import streamlit as st
from modulos.eliminacionporgaus import eliminacion_por_gauss, print_matrix
from modulos.escalonada import forma_escalonada, imprimir_matriz, imprimir_solucion

# Título de la aplicación
st.title("Calculadora de Álgebra Lineal")

# Menú de opciones
opcion = st.sidebar.selectbox("Selecciona una operación:", [
    "Eliminación por Gauss",
    "Matriz de forma escalonada",
    "Multiplicación de vectores",
    "Vectores",
    "Ecuaciones vectoriales",
    "Transpuestas",
    "Determinante",
    "Regla de Cramer",
    "Matriz inversa"
])

# Ejecución del módulo para la eliminación por Gauss
if opcion == "Eliminación por Gauss":
    st.subheader("Eliminación por Gauss")
    
    n = st.number_input("Introduce el tamaño de la matriz aumentada (n x n+1):", min_value=2, max_value=10, step=1)
    
    # Entrada de los datos de la matriz
    matrix = []
    for i in range(int(n)):
        row = st.text_input(f"Fila {i + 1} (introduce los valores separados por espacios):")
        if row:
            matrix.append(list(map(float, row.split())))
    
    # Verificación y ejecución de la eliminación de Gauss
    if len(matrix) == n and all(len(row) == n + 1 for row in matrix):
        st.write("Matriz inicial:")
        print_matrix(matrix, [])
        
        result = eliminacion_por_gauss(matrix)
        
        if result:
            st.write("Matriz final (matriz unitaria):")
            for row in result:
                st.write(" ".join(f"{int(num)}" if num.is_integer() else f"{num:.2f}" for num in row))
    else:
        st.warning("Introduce todas las filas de la matriz.")

# Ejecución del módulo para la forma escalonada
if opcion == "Matriz de forma escalonada":
    st.subheader("Forma escalonada")
    
    # Obtener la matriz
    n = st.number_input("Introduce el tamaño de la matriz (n x n+1):", min_value=2, max_value=10, step=1)
    matrix = []
    for i in range(int(n)):
        row = st.text_input(f"Fila {i + 1} (introduce los valores separados por espacios):")
        if row:
            matrix.append(list(map(float, row.split())))

    # Verificar el tamaño y aplicar la forma escalonada
    if len(matrix) == n and all(len(row) == n + 1 for row in matrix):
        st.write("Matriz inicial:")
        imprimir_matriz(matrix)
        forma_escalonada(matrix)
        st.write("Matriz en forma escalonada:")
        imprimir_matriz(matrix)
        st.write("Solución:")
        imprimir_solucion(matrix)
    else:
        st.warning("Introduce todas las filas de la matriz correctamente.")
