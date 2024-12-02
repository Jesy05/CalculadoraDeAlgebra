import math
import re
import streamlit as st
import sympy as sp
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
from modulos.verificar_traspuesta import verificar_propiedades_matrices, parsear_numero, transpuesta, verificar_propiedad_a_procedimiento,verificar_propiedad_b_procedimiento,verificar_propiedad_c_procedimiento,verificar_propiedad_d_procedimiento, suma_matrices, multiplicar_por_escalar,multiplicar_matrices
from modulos.transpuesta_simple import calcular_transpuesta
from modulos.multiplicacion_matriz_escalar import multiplicar_matriz_por_escalar 
from modulos.sistema_ecuaciones import resolver_sistema, graficar_sistema
from modulos.falsa_posicion import preparar_funcion, actualizar_funcion, falsa_posicion
from modulos.metodo_secante import preparar_funcion, metodo_secante
from modulos.metodo_biseccion import parse_function, eval_function, bisection_method
from modulos.juega import pantalla_juego
import fractions as frac
import matplotlib.pyplot as plt
import matplotlib


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
        st.write("Descripción sobre la calculadora:")
        st.write("La página web Calculadora de Álgebra Lineal, ofrece una herramienta interactiva "
        " para resolver una amplia variedad de operaciones"
        " y conceptos relacionados con álgebra lineal."
        " Con una interfaz amigable y funcionalidades dinámicas, esta calculadora "
        "está diseñada tanto para estudiantes como para profesionales, "
       " permitiendo resolver problemas y validar conceptos de manera eficiente."
                "    Autores: Jesy González, Alejandra Morales, Daysi Miranda")

                 
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

    # Funciones multiplicar matriz por escalar


# Función principal
def multiplicar_matriz_por_escalar():
    st.write("### Multiplicación de una Matriz por un Escalar")

    # Configurar el tamaño de la matriz
    st.write("Ingrese las dimensiones de la matriz:")
    filas = st.number_input("Número de filas:", min_value=1, max_value=10, value=3)
    columnas = st.number_input("Número de columnas:", min_value=1, max_value=10, value=3)

    # Inicializar la matriz
    st.write("Ingrese los valores de la matriz:")
    matriz = []
    for i in range(filas):
        fila = []
        cols = st.columns(columnas)  # Dividir cada fila en columnas
        for j in range(columnas):
            # Cada celda tendrá un campo de texto
            placeholder = f"Elemento ({i+1},{j+1})"
            valor = cols[j].text_input(placeholder, value="", key=f"matriz_{i}_{j}")
            # Intentamos convertir el valor ingresado a fracción o asignar 0 si no es válido
            try:
                if valor:
                    valor = str(frac.Fraction(valor))  # Convertir a fracción
                else:
                    valor = "0"  # Si no se ingresa nada, asignamos 0
            except ValueError:
                st.warning(f"El valor ingresado en ({i+1},{j+1}) no es válido. Se tomará 0 como valor.")
                valor = "0"
            fila.append(valor)
        matriz.append(fila)

    # Entrada del escalar
    st.write("Ingrese el escalar para multiplicar la matriz:")
    escalar = st.text_input("Escalar (acepta fracciones y decimales):", value="1")

    # Variables para almacenar los resultados y permitir interacción con los botones
    matriz_resultante = None
    mostrar_proc = False

    # Botón para calcular la matriz resultante
    if st.button('Multiplicar Matriz por Escalar'):
        try:
            # Procesar el escalar
            escalar = frac.Fraction(escalar)

            # Convertir la matriz a valores numéricos
            matriz_numerica = [[frac.Fraction(valor) for valor in fila] for fila in matriz]

            # Mostrar la matriz original
            st.subheader('Matriz Original:')
            mostrar_matriz(matriz_numerica)

            # Calcular la matriz resultante
            matriz_resultante = [
                [elemento * escalar for elemento in fila] for fila in matriz_numerica
            ]

            # Mostrar la matriz resultante
            st.subheader('Matriz Resultante:')
            mostrar_matriz(matriz_resultante)

            # Indicar que el procedimiento puede mostrarse
            st.session_state["matriz_numerica"] = matriz_numerica
            st.session_state["escalar"] = escalar
            st.session_state["matriz_resultante"] = matriz_resultante
            st.session_state["mostrar_proc"] = True

        except ValueError as e:
            st.error(f"Error: {e}. Asegúrese de ingresar valores válidos para la matriz y el escalar.")

    # Botón para mostrar el procedimiento
    if "mostrar_proc" in st.session_state and st.session_state["mostrar_proc"]:
        if st.button('Mostrar Procedimiento'):
            matriz_numerica = st.session_state["matriz_numerica"]
            escalar = st.session_state["escalar"]
            matriz_resultante = st.session_state["matriz_resultante"]

            st.subheader('Procedimiento:')
            mostrar_procedimiento(matriz_numerica, escalar, matriz_resultante)


