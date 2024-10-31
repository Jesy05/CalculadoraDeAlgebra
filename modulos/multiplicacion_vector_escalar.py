import streamlit as st

def multiplicacion_vector_por_escalar(vector, escalar):
    return [x * escalar for x in vector]

def ejecutar_multiplicacion_vector_por_escalar():
    st.write("### Multiplicación de Vector por Escalar")
    tamano_vector = st.number_input("Tamaño del vector", min_value=1, max_value=10, value=3)
    
    vector = []
    for i in range(tamano_vector):
        valor = st.number_input(f"Elemento {i+1} del vector", format="%.2f")
        vector.append(valor)
    
    escalar = st.number_input("Escalar", format="%.2f")
    
    resultado = multiplicacion_vector_por_escalar(vector, escalar)
    st.write("Resultado de la multiplicación por escalar:")
    st.write(resultado)
