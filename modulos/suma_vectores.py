import streamlit as st

def ingresar_vectores():
    n = st.number_input("Tamaño de los vectores (deben ser del mismo tamaño):", min_value=1, step=1)
    u, v = [], []
    
    st.write("Ingrese los elementos del vector u:")
    for i in range(n):
        elemento = st.number_input(f"u[{i+1}]", key=f"u_{i}")
        u.append(elemento)
    
    st.write("Ingrese los elementos del vector v:")
    for i in range(n):
        elemento = st.number_input(f"v[{i+1}]", key=f"v_{i}")
        v.append(elemento)
    
    return u, v

def sumar_vectores(u, v):
    return [u[i] + v[i] for i in range(len(u))]

def mostrar_resultado_vector(vector, nombre="Resultado"):
    st.write(f"\nVector {nombre}: {' '.join(map(str, vector))}")

def suma_vectores():
    st.header("Suma de Vectores")
    u, v = ingresar_vectores()
    
    if u and v and len(u) == len(v):
        resultado = sumar_vectores(u, v)
        mostrar_resultado_vector(resultado)
    else:
        st.write("Los vectores deben tener el mismo tamaño para ser sumados.")