# Función para mostrar una matriz
def mostrar_matriz(matriz):
    """
    Muestra una matriz en formato tabla en Streamlit.
    """
    st.table([[str(elem) for elem in fila] for fila in matriz])


# Función para mostrar el procedimiento paso a paso
def mostrar_procedimiento(matriz, escalar, matriz_resultante):
    """
    Muestra el procedimiento de la multiplicación paso a paso.
    """
    for i, fila in enumerate(matriz):
        st.write(f"### Fila {i + 1}:")
        pasos = []
        for j, elemento in enumerate(fila):
            pasos.append(f"{elemento} × {escalar} = {matriz_resultante[i][j]}")
        st.write("  \n".join(pasos))  # Mostrar los pasos para cada fila
#  ###    

#WORK IN PROGRESS

def propiedades_transpuesta():
    st.write("### Transposición con Verificación de Propiedades")
    def propiedades_transpuesta():

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
            valor = cols[j].text_input(placeholder, value="", key=f"matriz_{i}_{j}")
            fila.append(valor)
        matriz.append(fila)

    # Botón para verificar propiedades
    if st.button("Verificar Propiedades"):
        try:
            # Procesar la entrada
            matriz = [[parsear_numero(cell) for cell in fila] for fila in matriz]

            # Calcular la transpuesta de la matriz
            matriz_transpuesta = transpuesta(matriz)

            # Verificar las propiedades con detalles
            verificar_a, detalle_a = verificar_propiedad_a(matriz, matriz_transpuesta, detalles=True)
            verificar_b, detalle_b = verificar_propiedad_b(matriz, matriz_transpuesta, detalles=True)
            verificar_c, detalle_c = verificar_propiedad_c(matriz, matriz_transpuesta, detalles=True)
            verificar_d, detalle_d = verificar_propiedad_d(matriz, matriz_transpuesta, detalles=True)

            # Mostrar resultados con procedimientos
            st.write("### Resultados:")
            if verificar_a:
                st.success("(A^T)^T = A cumple.")
            else:
                st.error("(A^T)^T = A no cumple.")
            st.text(detalle_a)

            if verificar_b:
                st.success("(A + B)^T = A^T + B^T cumple.")
            else:
                st.error("(A + B)^T = A^T + B^T no cumple.")
            st.text(detalle_b)

            if verificar_c:
                st.success("(rA)^T = rA^T cumple.")
            else:
                st.error("(rA)^T = rA^T no cumple.")
            st.text(detalle_c)

            if verificar_d:
                st.success("(AB)^T = B^T A^T cumple.")
            else:
                st.error("(AB)^T = B^T A^T no cumple.")
            st.text(detalle_d)

        except ValueError as e:
            st.error(f"Error: {e}")
        except ZeroDivisionError:
            st.error("No se puede dividir por cero durante el cálculo.")

# Funciones auxiliares actualizadas
def parsear_numero(valor):
    try:
        if "/" in valor:
            return frac.Fraction(valor)
        elif "." in valor:
            return float(valor)
        else:
            return int(valor)
    except ValueError:
        raise ValueError(f"El valor '{valor}' no es un número válido. Use enteros, decimales o fracciones (ej. 3/4).")

def transpuesta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def verificar_propiedad_a(A, _, detalles=False):
    A_T_T = transpuesta(transpuesta(A))
    detalle = f"Transpuesta doble:\n{A_T_T}\nOriginal:\n{A}"
    return A == A_T_T, detalle if detalles else (A == A_T_T)

