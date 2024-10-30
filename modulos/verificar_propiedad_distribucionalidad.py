import streamlit as st

def ingresar_matriz_y_vectores():
    num_filas = st.number_input("Número de filas de la matriz A", min_value=1, max_value=5, value=3)
    num_columnas = st.number_input("Número de columnas de la matriz A", min_value=1, max_value=5, value=3)
    
    A = []
    st.write("Ingrese los elementos de la matriz A:")
    for i in range(num_filas):
        fila = []
        for j in range(num_columnas):
            valor = st.number_input(f"A[{i+1},{j+1}]", key=f"A_{i}_{j}")
            fila.append(valor)
        A.append(fila)
    
    st.write("Ingrese los elementos del vector u:")
    u = [st.number_input(f"u[{i+1}]", key=f"u_{i}") for i in range(num_columnas)]
    
    st.write("Ingrese los elementos del vector v:")
    v = [st.number_input(f"v[{i+1}]", key=f"v_{i}") for i in range(num_columnas)]
    
    return A, u, v

def multiplicar_matriz_vector(A, vector):
    return [sum(A[i][j] * vector[j] for j in range(len(vector))) for i in range(len(A))]

def verificar_propiedad_distribucionalidad():
    st.header("Verificar Propiedad A(u + v) = Au + Av")
    A, u, v = ingresar_matriz_y_vectores()
    
    if len(A[0]) == len(u) == len(v):
        u_v_sum = [u[i] + v[i] for i in range(len(u))]
        Au_v = multiplicar_matriz_vector(A, u_v_sum)
        Au = multiplicar_matriz_vector(A, u)
        Av = multiplicar_matriz_vector(A, v)
        Au_Av = [Au[i] + Av[i] for i in range(len(Au))]
        
        if Au_v == Au_Av:
            st.write("La propiedad A(u + v) = Au + Av se cumple.")
        else:
            st.write("La propiedad A(u + v) = Au + Av no se cumple.")
        
        st.write(f"A(u + v): {Au_v}")
        st.write(f"Au + Av: {Au_Av}")
    else:
        st.write("Las dimensiones de la matriz A y los vectores u y v deben coincidir.")
