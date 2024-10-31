import streamlit as st
from Calculadora1 import recibir_matriz  # Asegúrate de que la función esté en este módulo

def multiplicacion_matriz_por_vector(matriz, vector):
    if len(matriz[0]) != len(vector):
        st.error("El número de columnas de la matriz debe coincidir con la longitud del vector.")
        return None
    resultado = []
    for fila in matriz:
        suma = sum(fila[i] * vector[i] for i in range(len(vector)))
        resultado.append(suma)
    return resultado

def ejecutar_multiplicacion_matriz_por_vector(matriz, vector):
    st.write("### Multiplicación de Matriz por Vector")
    resultado = multiplicacion_matriz_por_vector(matriz, vector)
    if resultado:
        st.write("Resultado de la multiplicación:")
        st.write(resultado)