def verificar_propiedad_b(A, A_T, detalles=False):
    try:
        suma_original = suma_matrices(A, A)
        suma_transpuesta = transpuesta(suma_original)
        suma_individual = suma_matrices(A_T, A_T)
        detalle = (
            f"Suma original:\n{suma_original}\n"
            f"Transpuesta de la suma:\n{suma_transpuesta}\n"
            f"Suma de transpuestas:\n{suma_individual}"
        )
        cumple = suma_transpuesta == suma_individual
        return cumple, detalle if detalles else cumple
    except ValueError:
        return False, "Error al sumar matrices."

def verificar_propiedad_c(A, A_T, detalles=False):
    escalar = 2  # Ejemplo con r = 2
    multiplicacion_original = multiplicar_por_escalar(A, escalar)
    transpuesta_escalar = transpuesta(multiplicacion_original)
    multiplicacion_transpuesta = multiplicar_por_escalar(A_T, escalar)
    detalle = (
        f"Multiplicación original:\n{multiplicacion_original}\n"
        f"Transpuesta del resultado:\n{transpuesta_escalar}\n"
        f"Resultado escalado de la transpuesta:\n{multiplicacion_transpuesta}"
    )
    cumple = transpuesta_escalar == multiplicacion_transpuesta
    return cumple, detalle if detalles else cumple

def verificar_propiedad_d(A, A_T, detalles=False):
    try:
        producto_original = multiplicar_matrices(A, A)
        transpuesta_producto = transpuesta(producto_original)
        producto_transpuestas = multiplicar_matrices(A_T, A_T)
        detalle = (
            f"Producto original:\n{producto_original}\n"
            f"Transpuesta del producto:\n{transpuesta_producto}\n"
            f"Producto de transpuestas:\n{producto_transpuestas}"
        )
        cumple = transpuesta_producto == producto_transpuestas
        return cumple, detalle if detalles else cumple
    except ValueError:
        return False, "Error al multiplicar matrices."

def suma_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Las matrices A y B no tienen las mismas dimensiones para la suma.")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiplicar_por_escalar(matriz, escalar):
    return [[escalar * matriz[i][j] for j in range(len(matriz[0]))] for i in range(len(matriz))]

def multiplicar_matrices(A, B):
    if len(A[0]) != len(B):
        raise ValueError("El número de columnas de A debe coincidir con el número de filas de B para multiplicar matrices.")
    filas_A = len(A)
    columnas_A = len(A[0])
    columnas_B = len(B[0])
    producto = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]
    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                producto[i][j] += A[i][k] * B[k][j]
    return producto

    ####
def propiedades_transpuesta():
    st.write("### Transposición con Verificación de Propiedades")

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
            valor = cols[j].text_input(placeholder, value="", key=f"matriz_{i}_{j}")
            fila.append(valor)
        matriz.append(fila)

    # Botón para verificar propiedades
    if st.button("Verificar Propiedades"):
        try:
            # Procesar la entrada
            matriz = [[parsear_numero(cell) for cell in fila] for fila in matriz]

            # Calcular la transpuesta de la matriz
            matriz_transpuesta = transpuesta(matriz)

            # Verificar las propiedades con detalles
            verificar_a, detalle_a = verificar_propiedad_a(matriz, matriz_transpuesta, detalles=True)
            verificar_b, detalle_b = verificar_propiedad_b(matriz, matriz_transpuesta, detalles=True)
            verificar_c, detalle_c = verificar_propiedad_c(matriz, matriz_transpuesta, detalles=True)
            verificar_d, detalle_d = verificar_propiedad_d(matriz, matriz_transpuesta, detalles=True)

            # Mostrar resultados con procedimientos
            st.write("### Resultados:")
            if verificar_a:
                st.success("(A^T)^T = A cumple.")
            else:
                st.error("(A^T)^T = A no cumple.")
            st.text(detalle_a)

            if verificar_b:
                st.success("(A + B)^T = A^T + B^T cumple.")
            else:
                st.error("(A + B)^T = A^T + B^T no cumple.")
            st.text(detalle_b)

            if verificar_c:
                st.success("(rA)^T = rA^T cumple.")
            else:
                st.error("(rA)^T = rA^T no cumple.")
            st.text(detalle_c)

            if verificar_d:
                st.success("(AB)^T = B^T A^T cumple.")
            else:
                st.error("(AB)^T = B^T A^T no cumple.")
            st.text(detalle_d)

        except ValueError as e:
            st.error(f"Error: {e}")
        except ZeroDivisionError:
            st.error("No se puede dividir por cero durante el cálculo.")

