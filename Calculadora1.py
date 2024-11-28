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
from modulos.determinante import calcular_determinante, pasos_determinante
from modulos.multiplicacion_matrices import multiplicar_matrices
from modulos.inversa import calcular_inversa_matriz, parsear_numero, calcular_determinante, agregar_identidad, hacer_pivote
from modulos.graficos import pantalla_graficos
from modulos.juega import pantalla_juego
import fractions as frac
import matplotlib.pyplot as plt

# Inicializar las claves en st.session_state si no existen
if 'pagina_inicial' not in st.session_state:
    st.session_state.pagina_inicial = True
if 'juego_activo' not in st.session_state:
    st.session_state.juego_activo = False
if 'juego_activo' not in st.session_state:
    st.session_state.pantalladegraficos = False
if 'is_running' not in st.session_state:
    st.session_state.is_running = False
if 'current_question' not in st.session_state:
    st.session_state.current_question = None
if 'current_options' not in st.session_state:
    st.session_state.current_options = None
if 'current_answer' not in st.session_state:
    st.session_state.current_answer = None

# Función para cambiar a la calculadora
def cambiar_a_calculadora():
    st.session_state.pagina_inicial = True
    st.session_state.juego_activo = False
    st.session_state.pantalladegraficos = False 

# Función para manejar el juego
def iniciar_juego():
    st.session_state.pagina_inicial = False
    st.session_state.pantalladegraficos = False 
    st.session_state.juego_activo = True


# Función para manejar la pantalla de gráficos
def activar_pantalla_graficos():
    st.session_state.pagina_inicial = False
    st.session_state.juego_activo = False
    st.session_state.pantalladegraficos = True

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
        st.write("La página web Calculadora de Álgebra Lineal ofrece una herramienta interactiva"
        "ofrece una herramienta interactiva para resolver una amplia variedad de operaciones"
        "y conceptos relacionados con álgebra lineal."
        "Con una interfaz amigable y funcionalidades dinámicas, esta calculadora "
        "está diseñada tanto para estudiantes como para profesionales, "
       " permitiendo resolver problemas y validar conceptos de manera eficiente"
                "    Autores: Jesy Gonzales, Alejandra Morales, Daysi Miranda")

                 
    if st.button("Notas de Uso", key="notas"):
        st.session_state.show_notas = not st.session_state.get('show_notas', False)
    if st.session_state.get('show_notas', False):
        st.write("### Notas de Uso")
        st.write("Notas sobre cómo usar la calculadora.")
        st.write("•	Navegación: Selecciona la operación que necesitas desde el menú principal y sigue las instrucciones en pantalla.•	Datos de Entrada: Ingresa correctamente las matrices, vectores o ecuaciones según el formato indicado.•	Interpretación de Resultados: Los resultados incluyen procedimientos en algunos casos para una mejor comprensión.")

    if st.button("Ayuda", key="ayuda"):
        st.session_state.show_ayuda = not st.session_state.get('show_ayuda', False)
    if st.session_state.get('show_ayuda', False):
        st.write("### Ayuda")
        st.write("Para más información sobre la calculadora contactar con amoralesl@uamv.edu.ni , dmirandao@uamv.edu.ni , jgonzalez@uamv.edu.ni.")    

    if st.button("Juega", key="juega"):
        iniciar_juego()

    if st.button("Gráficos", key="graficos"):
        activar_pantalla_graficos()   
        

# Contenido principal de la calculadora
if st.session_state.pagina_inicial and not st.session_state.juego_activo:
    st.title(" ")

# Contenido del juego
elif st.session_state.juego_activo:
    pantalla_juego()
    for _ in range(100):
        st.write("")  # Añadir espacio para separar visualmente el contenido

