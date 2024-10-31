import streamlit as st
from modulos.eliminacionporgaus import eliminacion_por_gauss, print_matrix
from modulos.escalonada import forma_escalonada, imprimir_matriz, imprimir_solucion
from modulos.multiplicacion_vectores import multiplicacion_de_vectores
from modulos.multiplicacion_matriz_vector import multiplicacion_matriz_por_vector  # Nuevo módulo
from modulos.multiplicacion_vector_escalar import multiplicacion_vector_por_escalar
from modulos.suma_resta_matrices import sumar_matrices, restar_matrices
from modulos.suma_vectores import suma_vectores
from modulos.verificar_propiedad_distribucionalidad import verificar_propiedad_distribucionalidad
from modulos.recibir_matriz import recibir_matriz
from modulos.multiplicacion_matriz_vector import ejecutar_multiplicacion_matriz_por_vector



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


def recibir_vector():
    longitud = st.number_input("Longitud del vector", min_value=1, max_value=5, value=3)
    vector = []
    for i in range(longitud):
        valor = st.number_input(f"Elemento {i+1}", format="%.2f")
        vector.append(valor)
    return vector


def cramer_regla():
    st.write("### Regla de Cramer")
    st.write("Esta funcionalidad está en desarrollo.")


# Función para multiplicación de vector por escalar
def vector_escalar_multiplicacion():
    st.write("### Multiplicación de Vector por Escalar")
    escalar = st.number_input("Ingrese el valor del escalar", format="%.2f")
    vector = recibir_vector()  # Aquí recibes el vector
    # Asegúrate de que el vector no esté vacío antes de multiplicar
    if vector:  # Solo ejecuta si el vector tiene elementos
        resultado = multiplicacion_vector_por_escalar(vector, escalar)  # Pasa el vector primero y luego el escalar
        st.write("Resultado de la multiplicación de vector por escalar:")
        st.write(resultado)
    else:
        st.write("Por favor, ingresa un vector válido.")




# Función para multiplicación de matriz por vector
def matriz_vector_multiplicacion():
    matriz = recibir_matriz()
    vector = recibir_vector()
    
    # Verificar que el número de columnas de la matriz sea igual a la longitud del vector
    if len(matriz[0]) != len(vector):
        st.write("Error: El número de columnas de la matriz debe coincidir con el número de elementos en el vector.")
        return

    # Llamar a la función de multiplicación solo si las dimensiones son compatibles
    resultado = ejecutar_multiplicacion_matriz_por_vector(matriz, vector)
    st.write("Resultado de la multiplicación de matriz por vector:")
    st.write(resultado)



def matrices_multiplicacion():
    st.write("### Multiplicación de Matrices")
    st.write("Esta funcionalidad está en desarrollo.")


def inversa_matriz():
    st.write("### Inversa de una Matriz")
    st.write("Esta funcionalidad está en desarrollo.")


def propiedades_transpuesta():
    st.write("### Transposición con Verificación de Propiedades")
    st.write("Esta funcionalidad está en desarrollo.")


def transpuesta_simple():
    st.write("### Transposición Simple")
    st.write("Esta funcionalidad está en desarrollo.")


def matriz_determinante():
    st.write("### Determinante de una Matriz")
    st.write("Esta funcionalidad está en desarrollo.")


# Función principal de la calculadora
def main():
    st.title("Calculadora de Álgebra Lineal")
    st.write("Seleccione la operación que desea realizar:")

    # Menú principal
    menu_principal = st.selectbox("Menú de Categorías", [
        "Resolución de Sistemas de Ecuaciones",
        "Operaciones de Vectores",
        "Operaciones con Matrices",
        "Transformaciones de Matrices"
    ])

    # Submenús y llamadas a funciones
    if menu_principal == "Resolución de Sistemas de Ecuaciones":
        opcion = st.radio("Seleccione una operación:", ["Eliminación por Gauss", "Regla de Cramer"])
        if opcion == "Eliminación por Gauss":
            matriz = recibir_matriz()
            eliminacion_por_gauss(matriz)
        elif opcion == "Regla de Cramer":
            cramer_regla()

    elif menu_principal == "Operaciones de Vectores":
        opcion = st.radio("Seleccione una operación:", [
            "Multiplicación de vectores",
            "Suma de vectores",
            "Multiplicación de vector por escalar",
            "Multiplicación de matriz por vector",
            "Verificar propiedad A(u + v) = Au + Av"
        ])
        if opcion == "Multiplicación de vectores":
            multiplicacion_de_vectores()
        elif opcion == "Suma de vectores":
            suma_vectores()
        elif opcion == "Multiplicación de vector por escalar":
            vector_escalar_multiplicacion()
        elif opcion == "Multiplicación de matriz por vector":
            matriz_vector_multiplicacion()
        elif opcion == "Verificar propiedad A(u + v) = Au + Av":
            verificar_propiedad_distribucionalidad()

    elif menu_principal == "Operaciones con Matrices":
        opcion = st.radio("Seleccione una operación:", [
            "Suma de matrices",
            "Resta de matrices",
            "Multiplicación de matrices",
            "Inversa de una matriz"
        ])
        if opcion == "Suma de matrices":
            A = recibir_matriz()
            B = recibir_matriz()
            resultado = sumar_matrices(A, B)
            st.write("Resultado de la suma de matrices:")
            st.write(resultado)
        elif opcion == "Resta de matrices":
            A = recibir_matriz()
            B = recibir_matriz()
            resultado = restar_matrices(A, B)
            st.write("Resultado de la resta de matrices:")
            st.write(resultado)
        elif opcion == "Multiplicación de matrices":
            matrices_multiplicacion()
        elif opcion == "Inversa de una matriz":
            inversa_matriz()

    elif menu_principal == "Transformaciones de Matrices":
        opcion = st.radio("Seleccione una operación:", [
            "Transpuesta (propiedades)",
            "Transpuesta simple",
            "Determinante",
            "Matriz en forma escalonada"
        ])
        if opcion == "Transpuesta (propiedades)":
            propiedades_transpuesta()
        elif opcion == "Transpuesta simple":
            transpuesta_simple()
        elif opcion == "Determinante":
            matriz_determinante()
        elif opcion == "Matriz en forma escalonada":
            matriz = recibir_matriz()
            forma_escalonada(matriz)


if __name__ == "__main__":
    main()