# Funciones auxiliares actualizadas
def parsear_numero(valor):
    try:
        if "/" in valor:
            return frac.Fraction(valor)
        elif "." in valor:
            return float(valor)
        else:
            return int(valor)
    except ValueError:
        raise ValueError(f"El valor '{valor}' no es un número válido. Use enteros, decimales o fracciones (ej. 3/4).")

def transpuesta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def verificar_propiedad_a(A, _, detalles=False):
    A_T_T = transpuesta(transpuesta(A))
    detalle = f"Transpuesta doble:\n{A_T_T}\nOriginal:\n{A}"
    return A == A_T_T, detalle if detalles else (A == A_T_T)

def verificar_propiedad_b(A, A_T, detalles=False):
    try:
        suma_original = suma_matrices(A, A)
        suma_transpuesta = transpuesta(suma_original)
        suma_individual = suma_matrices(A_T, A_T)
        detalle = (
            f"Suma original:\n{suma_original}\n"
            f"Transpuesta de la suma:\n{suma_transpuesta}\n"
            f"Suma de transpuestas:\n{suma_individual}"
        )
        cumple = suma_transpuesta == suma_individual
        return cumple, detalle if detalles else cumple
    except ValueError:
        return False, "Error al sumar matrices."

def verificar_propiedad_c(A, A_T, detalles=False):
    escalar = 2  # Ejemplo con r = 2
    multiplicacion_original = multiplicar_por_escalar(A, escalar)
    transpuesta_escalar = transpuesta(multiplicacion_original)
    multiplicacion_transpuesta = multiplicar_por_escalar(A_T, escalar)
    detalle = (
        f"Multiplicación original:\n{multiplicacion_original}\n"
        f"Transpuesta del resultado:\n{transpuesta_escalar}\n"
        f"Resultado escalado de la transpuesta:\n{multiplicacion_transpuesta}"
    )
    cumple = transpuesta_escalar == multiplicacion_transpuesta
    return cumple, detalle if detalles else cumple

def verificar_propiedad_d(A, A_T, detalles=False):
    try:
        producto_original = multiplicar_matrices(A, A)
        transpuesta_producto = transpuesta(producto_original)
        producto_transpuestas = multiplicar_matrices(A_T, A_T)
        detalle = (
            f"Producto original:\n{producto_original}\n"
            f"Transpuesta del producto:\n{transpuesta_producto}\n"
            f"Producto de transpuestas:\n{producto_transpuestas}"
        )
        cumple = transpuesta_producto == producto_transpuestas
        return cumple, detalle if detalles else cumple
    except ValueError:
        return False, "Error al multiplicar matrices."

def suma_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Las matrices A y B no tienen las mismas dimensiones para la suma.")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiplicar_por_escalar(matriz, escalar):
    return [[escalar * matriz[i][j] for j in range(len(matriz[0]))] for i in range(len(matriz))]

def multiplicar_matrices(A, B):
    if len(A[0]) != len(B):
        raise ValueError("El número de columnas de A debe coincidir con el número de filas de B para multiplicar matrices.")
    filas_A = len(A)
    columnas_A = len(A[0])
    columnas_B = len(B[0])
    producto = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]
    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                producto[i][j] += A[i][k] * B[k][j]
    return producto

    ####

# Función para calcular la transpuesta de una matriz
def calcular_transpuesta(matriz):
    # La transpuesta intercambia filas y columnas
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

# Función para mostrar la matriz en un formato organizado
def mostrar_matriz(matriz):
    for fila in matriz:
        st.write(" | ".join([str(elem) for elem in fila]))

