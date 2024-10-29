import streamlit as st
from modulos.eliminacionporgaus import eliminacion_por_gauss, print_matrix
from modulos.escalonada import forma_escalonada, imprimir_matriz, imprimir_solucion

# Función para recibir matrices como entrada
def recibir_matriz():
    num_filas = st.number_input("Número de filas", min_value=1, max_value=5, value=3)
    num_columnas = st.number_input("Número de columnas", min_value=1, max_value=5, value=4)
    
    matriz = []
    for i in range(num_filas):
        fila = []
        for j in range(num_columnas):
            valor = st.number_input(f"Elemento ({i+1},{j+1})", format="%.2f")
            fila.append(valor)
        matriz.append(fila)
    
    return matriz

# Funciones ficticias para representar cada operación en otras categorías
def cramer_regla():
    st.write("Regla de Cramer")

def multiplicacion_de_vectores():
    st.write("Multiplicación de vectores")

def vectores_suma():
    st.write("Suma de vectores")

def vector_escalar_multiplicacion():
    st.write("Multiplicación de vector por escalar")

def matriz_vector_multiplicacion():
    st.write("Multiplicación de matriz por vector")

def propiedad_verificacion():
    st.write("Verificar propiedad A(u + v) = Au + Av")

def matrices_suma():
    st.write("Suma de matrices")

def matrices_resta():
    st.write("Resta de matrices")

def matrices_multiplicacion():
    st.write("Multiplicación de matrices")

def matriz_escalar_multiplicacion():
    st.write("Multiplicación de matriz por un escalar")

def inversa_matriz():
    st.write("Matriz inversa")

def propiedades_transpuesta():
    st.write("Transpuesta con verificación de propiedades")

def transpuesta_simple():
    st.write("Transpuesta simple")

def matriz_determinante():
    st.write("Determinante")

# Función principal para Eliminación por Gauss
def gauss_eliminacion():
    st.write("### Eliminación por Gauss")
    matriz = recibir_matriz()
    resultado = eliminacion_por_gauss(matriz)
    if resultado:
        print_matrix(resultado, [])

# Función principal para Forma Escalonada
def escalonada_matriz():
    st.write("### Matriz en Forma Escalonada")
    matriz = recibir_matriz()
    forma_escalonada(matriz)
    imprimir_solucion(matriz)

# Menú Principal
st.title("Calculadora Algebraica")

menu_principal = st.selectbox("Seleccione una categoría:", 
                              ["Resolución de Sistemas de Ecuaciones", 
                               "Operaciones de Vectores", 
                               "Operaciones con Matrices", 
                               "Transformaciones de Matrices"])

# Submenús basados en la selección
if menu_principal == "Resolución de Sistemas de Ecuaciones":
    operacion = st.radio("Seleccione una operación:", ["Eliminación por Gauss", "Regla de Cramer"])
    if operacion == "Eliminación por Gauss":
        gauss_eliminacion()
    elif operacion == "Regla de Cramer":
        cramer_regla()

elif menu_principal == "Operaciones de Vectores":
    operacion = st.radio("Seleccione una operación:", 
                         ["Multiplicación de vectores", "Suma de vectores", 
                          "Multiplicación de vector por escalar", 
                          "Multiplicación de matriz por vector", 
                          "Verificar propiedad A(u + v) = Au + Av"])
    if operacion == "Multiplicación de vectores":
        multiplicacion_de_vectores()
    elif operacion == "Suma de vectores":
        vectores_suma()
    elif operacion == "Multiplicación de vector por escalar":
        vector_escalar_multiplicacion()
    elif operacion == "Multiplicación de matriz por vector":
        matriz_vector_multiplicacion()
    elif operacion == "Verificar propiedad A(u + v) = Au + Av":
        propiedad_verificacion()

elif menu_principal == "Operaciones con Matrices":
    operacion = st.radio("Seleccione una operación:", 
                         ["Suma de matrices", "Resta de matrices", 
                          "Multiplicación de matrices", 
                          "Multiplicación de matriz por un escalar", 
                          "Matriz inversa"])
    if operacion == "Suma de matrices":
        matrices_suma()
    elif operacion == "Resta de matrices":
        matrices_resta()
    elif operacion == "Multiplicación de matrices":
        matrices_multiplicacion()
    elif operacion == "Multiplicación de matriz por un escalar":
        matriz_escalar_multiplicacion()
    elif operacion == "Matriz inversa":
        inversa_matriz()

elif menu_principal == "Transformaciones de Matrices":
    operacion = st.radio("Seleccione una operación:", 
                         ["Transpuesta (propiedades)", "Transpuesta simple", 
                          "Determinante", "Matriz en forma escalonada"])
    if operacion == "Transpuesta (propiedades)":
        propiedades_transpuesta()
    elif operacion == "Transpuesta simple":
        transpuesta_simple()
    elif operacion == "Determinante":
        matriz_determinante()
    elif operacion == "Matriz en forma escalonada":
        escalonada_matriz()