# Contenido del juego
elif st.session_state.pantalladegraficos:
    pantalla_graficos()
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
    
    # Configurar las dimensiones de las matrices
    st.write("Ingrese las dimensiones de las matrices:")
    col1, col2 = st.columns(2)
    filas_A = col1.number_input("Filas de la matriz A", min_value=1, max_value=10, value=2)
    columnas_A = col2.number_input("Columnas de la matriz A", min_value=1, max_value=10, value=2)
    
    col3, col4 = st.columns(2)
    filas_B = col3.number_input("Filas de la matriz B", min_value=1, max_value=10, value=2)
    columnas_B = col4.number_input("Columnas de la matriz B", min_value=1, max_value=10, value=2)
    
    # Validar la compatibilidad de dimensiones para la multiplicación
    if columnas_A != filas_B:
        st.warning("El número de columnas de la matriz A debe ser igual al número de filas de la matriz B.")
        return

    # Entradas para la matriz A
    st.write("Ingrese los valores de la matriz A:")
    matriz_A = []
    for i in range(filas_A):
        fila = []
        cols = st.columns(columnas_A)
        for j in range(columnas_A):
            placeholder = f"A({i+1},{j+1})"
            valor = cols[j].text_input(placeholder, value="", key=f"A_{i}_{j}")
            fila.append(valor)
        matriz_A.append(fila)

    # Entradas para la matriz B
    st.write("Ingrese los valores de la matriz B:")
    matriz_B = []
    for i in range(filas_B):
        fila = []
        cols = st.columns(columnas_B)
        for j in range(columnas_B):
            placeholder = f"B({i+1},{j+1})"
            valor = cols[j].text_input(placeholder, value="", key=f"B_{i}_{j}")
            fila.append(valor)
        matriz_B.append(fila)

    # Botón para calcular la multiplicación
    if st.button("Multiplicar matrices"):
        try:
            # Procesar la entrada
            matriz_A = [[float(cell) for cell in fila] for fila in matriz_A]
            matriz_B = [[float(cell) for cell in fila] for fila in matriz_B]

            # Llamar a la función del módulo para multiplicar
            resultado = multiplicar_matrices(matriz_A, matriz_B)

            # Mostrar los resultados
            st.subheader("Resultado de la multiplicación:")
            st.table(resultado)

        except ValueError:
            st.error("Por favor, ingrese valores numéricos válidos en todos los campos.")

# Función para multiplicar matrices (puedes colocarla en otro archivo y llamarla aquí)
def multiplicar_matrices(A, B):
    filas_A, columnas_A = len(A), len(A[0])
    filas_B, columnas_B = len(B), len(B[0])
    
    # Crear la matriz de resultado con ceros
    resultado = [[0] * columnas_B for _ in range(filas_A)]
    
    # Realizar la multiplicación
    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                resultado[i][j] += A[i][k] * B[k][j]
    
    return resultado


def ejecutar_multiplicacion_matriz_por_vector(matriz, vector) -> list[int]:
    resultado = [sum(matriz[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matriz))]
    return resultado

#WORK IN PROGRESS

def inversa():
    st.write("### Inversa de una Matriz")
    st.write("### Cálculo de la Matriz Inversa")

    # Configurar el tamaño de la matriz
    st.write("Ingrese las dimensiones de la matriz cuadrada:")
    dimension = st.number_input(
        "Dimensión de la matriz (n x n):", min_value=2, max_value=10, value=2
    )

    # Entradas para la matriz
    st.write("Ingrese los valores de la matriz:")
    matriz = []
    for i in range(dimension):
        fila = []
        cols = st.columns(dimension)
        for j in range(dimension):
            placeholder = f"({i+1},{j+1})"
            valor = cols[j].text_input(placeholder, value="", key=f"inversa_{i}_{j}")
            fila.append(valor)
        matriz.append(fila)

    # Botón para calcular la inversa
    if st.button("Calcular Inversa"):
        try:
            # Procesar la entrada
            matriz = [[parsear_numero(cell) for cell in fila] for fila in matriz]
            det = calcular_determinante(matriz)
            
            if det == 0:
                st.error("La matriz no es invertible (determinante = 0).")
            else:
                st.success(f"Determinante: {det}")
                # Crear matriz aumentada (A | I)
                matriz_aumentada = agregar_identidad(matriz)

                # Realizar las operaciones elementales para obtener la inversa
                for i in range(dimension):
                    hacer_pivote(matriz_aumentada, i, i)

                # Extraer la parte derecha de la matriz aumentada como la inversa
                inversa = [fila[dimension:] for fila in matriz_aumentada]
                
                # Mostrar la matriz inversa
                st.subheader("Matriz Inversa (A^-1):")
                st.table([[str(elem) for elem in fila] for fila in inversa])

        except ValueError as e:
            st.error(f"Error: {e}")
        except ZeroDivisionError:
            st.error("No se puede dividir por cero durante el cálculo.")

#WORK IN PROGRESS

def propiedades_transpuesta():
    st.write("### Transposición con Verificación de Propiedades")
    st.write("Esta funcionalidad está en desarrollo.")

def transpuesta_simple():
    st.write("### Transposición Simple")
    st.write("Esta funcionalidad está en desarrollo.")