# Función principal para calcular la transpuesta de una matriz
def transpuesta_simple():
    st.title('Calculadora de la Transpuesta de una Matriz')

    # Configurar el tamaño de la matriz
    st.write("Ingrese las dimensiones de la matriz cuadrada:")
    dimension = st.number_input(
        "Dimensión de la matriz (n x n):", min_value=2, max_value=10, value=3, step=1
    )

    # Entrada de los valores de la matriz
    st.write("Ingrese los valores de la matriz:")
    matriz = []

    for i in range(dimension):
        fila = []
        cols = st.columns(dimension)  # Crear columnas dinámicas para la fila
        for j in range(dimension):
            placeholder = f"Elemento ({i+1},{j+1})"
            valor = cols[j].text_input(placeholder, key=f"matriz_{i}_{j}")

            # Validar y convertir el valor a número
            try:
                valor = frac.Fraction (valor) if valor else 0  # Convertir a fracción o asignar 0
            except ValueError:
                st.warning(f"El valor ingresado en ({i+1},{j+1}) no es válido. Se usará 0.")
                valor = 0
            fila.append(valor)
        matriz.append(fila)

    # Botón para calcular la transpuesta
    if st.button('Calcular Transpuesta'):
        # Verificar si la matriz está correctamente llena
        if len(matriz) == dimension and all(len(fila) == dimension for fila in matriz):
            # Mostrar la matriz original
            st.subheader('Matriz Original:')
            mostrar_matriz(matriz)

            # Calcular y mostrar la transpuesta
            matriz_transpuesta = calcular_transpuesta(matriz)
            st.subheader('Matriz Transpuesta:')
            mostrar_matriz(matriz_transpuesta)
        else:
            st.error("La matriz no está completamente llena o tiene dimensiones incorrectas.")

            ## 

def determinante_calculadora():
    st.write("### Cálculo de Determinante")
    
    # Configurar la entrada de la matriz
    st.write("Ingrese los valores de la matriz:")
    num_variables = st.slider("Tamaño de la matriz", min_value=2, max_value=10, value=2, step=1)

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

 #Sistemas de ecuaciones 

def sistema_ecuac():
    # Configuración de la página
    st.title("🧮 Resolución de Sistemas de Ecuaciones Lineales")
    st.write("Este programa resuelve sistemas de ecuaciones lineales de la forma:")
    st.latex("ra_1x + b_1y = c_1")
    st.latex("ra_2x + b_2y = c_2")

    # Entrada de datos
    st.subheader("Ingresa los coeficientes del sistema")

    col1, col2 = st.columns(2)

    with col1:
        a1 = st.number_input("a1 (coeficiente de x en la primera ecuación)", value=1.0)
        b1 = st.number_input("b1 (coeficiente de y en la primera ecuación)", value=1.0)
        c1 = st.number_input("c1 (término independiente de la primera ecuación)", value=1.0)

    with col2:
        a2 = st.number_input("a2 (coeficiente de x en la segunda ecuación)", value=1.0)
        b2 = st.number_input("b2 (coeficiente de y en la segunda ecuación)", value=1.0)
        c2 = st.number_input("c2 (término independiente de la segunda ecuación)", value=1.0)

    # Resolver el sistema
    if st.button("Resolver sistema"):
        tipo_solucion, solucion = resolver_sistema(a1, b1, c1, a2, b2, c2)

        st.subheader("Resultado")
        if tipo_solucion == "Única solución":
            st.success(f"El sistema tiene una única solución: x = {solucion[0]:.2f}, y = {solucion[1]:.2f}")
        elif tipo_solucion == "Infinitas soluciones":
            st.info("El sistema tiene infinitas soluciones (las rectas son equivalentes).")
        elif tipo_solucion == "Sin solución":
            st.error("El sistema no tiene solución (las rectas son paralelas).")

    # Botón para mostrar la gráfica
    if st.button("Mostrar gráfica"):
        st.subheader("Gráfica del sistema")
        fig = graficar_sistema(a1, b1, c1, a2, b2, c2)
        st.pyplot(fig)
 ####      

##Método de la Falsa Posición

# Función para convertir y preparar la función matemática
def preparar_funcion(funcion):
    funciones_math = {
        'sen': 'sin',
        'sin': 'sin',
        'cos': 'cos',
        'tan': 'tan',
        'cot': '1/tan',
        'sec': '1/cos',
        'csc': '1/sin',
        'log': 'log10',
        'ln': 'log',
        'exp': 'exp',
        'sqrt': 'sqrt',
        'pi': 'pi',
        'e': 'E'
    }
    try:
        funcion = funcion.replace('^', '**').replace(' ', '')
        funcion = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', funcion)
        funcion = re.sub(r'(\))(?=\d|[a-zA-Z])', r')*', funcion)
        for key, val in funciones_math.items():
            funcion = re.sub(r'\b' + key + r'\b', val, funcion)
        return funcion
    except Exception as e:
        raise ValueError(f"Error al procesar la función: {e}")

