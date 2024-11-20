import streamlit as st
from modulos.eliminacionporgaus import eliminacion_por_gauss as eliminacion_por_gauss_modulo
from modulos.escalonada import forma_escalonada, imprimir_matriz, imprimir_solucion
from modulos.multiplicacion_vectores import multiplicacion_de_vectores
from modulos.multiplicacion_matriz_vector import multiplicacion_matriz_por_vector
from modulos.multiplicacion_vector_escalar import multiplicacion_vector_por_escalar
from modulos.suma_resta_matrices import sumar_matrices, restar_matrices
from modulos.suma_vectores import suma_vectores
from modulos.verificar_propiedad_distribucionalidad import verificar_propiedad_distribucionalidad
from modulos.recibir_matriz import recibir_matriz, recibir_vector
from modulos.regla_de_cramer import resolver_sistema
from modulos.juega import pantalla_juego

# Inicializar las claves en st.session_state si no existen
if 'pagina_inicial' not in st.session_state:
    st.session_state.pagina_inicial = True

# Función para cambiar a la calculadora
def cambiar_a_calculadora():
    st.session_state.pagina_inicial = True
    st.session_state.juego_activo = False

# Función para manejar el juego
def iniciar_juego():
    st.session_state.pagina_inicial = False
    st.session_state.juego_activo = True

# Barra lateral
with st.sidebar:
    st.title("Menú")
    if st.button("Calculadora", key="calculadora"):
        cambiar_a_calculadora()
    if st.button("Sobre", key="sobre"):
        st.session_state.show_sobre = not st.session_state.get('show_sobre', False)
    if st.session_state.get('show_sobre', False):
        st.write("### Sobre")
        st.write("Descripción sobre la calculadora.")

    if st.button("Notas de Uso", key="notas"):
        st.session_state.show_notas = not st.session_state.get('show_notas', False)
    if st.session_state.get('show_notas', False):
        st.write("### Notas de Uso")
        st.write("Notas sobre cómo usar la calculadora.")

    if st.button("Ayuda", key="ayuda"):
        st.session_state.show_ayuda = not st.session_state.get('show_ayuda', False)
    if st.session_state.get('show_ayuda', False):
        st.write("### Ayuda")
        st.write("Para más información sobre la calculadora contactar con mail@gmail.com.")    

    if st.button("Juega", key="juega"):
        iniciar_juego()

# Contenido principal de la calculadora
if st.session_state.pagina_inicial and not st.session_state.juego_activo:
    st.title(" ")

# Contenido del juego
elif st.session_state.juego_activo:
    pantalla_juego()
    for _ in range(100):
        st.write("")  # Añadir espacio para separar visualmente el contenido

else:
    # Definiciones de funciones principales
    def matriz_vector_multiplicacion():
        st.write("### Multiplicación de Matriz por Vector")
        matriz = recibir_matriz_local("matriz_vector")
        vector = recibir_vector_local("vector_matriz")
        
        if len(matriz[0]) != len(vector):
            st.write("Error: El número de columnas de la matriz debe coincidir con el número de elementos en el vector.")
            return

        resultado = ejecutar_multiplicacion_matriz_por_vector(matriz, vector)
        st.write("Resultado de la multiplicación de matriz por vector:")
        st.write(resultado)

    def matrices_multiplicacion():
        st.write("### Multiplicación de Matrices")
        st.write("Esta funcionalidad está en desarrollo.")


# Definiciones de funciones principales
def recibir_matriz_local(key_prefix="matriz"):
    filas = st.number_input("Ingrese el número de filas:", min_value=1, step=1, key=f"{key_prefix}_filas")
    columnas = st.number_input("Ingrese el número de columnas:", min_value=1, step=1, key=f"{key_prefix}_columnas")
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = st.number_input(f"Ingrese el valor para la posición ({i+1}, {j+1}):", key=f"{key_prefix}_{i}_{j}")
            fila.append(valor)
        matriz.append(fila)
    return matriz

def recibir_vector_local(key_prefix="vector"):
    longitud = st.number_input("Ingrese la longitud del vector:", min_value=1, step=1, key=f"{key_prefix}_longitud")
    vector = []
    for i in range(longitud):
        valor = st.number_input(f"Ingrese el valor para la posición {i+1}:", key=f"{key_prefix}_{i}")
        vector.append(valor)
    return vector

def matriz_vector_multiplicacion():
    st.write("### Multiplicación de Matriz por Vector")
    matriz = recibir_matriz_local("matriz_vector")
    vector = recibir_vector_local("vector_matriz")
    
    if len(matriz[0]) != len(vector):
        st.write("Error: El número de columnas de la matriz debe coincidir con el número de elementos en el vector.")
        return

    resultado = ejecutar_multiplicacion_matriz_por_vector(matriz, vector)
    st.write("Resultado de la multiplicación de matriz por vector:")
    st.write(resultado)