def determinante_calculadora():
    st.write("### Cálculo de Determinante")
    
    # Configurar la entrada de la matriz
    st.write("Ingrese los valores de la matriz:")
    num_variables = st.selectbox("Tamaño de la matriz", [2, 3, 4], index=0)

    # Generar campos de entrada para la matriz
    matriz = []
    for i in range(num_variables):
        fila = []
        cols = st.columns(num_variables)
        for j in range(num_variables):
            placeholder = f"({i+1},{j+1})"
            valor = cols[j].text_input(placeholder, value="", key=f"det_cell_{i}_{j}")
            fila.append(valor)
        matriz.append(fila)

    # Botón para calcular determinante
    if st.button("Calcular determinante"):
        try:
            # Procesar la entrada
            matriz_numerica = [[int(cell) for cell in fila] for fila in matriz]

            # Llamar a la función del módulo
            determinante = calcular_determinante(matriz_numerica)

            # Mostrar el resultado
            st.success(f"El determinante de la matriz es: {determinante}")

            # Mostrar pasos detallados (solo para matrices 3x3 o mayores)
            if num_variables >= 2:
                with st.expander("Pasos detallados"):
                    pasos = pasos_determinante(matriz_numerica)
                    st.text_area("Pasos del cálculo:", pasos, height=200)
        except ValueError:
            st.error("Por favor, ingrese valores numéricos válidos en todos los campos.")
        except Exception as e:
            st.error(f"Error: {e}")


def cramer_calculadora():
    st.write("### Regla de Cramer")
    
    # Configurar la entrada de la matriz
    st.write("Ingrese los coeficientes de la matriz y el vector aumentado:")
    num_variables = st.selectbox("Número de variables", [2, 3, 4], index=0)
    
    # Generar campos de entrada para la matriz y el vector
    matriz = []
    for i in range(num_variables):
        fila = []
        cols = st.columns(num_variables + 1)
        for j in range(num_variables + 1):
            placeholder = f"({i+1},{j+1})" if j < num_variables else f"(aumentada {i+1})"
            valor = cols[j].text_input(placeholder, value="", key=f"cramer_cell_{i}_{j}")
            fila.append(valor)
        matriz.append(fila)

    # Botón para resolver
    if st.button("Resolver sistema"):
        try:
            # Procesar la entrada
            coeficientes = [[int(cell) for cell in fila[:-1]] for fila in matriz]
            terminos = [int(fila[-1]) for fila in matriz]

            # Llamar a la función del módulo
            resultado = resolver_sistema(coeficientes, terminos)

            # Mostrar los resultados
            if resultado["soluciones"] is None:
                st.error(resultado["mensaje"])
            else:
                st.subheader("Soluciones del sistema:")
                for i, solucion in enumerate(resultado["soluciones"]):
                    st.write(f"x{i+1} = {solucion}")

            # Mostrar pasos detallados
            with st.expander("Pasos detallados"):
                st.write(f"Determinante principal: {resultado['pasos']['det_principal']}")
                for detalle in resultado["pasos"]["detalles"]:
                    st.write(f"Determinante para {detalle['variable']}: {detalle['det_i']}")
                    st.write("Matriz modificada:")
                    st.table(detalle["matriz_modificada"])
        except ValueError:
            st.error("Por favor, ingrese valores numéricos válidos en todos los campos.")

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

def cramer_regla(matriz, vector):
    import numpy as np
    det_matriz = np.linalg.det(matriz)
    if det_matriz == 0:
        st.write("Error: La matriz no tiene inversa, por lo tanto, no se puede aplicar la regla de Cramer.")
        return None

    soluciones = []
    for i in range(len(vector)):
        matriz_modificada = np.copy(matriz)
        matriz_modificada[:, i] = vector
        det_modificada = np.linalg.det(matriz_modificada)
        soluciones.append(det_modificada / det_matriz)

    return soluciones

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
        "Transformaciones de Matrices",
        "Métodos Numéricos"
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
            inversa()

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
            determinante_calculadora()
        elif opcion == "Matriz en forma escalonada":
            st.write("### Matriz en forma escalonada")
            matriz = recibir_matriz_local("matriz_escalonada")
            eliminacion_por_gauss(matriz)

    if menu_principal ==  "Métodos Numéricos":
       opcion = st.radio(
        "Seleccione una operación (Métodos cerrados):",
        
        [
            "Método de Falsa Posición",
            "Método de Bisecciónde",
        ]
    )
    if menu_principal ==  "Métodos Numéricos":
       opcion = st.radio(
        "Seleccione una operación (Métodos abiertos):",
        [
            "Método de Newton-Raphson",
            "Método la Secante",
        ]
    )   
    
    if opcion == "Método de Falsa Posición":
        st.write("### Método de Falsa Posición")
        st.write("Esta funcionalidad está en desarrollo.")
    
    elif opcion == "Método de la Secante":
        st.write("### Método de la Secante")
        st.write("Esta funcionalidad está en desarrollo.")
    
    elif opcion == "Método de Newton-Raphson":
        st.write("### Método de Newton-Raphson")
        st.write("Esta funcionalidad está en desarrollo.")
    
    elif opcion == "Método de Bisección":
        st.write("### Método de Bisección")
        st.write("Esta funcionalidad está en desarrollo.")
    
         
          

if __name__ == "__main__":
    main()
