import streamlit as st
from fractions import Fraction

def matriz_transpuesta():
    st.write("### Cálculo de la Matriz Transpuesta")
    
    # Configurar las dimensiones de la matriz
    st.write("Ingrese las dimensiones de la matriz:")
    filas = st.number_input("Número de filas", min_value=1, max_value=10, value=2, step=1)
    columnas = st.number_input("Número de columnas", min_value=1, max_value=10, value=2, step=1)

    # Entradas para la matriz
    st.write("Ingrese los valores de la matriz:")
    matriz = []
    for i in range(filas):
        fila = []
        cols = st.columns(columnas)
        for j in range(columnas):
            placeholder = f"({i+1},{j+1})"
            valor = cols[j].text_input(placeholder, value="", key=f"transpuesta_{i}_{j}")
            fila.append(valor)
        matriz.append(fila)

    # Botón para calcular la transpuesta
    if st.button("Calcular Transpuesta"):
        try:
            # Convertir las entradas a números (soporta fracciones, decimales e enteros)
            matriz = [[parsear_numero(celda) for celda in fila] for fila in matriz]

            # Calcular la transpuesta
            transpuesta = [[matriz[j][i] for j in range(filas)] for i in range(columnas)]

            # Mostrar el resultado
            st.subheader("Matriz Transpuesta:")
            st.table([[str(elem) for elem in fila] for fila in transpuesta])

        except ValueError as e:
            st.error(f"Error: {e}. Por favor, verifique los valores ingresados.")

# Función para convertir valores ingresados en enteros, decimales o fracciones
def parsear_numero(valor):
    """Convierte la entrada en un número válido, ya sea entero, decimal o fracción."""
    try:
        if "/" in valor:
            return float(Fraction(valor))
        return float(valor)
    except ValueError:
        raise ValueError("Entrada inválida. Use números en formato entero, decimal o fracción.")