def matrices_multiplicacion():
    st.write("### Multiplicación de Matrices")
    st.write("Esta funcionalidad está en desarrollo.")

def ejecutar_multiplicacion_matriz_por_vector(matriz, vector) -> list[int]:
    resultado = [sum(matriz[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matriz))]
    return resultado

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
    
    matriz = recibir_matriz_local("matriz_cramer")
    vector = recibir_vector_local("vector_cramer")
    
    if len(matriz) != len(vector) or len(matriz) != len(matriz[0]):
        st.write("Error: La matriz debe ser cuadrada y el tamaño debe coincidir con el vector.")
        return

    soluciones = resolver_sistema(matriz, vector)
    if soluciones:
        st.write("Soluciones del sistema:")
        for i, solucion in enumerate(soluciones, start=1):
            st.write(f"x_{i} = {solucion}")

def suma_vectores():
    st.write("### Suma de Vectores")
    vector1 = recibir_vector_local("vector1")
    vector2 = recibir_vector_local("vector2")
    
    if len(vector1) != len(vector2):
        st.write("Error: Los vectores deben tener la misma longitud.")
        return
    
    resultado = [vector1[i] + vector2[i] for i in range(len(vector1))]
    st.write("Resultado de la suma de vectores:")
    st.write(resultado)

def multiplicacion_de_vectores():
    st.write("### Multiplicación de Vectores")
    vector1 = recibir_vector_local("vector1")
    vector2 = recibir_vector_local("vector2")
    
    if len(vector1) != len(vector2):
        st.write("Error: Los vectores deben tener la misma longitud.")
        return
    
    resultado = [vector1[i] * vector2[i] for i in range(len(vector1))]
    st.write("Resultado de la multiplicación de vectores:")
    st.write(resultado)

def multiplicacion_vector_por_escalar(vector, escalar):
    resultado = [escalar * v for v in vector]
    return resultado

def verificar_propiedad_distribucionalidad():
    st.write("### Verificar propiedad A(u + v) = Au + Av")
    matriz = recibir_matriz_local("matriz_distribucionalidad")
    vector_u = recibir_vector_local("vector_u")
    vector_v = recibir_vector_local("vector_v")
    
    if len(matriz[0]) != len(vector_u) or len(vector_u) != len(vector_v):
        st.write("Error: Las dimensiones de la matriz y los vectores no coinciden.")
        return
    
    suma_vectores = [vector_u[i] + vector_v[i] for i in range(len(vector_u))]
    resultado_suma = ejecutar_multiplicacion_matriz_por_vector(matriz, suma_vectores)
    resultado_u = ejecutar_multiplicacion_matriz_por_vector(matriz, vector_u)
    resultado_v = ejecutar_multiplicacion_matriz_por_vector(matriz, vector_v)
    resultado_suma_individual = [resultado_u[i] + resultado_v[i] for i in range(len(resultado_u))]
    
    st.write("Resultado de A(u + v):")
    st.write(resultado_suma)
    st.write("Resultado de Au + Av:")
    st.write(resultado_suma_individual)
    
    if resultado_suma == resultado_suma_individual:
        st.write("La propiedad A(u + v) = Au + Av se verifica.")
    else:
        st.write("La propiedad A(u + v) = Au + Av no se verifica.")

def sumar_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        st.write("Error: Las matrices deben tener las mismas dimensiones.")
        return None
    resultado = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return resultado

def restar_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        st.write("Error: Las matrices deben tener las mismas dimensiones.")
        return None
    resultado = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return resultado

def eliminacion_por_gauss(matriz):
    eliminacion_por_gauss_modulo(matriz)

# Función principal de la calculadora
def main():
    st.title("Calculadora de Álgebra Lineal")
    st.write("Calculadora para realizar operaciones con matrices y vectores. Ideal para estudiantes y profesionales que buscan resolver problemas de álgebra lineal de forma rápida y sencilla.")
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
            matriz = recibir_matriz_local("matriz_gauss")
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
            vector = recibir_vector_local("vector_escalar")
            escalar = st.number_input("Ingrese el escalar:", key="escalar")
            resultado = multiplicacion_vector_por_escalar(vector, escalar)
            st.write("Resultado de la multiplicación de vector por escalar:")
            st.write(resultado)
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
            A = recibir_matriz_local("matriz_suma_A")
            B = recibir_matriz_local("matriz_suma_B")
            resultado = sumar_matrices(A, B)
            st.write("Resultado de la suma de matrices:")
            st.write(resultado)
        elif opcion == "Resta de matrices":
            st.write("### Resta de Matrices")
            A = recibir_matriz_local("matriz_resta_A")
            B = recibir_matriz_local("matriz_resta_B")
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
            matriz = recibir_matriz_local("matriz_escalonada")
            eliminacion_por_gauss(matriz)

if __name__ == "__main__":
    main()
