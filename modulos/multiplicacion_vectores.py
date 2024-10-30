import streamlit as st

def ingresar_vectores():
    # Ingresar el tamaño de los vectores
    n = st.number_input("Ingrese el tamaño de los vectores (deben ser del mismo tamaño):", min_value=1, step=1)

    # Ingresar elementos del vector fila
    fila = []
    st.write(f"Ingrese los elementos del vector fila de tamaño {n}:")
    for i in range(n):
        elemento = st.number_input(f"Elemento fila {i+1}:", key=f"fila_{i}")
        fila.append(elemento)
    
    # Ingresar elementos del vector columna
    columna = []
    st.write(f"Ingrese los elementos del vector columna de tamaño {n}:")
    for i in range(n):
        elemento = st.number_input(f"Elemento columna {i+1}:", key=f"columna_{i}")
        columna.append(elemento)

    return fila, columna

def multiplicar_vectores(fila, columna):
    # Realizar la multiplicación fila por columna
    producto_punto = sum(f * c for f, c in zip(fila, columna))
    termino_matematico = [f"{fila[i]}*{columna[i]}" for i in range(len(fila))]
    
    # Mostrar el cálculo de manera matemática
    st.write("\nRealizando la multiplicación fila por columna:")
    st.write(f"Resultado: {' + '.join(termino_matematico)} = {producto_punto}")
    
    return producto_punto

def multiplicacion_de_vectores():
    st.header("Multiplicación de vectores (Fila por Columna)")
    fila, columna = ingresar_vectores()
    
    if fila and columna and len(fila) == len(columna):
        producto_punto = multiplicar_vectores(fila, columna)
        st.write("\nResultado de la multiplicación del vector fila por el vector columna:")
        st.write(producto_punto)
    else:
        st.write("Ingrese vectores de igual tamaño.")
