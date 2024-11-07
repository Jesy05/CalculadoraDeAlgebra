import streamlit as st
from modulos.eliminacionporgaus import eliminacion_por_gauss, print_matrix
from modulos.escalonada import forma_escalonada, imprimir_matriz, imprimir_solucion
from modulos.multiplicacion_vectores import multiplicacion_de_vectores
from modulos.multiplicacion_matriz_vector import multiplicacion_matriz_por_vector, ejecutar_multiplicacion_matriz_por_vector
from modulos.multiplicacion_vector_escalar import multiplicacion_vector_por_escalar
from modulos.suma_resta_matrices import sumar_matrices, restar_matrices
from modulos.suma_vectores import suma_vectores
from modulos.verificar_propiedad_distribucionalidad import verificar_propiedad_distribucionalidad
from modulos.recibir_matriz import recibir_matriz, recibir_vector
from modulos.regla_de_cramer import cramer_regla

# Inicializar la clave 'pagina_inicial' en st.session_state si no existe
if 'pagina_inicial' not in st.session_state:
    st.session_state.pagina_inicial = True

# Función para cambiar a la calculadora
def cambiar_a_calculadora():
    st.session_state.pagina_inicial = False

# Página de presentación
if st.session_state.pagina_inicial:
    st.markdown(
        """
        <style>
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
        }
        .top-links {
            display: flex;
            justify-content: space-between;
            width: 100%;
            position: absolute;
            top: 10px;
        }
        .top-links div {
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="top-links">
            <div onclick="document.querySelector('input[value=\\'Sobre\\']').click()">Sobre</div>
            <div onclick="document.querySelector('input[value=\\'Configuración de Apariencia\\']').click()">Configuración de Apariencia</div>
            <div onclick="document.querySelector('input[value=\\'Notas de Uso\\']').click()">Notas de Uso</div>
        </div>
        <div class="centered">
            <h1>Calculadora de Álgebra Lineal</h1>
            <p>Aquí irá una descripción breve de la funcionalidad de la calculadora.</p>
            <button onclick="document.querySelector('button[data-testid=\\'stButton\\']').click()">Comenzar</button>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Comenzar"):
        cambiar_a_calculadora()

else:
    # Aquí inicia tu código de la calculadora de álgebra lineal
    pass

# Definiciones de funciones principales
def vector_escalar_multiplicacion():
    st.write("### Multiplicación de Vector por Escalar")
    escalar = st.number_input("Ingrese el valor del escalar", format="%.2f")
    vector = recibir_vector()
    if vector:
        resultado = multiplicacion_vector_por_escalar(vector, escalar)
        st.write("Resultado de la multiplicación de vector por escalar:")
        st.write(resultado)
    else:
        st.write("Por favor, ingresa un vector válido.")

def matriz_vector_multiplicacion():
    st.write("### Multiplicación de Matriz por Vector")
    matriz = recibir_matriz()
    vector = recibir_vector()
    
    if len(matriz[0]) != len(vector):
        st.write("Error: El número de columnas de la matriz debe coincidir con el número de elementos en el vector.")
        return

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

def cramer_calculadora():
    st.write("### Regla de Cramer")
    
    matriz = recibir_matriz()
    vector = recibir_vector()
    
    if len(matriz) != len(vector) or len(matriz) != len(matriz[0]):
        st.write("Error: La matriz debe ser cuadrada y el tamaño debe coincidir con el vector.")
        return

    soluciones = cramer_regla(matriz, vector)
    if soluciones:
        st.write("Soluciones del sistema:")
        for i, solucion in enumerate(soluciones, start=1):
            st.write(f"x_{i} = {solucion}")

# Función principal de la calculadora
def main():
    st.title("Calculadora de Álgebra Lineal")
    st.write("Seleccione la operación que desea realizar:")

    menu_principal = st.selectbox("Menú de Categorías", [
        "Resolución de Sistemas de Ecuaciones",
        "Operaciones de Vectores",
        "Operaciones con Matrices",
        "Transformaciones de Matrices"
    ])

    if menu_principal == "Resolución de Sistemas de Ecuaciones":
        opcion = st.radio("Seleccione una operación:", ["Eliminación por Gauss", "Regla de Cramer"])
        if opcion == "Eliminación por Gauss":
            st.write("### Eliminación por Gauss ")
            matriz = recibir_matriz()
            eliminacion_por_gauss(matriz)
        elif opcion == "Regla de Cramer":
            cramer_calculadora()

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
            st.write("### Suma de Matrices")
            A = recibir_matriz()
            B = recibir_matriz()
            resultado = sumar_matrices(A, B)
            st.write("Resultado de la suma de matrices:")
            st.write(resultado)
        elif opcion == "Resta de matrices":
            st.write("### Resta de Matrices")
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
            st.write("### Matriz en forma escalonada")
            matriz = recibir_matriz()
            forma_escalonada(matriz)

if __name__ == "__main__":
    main()