# Interfaz en Streamlit
def interfaz_falsa_posicion():
    st.title("Método de Falsa Posición")
    st.markdown(
        """
        Resuelve ecuaciones no lineales usando el **Método de Falsa Posición**.
        Proporcione la función, los valores iniciales (`xi`, `xu`), la tolerancia y el máximo de iteraciones.
        """
    )

    # Entrada de la función matemática
    st.subheader("Ingrese la función")
    if "funcion" not in st.session_state:
        st.session_state["funcion"] = ""

    funcion_str = st.text_input(
        "Función (use 'x' como variable):", 
        value=st.session_state["funcion"], 
        placeholder="Ejemplo: x^3 - 6x^2 + 11x - 6"
    )
    st.session_state["funcion"] = funcion_str

    # Entradas para parámetros del método
    st.subheader("Parámetros del Método")
    col1, col2 = st.columns(2)
    with col1:
        xi = st.number_input("Valor inicial xi:", format="%.4f", value=1.0)
        tolerancia = st.number_input("Tolerancia (%):", format="%.4f", value=0.01)
    with col2:
        xu = st.number_input("Valor inicial xu:", format="%.4f", value=2.0)
        max_iter = st.number_input("Máx. iteraciones:", min_value=1, value=50, step=1)

    # Botón para calcular
    if st.button("Calcular"):
        try:
            # Validación y preparación de la función
            funcion = sp.sympify(preparar_funcion(funcion_str))
            x = sp.symbols('x')

            # Validación inicial
            f_xi = funcion.subs(x, xi)
            f_xu = funcion.subs(x, xu)
            if f_xi * f_xu > 0:
                st.error("La función no cambia de signo en el intervalo dado. Intente con otros valores de `xi` y `xu`.")
                return

            # Inicialización del método
            iteracion = 0
            xr_anterior = None
            resultados = []

            # Iteraciones del método
            while iteracion < max_iter:
                f_xi = funcion.subs(x, xi)
                f_xu = funcion.subs(x, xu)
                xr = xu - (f_xu * (xi - xu)) / (f_xi - f_xu)
                f_xr = funcion.subs(x, xr)
                ea = abs((xr - xr_anterior) / xr) * 100 if xr_anterior is not None else None

                # Guardar resultados
                resultados.append(
                    {
                        "Iteración": iteracion + 1,
                        "xi": round(xi, 4),
                        "xu": round(xu, 4),
                        "xr": round(xr, 4),
                        "Error (%)": round(ea, 4) if ea is not None else "-",
                        "f(xi)": round(f_xi, 4),
                        "f(xu)": round(f_xu, 4),
                        "f(xr)": round(f_xr, 4),
                    }
                )

                # Verificar convergencia
                if ea is not None and ea < tolerancia:
                    break

                # Actualizar intervalos
                if f_xi * f_xr < 0:
                    xu = xr
                else:
                    xi = xr

                xr_anterior = xr
                iteracion += 1

            # Mostrar resultados en tabla
            st.subheader("Resultados por Iteración")
            st.dataframe(resultados)

            # Resumen final
            st.success(f"Raíz aproximada: {xr:.6f}")
            st.info(f"Error aproximado: {ea:.6f}%")
            st.info(f"Método converge en {iteracion + 1} iteraciones.")

        except Exception as e:
            st.error(f"Ocurrió un error: {e}")

#####

#Método de la Secante

# Función para convertir y preparar la función matemática
def preparar_funcion(funcion):
    funciones_math = {
        'sen': 'sin',
        'sin': 'sin',
        'cos': 'cos',
        'tan': 'tan',
        'cot': '1/tan',
        'sec': '1/cos',
        'csc': '1/sin',
        'log': 'log10',
        'ln': 'log',
        'exp': 'exp',
        'sqrt': 'sqrt',
        'pi': 'pi',
        'e': 'E'
    }
    try:
        funcion = funcion.replace('^', '**').replace(' ', '')
        funcion = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', funcion)
        funcion = re.sub(r'(\))(?=\d|[a-zA-Z])', r')*', funcion)
        for key, val in funciones_math.items():
            funcion = re.sub(r'\b' + key + r'\b', val, funcion)
        return funcion
    except Exception as e:
        raise ValueError(f"Error al procesar la función: {e}")

# Método de la Secante
def metodo_secante(funcion, x0, x1, tolerancia, max_iter):
    resultados = []
    f = sp.sympify(funcion)
    x0, x1 = float(x0), float(x1)
    ea = None  # Inicializamos el error aproximado

    for i in range(max_iter):
        y0 = f.subs('x', x0)
        y1 = f.subs('x', x1)

        if y1 - y0 == 0:
            raise ZeroDivisionError("La división por cero ocurrió en el método de la secante.")

        x2 = x1 - y1 * (x1 - x0) / (y1 - y0)
        ea = abs((x2 - x1) / x2) * 100 if i > 0 else None
        resultados.append([i + 1, x0, x1, x2, ea, y0, y1])

        # Detener el método si el error aproximado es menor que la tolerancia
        if ea is not None and ea < tolerancia:
            break

        x0, x1 = x1, x2

    # Conclusión final
    resultado_final = f"La raíz aproximada es {x2:.6f}, el error aproximado es {ea:.6f}%, el método converge a {i + 1} iteraciones."
    return resultados, resultado_final

# Interfaz de Streamlit
def interfaz_secante():
    st.title("Método de la Secante")
    st.markdown("Resuelve ecuaciones no lineales usando el **Método de la Secante**.")

    # Entrada de la función
    st.subheader("Función")
    funcion = st.text_input("Ingrese la función f(x):", value="x^3 - 6*x^2 + 11*x - 6", placeholder="Ejemplo: x^3 - 6x^2 + 11x - 6")

    # Opciones para intervalos
    usar_intervalos = st.checkbox("¿Usar valores iniciales personalizados?", value=True)

    # Entradas para los intervalos
    st.subheader("Parámetros del Método")
    col1, col2 = st.columns(2)
    with col1:
        x0 = st.text_input("Valor inicial x0:", value="1" if usar_intervalos else "")
    with col2:
        x1 = st.text_input("Valor inicial x1:", value="2" if usar_intervalos else "")

    tolerancia = st.number_input("Tolerancia:", min_value=0.0, value=0.001, step=0.0001, format="%.6f")
    max_iter = st.number_input("Máximo de iteraciones:", min_value=1, value=50, step=1)

    # Botón para calcular
    if st.button("Calcular"):
        try:
            # Validar y preparar la función
            funcion_preparada = preparar_funcion(funcion)

            # Validar intervalos
            if usar_intervalos and (not x0 or not x1):
                st.error("Por favor, complete ambos intervalos (x0 y x1).")
                return

            # Usar valores predeterminados si los intervalos no se usan
            x0 = float(x0) if x0 else 1.0
            x1 = float(x1) if x1 else 2.0

            # Llamar al método de la Secante
            resultados, resumen = metodo_secante(funcion_preparada, x0, x1, tolerancia, max_iter)

            # Mostrar el resumen
            st.success(resumen)

            # Mostrar la tabla de resultados
            st.subheader("Resultados por Iteración")
            st.dataframe(
                {
                    "Iteración": [r[0] for r in resultados],
                    "x0": [r[1] for r in resultados],
                    "x1": [r[2] for r in resultados],
                    "x2": [r[3] for r in resultados],
                    "Error (%)": [r[4] for r in resultados],
                    "f(x0)": [r[5] for r in resultados],
                    "f(x1)": [r[6] for r in resultados],
                }
            )
        except Exception as e:
            st.error(f"Se produjo un error: {e}")

#####
#Método de biseccion


# Función para procesar la expresión matemática
def parse_function(func):
    """Prepara la función ingresada para ser evaluada."""
    func = func.replace("^", "**")  # Reemplaza el operador de potencia
    func = func.replace(" ", "")   # Elimina espacios
    func = func.replace("sen", "math.sin") \
               .replace("cos", "math.cos") \
               .replace("tan", "math.tan") \
               .replace("log", "math.log") \
               .replace("exp", "math.exp") \
               .replace("e", str(math.exp(1)))  # Sustituye e por su valor numérico
    func = ''.join([f'*{char}' if i > 0 and char.isalpha() and func[i-1].isdigit() else char 
                    for i, char in enumerate(func)])
    return func


# Función para evaluar
def eval_function(func, x):
    """Evalúa la función en x usando eval. Asume que func está correctamente parseada."""
    return eval(func)


# Lógica del método de bisección
def bisection_method(func, a, b, tol, max_iter=100):
    results = []  # Almacena resultados de las iteraciones
    func = parse_function(func)
    fa = eval_function(func, a)
    fb = eval_function(func, b)

    if fa * fb > 0:
        return None, "El intervalo no contiene una raíz (f(a) * f(b) > 0)."

    xr_prev = a
    for i in range(max_iter):
        xr = (a + b) / 2
        fc = eval_function(func, xr)
        ea = abs(xr - xr_prev) if i > 0 else None

        results.append({
            "Iteración": i + 1,
            "a": a,
            "f(a)": fa,
            "b": b,
            "f(b)": fb,
            "x_r": xr,
            "f(x_r)": fc,
            "Error Absoluto": ea
        })

        if abs(fc) < tol or (ea is not None and ea < tol):
            return results, f"Raíz aproximada: {xr:.6f}, iteraciones: {i + 1}, error: {ea:.6f}" if ea else f"Raíz aproximada: {xr:.6f}, iteraciones: {i + 1}"

        if fa * fc < 0:
            b = xr
            fb = fc
        else:
            a = xr
            fa = fc

        xr_prev = xr

    return results, "El método no encontró una raíz en el número máximo de iteraciones."


# Interfaz con Streamlit
def bisection_interface():
    st.title("Método de Bisección para Encontrar Raíces")

    # Entrada de datos directamente en la interfaz principal
    st.header("Ingrese los parámetros")
    func = st.text_input("Función (en términos de x):", "x^3 - x - 2")
    a = st.number_input("Intervalo inferior (a):", value=1.0)
    b = st.number_input("Intervalo superior (b):", value=2.0)
    tol = st.number_input("Tolerancia:", value=0.001, format="%.6f")
    max_iter = st.number_input("Máximo de iteraciones:", value=100, step=1, min_value=1)
    calcular = st.button("Calcular")

    if calcular:
        try:
            results, summary = bisection_method(func, a, b, tol, max_iter)

            if results is None:
                st.error(summary)
            else:
                st.success(summary)

                # Mostrar resultados en una tabla
                st.subheader("Resultados por Iteración")
                st.table(results)

        except Exception as e:
            st.error(f"Error: {str(e)}")
##

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
        opcion = st.radio("Seleccione una operación:", ["Eliminación por Gauss", "Regla de Cramer", "Sistemas de ecuaciones lineales"])
        if opcion == "Eliminación por Gauss":
            st.write("### Eliminación por Gauss ")
            matriz = recibir_matriz_local("matriz_gauss")
            eliminacion_por_gauss(matriz)
        elif opcion == "Regla de Cramer":
            cramer_calculadora()

        elif opcion == "Sistemas de ecuaciones lineales":
            st.write("###  ")
            sistema_ecuac()


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
            "Inversa de una matriz",
            "Multiplicación de matriz por escalar"
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
        elif opcion == "Multiplicación de matriz por escalar":
            st.write("###   ")
    
            multiplicar_matriz_por_escalar()
            

    
                

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


    if  menu_principal == "Métodos Numéricos":
    # Primero, aseguramos que se selecciona un tipo de método
     metodo_tipo = st.radio(
        "Seleccione una categoría de métodos:",
        ["Métodos Cerrados", "Métodos Abiertos"]
    )

    # Dependiendo de la selección de 'metodo_tipo', se muestran las opciones correspondientes
     if metodo_tipo == "Métodos Cerrados":
        opcion = st.radio(
            "Seleccione una operación (Métodos Cerrados):",
            [
                "Método de Falsa Posición",
                "Método de Bisección",
            ]
        )
    
     elif metodo_tipo == "Métodos Abiertos":
        opcion = st.radio(
            "Seleccione una operación (Métodos Abiertos):",
            [
                "Método de Newton-Raphson",
                "Método de la Secante",
            ]
        )
    
    # Dependiendo de la opción seleccionada, mostramos la descripción
    if opcion == "Método de Falsa Posición":
        st.write("### Método de Falsa Posición")
        interfaz_falsa_posicion()
    
    elif opcion == "Método de la Secante":
        st.write("### Método de la Secante")
        interfaz_secante()

    elif opcion == "Método de Newton-Raphson":
        st.write("### Método de Newton-Raphson")
        st.write("Esta funcionalidad está en desarrollo.")
    
    elif opcion == "Método de Bisección":
        st.write("### Método de Bisección")
        bisection_interface()
    
         
          

if __name__ == "__main__":
    main()
