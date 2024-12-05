import math
import re
import numpy as np
import pandas as pd
import streamlit as st
import sympy as sp
from modulos.eliminacionporgaus import eliminacion_por_gauss as eliminacion_por_gauss_modulo
from modulos.escalonada import forma_escalonada, imprimir_matriz, imprimir_solucion
from modulos.multiplicacion_vectores import multiplicacion_de_vectores
from modulos.multiplicacion_matriz_vector import multiplicacion_matriz_por_vector
from modulos.multiplicacion_vector_escalar import multiplicacion_vector_por_escalar
from modulos.suma_resta_matrices import ingresar_matrices, suma_resta_matrices
from modulos.suma_vectores import suma_vectores
from modulos.verificar_propiedad_distribucionalidad import verificar_propiedad_distribucionalidad
from modulos.recibir_matriz import recibir_matriz, recibir_vector
from modulos.regla_de_cramer import resolver_sistema_cramer
from modulos.determinante import calcular_determinante, pasos_determinante
from modulos.multiplicacion_matrices import multiplicar_matrices
from modulos.inversa import calcular_inversa_matriz, parsear_numero, calcular_determinante, agregar_identidad, hacer_pivote
from modulos.graficos import pantalla_graficos
from modulos.verificar_traspuesta import verificar_propiedades_matrices, parsear_numero, transpuesta, verificar_propiedad_a_procedimiento,verificar_propiedad_b_procedimiento,verificar_propiedad_c_procedimiento,verificar_propiedad_d_procedimiento, suma_matrices, multiplicar_por_escalar,multiplicar_matrices
from modulos.transpuesta_simple import calcular_transpuesta
from modulos.multiplicacion_matriz_escalar import multiplicar_matriz_por_escalar 
from modulos.sistema_ecuaciones import resolver_sistema, graficar_sistema
from modulos.falsa_posicion import preprocesar_funcion, metodo_falsa_posicion
from modulos.metodo_secante import metodo_secante, preprocesar_funcion
from modulos.metodo_biseccion import parse_function, eval_function, bisection_method
from modulos.metodo_newton_raphson import preparar_funcion, newton_raphson, graficar_funcion, calcular_raiz
from modulos.economia_de_flujo import ejercicio_fabricante,ejercicio_gran_compania,ejercicio_joyeria,ejercicio_turista
from modulos.juega import pantalla_juego
import fractions as frac
from fractions import Fraction
import matplotlib.pyplot as plt
import matplotlib
from sympy import sympify, Matrix, SympifyError


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

#working

# Función para ingresar las matrices
def ingresar_matrices():
    st.write("Ingrese las dimensiones de las matrices:")
    filas = st.number_input("Número de filas:", min_value=1, max_value=10, value=3, step=1)
    columnas = st.number_input("Número de columnas:", min_value=1, max_value=10, value=3, step=1)

    st.write("Ingrese los valores de la Matriz A:")
    matriz_a = []
    for i in range(filas):
        fila = []
        cols = st.columns(columnas)
        for j in range(columnas):
            entrada = cols[j].text_input(f"A[{i+1},{j+1}]", value="0", key=f"a_{i}_{j}")
            try:
                fila.append(sympify(entrada))
            except SympifyError:
                st.error(f"El valor ingresado en A[{i+1},{j+1}] no es válido. Por favor, ingrese un número, fracción o expresión válida.")
                return None, None
        matriz_a.append(fila)

    st.write("Ingrese los valores de la Matriz B:")
    matriz_b = []
    for i in range(filas):
        fila = []
        cols = st.columns(columnas)
        for j in range(columnas):
            entrada = cols[j].text_input(f"B[{i+1},{j+1}]", value="0", key=f"b_{i}_{j}")
            try:
                fila.append(sympify(entrada))
            except SympifyError:
                st.error(f"El valor ingresado en B[{i+1},{j+1}] no es válido. Por favor, ingrese un número, fracción o expresión válida.")
                return None, None
        matriz_b.append(fila)

    matriz_a = Matrix(matriz_a)
    matriz_b = Matrix(matriz_b)
    return matriz_a, matriz_b

    st.write("Ingrese los valores de la Matriz B:")
    matriz_b = []
    for i in range(filas):
        fila = []
        cols = st.columns(columnas)
        for j in range(columnas):
            entrada = cols[j].text_input(f"B[{i+1},{j+1}]", value="0", key=f"b_{i}_{j}")
            fila.append(sympify(entrada))
        matriz_b.append(fila)

    matriz_a = Matrix(matriz_a)
    matriz_b = Matrix(matriz_b)
    return matriz_a, matriz_b

# Módulo para suma de matrices
def suma_matrices():
    st.header("Suma de Matrices")
    A, B = ingresar_matrices()  # Ingreso de matrices

    if st.button("Calcular Suma"):
        try:
            suma = A + B
            st.subheader("Resultado de la Suma:")
            st.write(suma)
        except Exception as e:
            st.error(f"Error: {e}")

# Módulo para resta de matrices
def resta_matrices():
    st.header("Resta de Matrices")
    A, B = ingresar_matrices()  # Ingreso de matrices

    if st.button("Calcular Resta"):
        try:
            resta = A - B
            st.subheader("Resultado de la Resta:")
            st.write(resta)
        except Exception as e:
            st.error(f"Error: {e}")


#parsear para fracciones 

def parsear_numero(valor):
    """Convierte un valor a Fraction, float o int según corresponda."""
    try:
        if "/" in valor:
            return Fraction(valor)  # Manejar fracciones
        elif "." in valor:
            return float(valor)    # Manejar decimales
        else:
            return int(valor)      # Manejar enteros
    except ValueError:
        raise ValueError(f"El valor '{valor}' no es válido. Use enteros, decimales o fracciones (ej. 3/4).")

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
            coeficientes = [[parsear_numero(cell) for cell in fila[:-1]] for fila in matriz]
            terminos = [parsear_numero(fila[-1]) for fila in matriz]

            # Llamar a la función del módulo
            resultado = resolver_sistema_cramer(coeficientes, terminos)

            # Mostrar los resultados
            if resultado["soluciones"] is None:
                st.error(resultado["mensaje"])
            else:
                st.subheader("Soluciones del sistema:")
                for i, solucion in enumerate(resultado["soluciones"]):
                    st.write(f"x{i+1} = {str(solucion)}")

            # Mostrar pasos detallados
            with st.expander("Pasos detallados"):
                st.write(f"Determinante principal: {resultado['pasos']['det_principal']}")
                for detalle in resultado["pasos"]["detalles"]:
                    st.write(f"Determinante para {detalle['variable']}: {detalle['det_i']}")
                    st.write("Matriz modificada:")
                    st.table(detalle["matriz_modificada"])
        except ValueError:
            st.error("Por favor, ingrese valores válidos (enteros, decimales o fracciones) en todos los campos.")
        except Exception as e:
            st.error(f"Error inesperado: {e}")

def eliminacion_por_gauss(matriz):
    eliminacion_por_gauss_modulo(matriz)

 #Sistemas de ecuaciones 

def sistema_ecuac():
    # Configuración de la página
    st.title("🔢 Resolución de Sistemas de Ecuaciones Lineales")
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
    """
    Interfaz gráfica para calcular la raíz de una función usando el método de falsa posición.
    """
    st.title("Cálculo de Raíces - Método de Falsa Posición")

    st.header("Ingrese los datos necesarios")
    funcion = st.text_input("Función en términos de x (ejemplo: 3x^2 + 4x - 10):", "3x^2 + 4x - 10")
    x0 = st.number_input("Valor inicial x0:", value=1.0)
    x1 = st.number_input("Valor inicial x1:", value=2.0)
    tolerancia = st.number_input("Tolerancia:", value=0.0001, format="%.8f")
    max_iter = st.number_input("Número máximo de iteraciones:", value=50, step=1)

    if st.button("Calcular"):
        try:
            # Convertir tolerancia de porcentaje a formato decimal
            tolerancia_decimal = tolerancia

            # Llamar a la lógica del método falsa posición
            resultados = metodo_falsa_posicion(funcion, x0, x1, tolerancia_decimal, max_iter)

            # Mostrar los resultados iterativos en una tabla
            st.subheader("Resultados por Iteración")
            tabla_resultados = {
                "Iteración": resultados["Iteración"],
                "x0": resultados["x0"],
                "x1": resultados["x1"],
                "x2": resultados["x2"],
                "f(x0)": resultados["f(x0)"],
                "f(x1)": resultados["f(x1)"],
                "f(x2)": resultados["f(x2)"],
                "Error": resultados["Error"],
            }
            st.table(tabla_resultados)

            # Mostrar la conclusión en una tabla separada
            st.subheader("Conclusión")
            st.write(resultados["Conclusión"])

        except Exception as e:
            st.error(f"Ha ocurrido un error: {e}")




#####

#Método de la Secante

def interfaz_secante():
    """
    Interfaz gráfica para calcular la raíz de una función usando el método del secante.
    """
    st.title("Cálculo de Raíces - Método del Secante")

    st.header("Ingrese los datos necesarios")
    funcion = st.text_input("Función en términos de x (ejemplo: 3x^2 + 4x - 10):", "3x^2 + 4x - 10")
    x0 = st.number_input("Valor inicial x0:", value=1.0)
    x1 = st.number_input("Valor inicial x1:", value=2.0)
    tolerancia = st.number_input("Tolerancia:", value=0.0001, format="%.8f")
    max_iter = st.number_input("Número máximo de iteraciones:", value=50, step=1)

    if st.button("Calcular"):
        try:
            # Convertir tolerancia de porcentaje a formato decimal
            tolerancia_decimal = tolerancia

            # Llamar a la lógica del método secante
            resultados = metodo_secante(funcion, x0, x1, tolerancia_decimal, max_iter)

            # Mostrar los resultados iterativos en una tabla
            st.subheader("Resultados por Iteración")
            tabla_resultados = {
                "Iteración": resultados["Iteración"],
                "x0": resultados["x0"],
                "x1": resultados["x1"],
                "x2": resultados["x2"],
                "Error": resultados["Error"],
                "f(x0)": resultados["f(x0)"],
                "f(x1)": resultados["f(x1)"],
            }
            st.table(tabla_resultados)

            # Mostrar la conclusión en una tabla separada
            st.subheader("Conclusión")
            st.write(resultados["Conclusión"])

        except Exception as e:
            st.error(f"Ha ocurrido un error: {e}")


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

#Método de Newton-Raphson


# Función para convertir y preparar la función matemática
def preparar_funcion(funcion):
    funcion = funcion.replace("^", "**")  # Cambiar ^ por ** para potencias
    funcion = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', funcion)  # Convertir 2x en 2*x
    funcion = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', funcion)  # Convertir x2 en x*2

    # Reemplazar funciones matemáticas en español
    funciones_spanish = {
        'sen': 'math.sin',  # seno
        'cos': 'math.cos',  # coseno
        'tan': 'math.tan',  # tangente
        'cot': '(1/math.tan)',  # cotangente
        'sec': '(1/math.cos)',  # secante
        'csc': '(1/math.sin)',  # cosecante
        'ln': 'math.log',       # logaritmo natural
        'log': 'math.log10',    # logaritmo base 10
        'exp': 'math.exp',      # exponencial
        'sqrt': 'math.sqrt',    # raíz cuadrada
        'pi': 'math.pi',        # constante pi
        'e': 'math.e'           # constante e
    }

    for key, val in funciones_spanish.items():
        funcion = funcion.replace(key, val)

    return funcion

# Declarar Método de Newton-Raphson
def newton_raphson(f, df, xi, tol=1e-4, max_iter=100):
    resultados = []
    for i in range(max_iter):
        fxi = f(xi)
        dfxi = df(xi)
        if dfxi == 0:
            st.warning(f'Iteración {i+1}: Derivada cero. No se puede continuar.')
            return None, resultados
        xi1 = xi - fxi / dfxi
        ea = abs(xi1 - xi)
        resultados.append((i+1, round(xi, 4), round(xi1, 4), round(ea, 4), round(fxi, 4), round(dfxi, 4)))
        if ea < tol:
            return xi1, resultados
        xi = xi1
    st.error("No convergió.")
    return None, resultados

# Graficar la función
def graficar_funcion(f, xi, xf, raiz):
    x = [xi + (xf - xi) * i / 1000 for i in range(1001)]
    y = [f(val) for val in x]
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label='f(x)', color='blue')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(raiz, color='r', linestyle='--', label=f'Raíz aproximada: {raiz:.4f}')
    plt.title('Gráfica de la función')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    st.pyplot(plt)

# Función principal para la interfaz
def interfaz():
    st.title("Calculadora de Raíces: Método de Newton-Raphson")
    st.write("Esta aplicación utiliza el método de Newton-Raphson para encontrar raíces de funciones.")
    
    st.header("Configuración")
    funcion_str = st.text_input("Ingrese la función f(x):", "sen(x) - x/2")
    df_str = st.text_input("Ingrese la derivada f'(x):", "cos(x) - 0.5")
    xi = st.number_input("Estimación inicial (xi):", value=0.5)
    xf = st.number_input("Límite superior para graficar (xf):", value=3.0)
    tol = st.number_input("Tolerancia:", value=0.001, format="%.6f")
    max_iter = st.number_input("Máximo de iteraciones:", value=100, min_value=1)

    # Botón para calcular
    if st.button("Calcular"):
        try:
            f = eval(f"lambda x: {preparar_funcion(funcion_str)}", {"math": math})
            df = eval(f"lambda x: {preparar_funcion(df_str)}", {"math": math})
            raiz, resultados = newton_raphson(f, df, xi, tol, max_iter)
            if raiz is not None:
                st.success(f"Raíz aproximada: {raiz:.10f}")
                st.subheader("Tabla de resultados por iteración")
                st.table({
                    "Iteración": [r[0] for r in resultados],
                    "xi": [r[1] for r in resultados],
                    "xi+1": [r[2] for r in resultados],
                    "Error Aproximado (Ea)": [r[3] for r in resultados],
                    "f(xi)": [r[4] for r in resultados],
                    "f'(xi)": [r[5] for r in resultados]
                })
                graficar_funcion(f, xi, xf, raiz)
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")



#####
##
# Ejercicios de econmía de flujo

# Ejercicio 1: Fabricante
def mostrar_ejercicio_fabricante():
    st.header("Ejercicio del Fabricante 🛠️")
    
    st.subheader("Ingreso de Datos")
    D = st.text_input("Ingrese el vector de demanda (separado por comas):", "")
    P = st.text_input("Ingrese el vector de precios unitarios (separado por comas):", "")
    
    if st.button("Calcular"):
        try:
            D = np.array([float(x) for x in D.split(",")])
            P = np.array([float(x) for x in P.split(",")])
            
            if len(D) != len(P):
                st.error("Los vectores de demanda y precios deben tener la misma longitud.")
                return

            total_ingreso = np.dot(D, P)

            st.subheader("Procedimiento")
            st.write(f"Vector de demanda (D): {D}")
            st.write(f"Vector de precios unitarios (P): {P}")
            st.write(f"Cálculo: Demanda × Precio = {D} × {P} = {total_ingreso}")

            st.subheader("Análisis")
            st.write("El fabricante recibe un total porque satisface toda la demanda de los artículos.")

            st.subheader("Resultado Final")
            st.write(f"Total Ingreso: ${total_ingreso:.2f}")
        except ValueError:
            st.error("Por favor, ingrese los vectores correctamente (separados por comas).")

# Ejercicio 2: Joyería
def mostrar_ejercicio_joyeria():
    st.header("Ejercicio de la Joyería 💎")
    
    st.subheader("Ingreso de Datos")
    ordenes = st.text_input("Ingrese el vector de órdenes (separado por comas):", "")
    tiempos = st.text_input("Ingrese el vector de tiempos de elaboración (separado por comas):", "")
    
    if st.button("Calcular"):
        try:
            ordenes = np.array([float(x) for x in ordenes.split(",")])
            tiempos = np.array([float(x) for x in tiempos.split(",")])
            
            if len(ordenes) != len(tiempos):
                st.error("Los vectores de órdenes y tiempos deben tener la misma longitud.")
                return

            total_horas = np.dot(ordenes, tiempos)

            st.subheader("Procedimiento")
            st.write(f"Vector de órdenes (O): {ordenes}")
            st.write(f"Vector de tiempos de elaboración (T): {tiempos}")
            st.write(f"Cálculo: Órdenes × Tiempos = {ordenes} × {tiempos} = {total_horas}")

            st.subheader("Análisis")
            st.write(f"Se requieren:  {total_horas:} horas de trabajo para satisfacer los pedidos.")

            st.subheader("Resultado Final")
            st.write(f"Total de horas: {total_horas:.2f} horas")
        except ValueError:
            st.error("Por favor, ingrese los vectores correctamente (separados por comas).")

# Ejercicio 3: Turista
def mostrar_ejercicio_turista():
    st.header("Ejercicio del Turista 🗺️")
    
    st.subheader("Ingreso de Datos")
    cantidades = st.text_input("Ingrese el vector de cantidades (separado por comas):", "")
    valores = st.text_input("Ingrese el vector de valores en dólares (separado por comas):", "")
    
    if st.button("Calcular"):
        try:
            cantidades = np.array([float(x) for x in cantidades.split(",")])
            valores = np.array([float(x) for x in valores.split(",")])
            
            if len(cantidades) != len(valores):
                st.error("Los vectores de cantidades y valores deben tener la misma longitud.")
                return

            total_dolares = np.dot(cantidades, valores)

            st.subheader("Procedimiento")
            st.write(f"Vector de cantidades (C): {cantidades}")
            st.write(f"Vector de valores en dólares (V): {valores}")
            st.write(f"Cálculo: Cantidad × Valor en dólares = {cantidades} × {valores} = {total_dolares:.2f}")

            st.subheader("Análisis")
            st.write("El total en dólares del turista se calcula multiplicando las cantidades por sus respectivos valores.")

            st.subheader("Resultado Final")
            st.write(f"Total en dólares: ${total_dolares:.2f}")
        except ValueError:
            st.error("Por favor, ingrese los vectores correctamente (separados por comas).")

# Ejercicio 4: Gran Compañía
def mostrar_ejercicio_gran_compania():
    st.header("Ejercicio de la Gran Compañía 📉")
    
    st.subheader("Ingreso de Datos")
    ventas = st.text_area("Ingrese la matriz de ventas por mes (use ; para separar filas y , para columnas):", "")
    utilidades = st.text_input("Ingrese el vector de utilidades (separado por comas):", "")
    impuestos = st.text_input("Ingrese el vector de impuestos (separado por comas):", "")
    
    if st.button("Calcular"):
        try:
            ventas = np.array([[float(x) for x in row.split(",")] for row in ventas.split(";")])
            utilidades = np.array([float(x) for x in utilidades.split(",")])
            impuestos = np.array([float(x) for x in impuestos.split(",")])
            
            if ventas.shape[1] != len(utilidades) or ventas.shape[1] != len(impuestos):
                st.error("El número de columnas de la matriz de ventas debe coincidir con la longitud de los vectores de utilidades e impuestos.")
                return

            utilidades_totales = ventas @ utilidades
            impuestos_totales = ventas @ impuestos

            st.subheader("Procedimiento")
            st.write(f"Matriz de ventas por mes (V):\n{ventas}")
            st.write(f"Vector de utilidades (U): {utilidades}")
            st.write(f"Vector de impuestos (I): {impuestos}")
            st.write(f"Cálculo de utilidades: Ventas × Utilidades = {utilidades_totales}")
            st.write(f"Cálculo de impuestos: Ventas × Impuestos = {impuestos_totales}")

            st.subheader("Análisis")
            st.write("Se calcularon las utilidades e impuestos para cada mes multiplicando las ventas por utilidades e impuestos unitarios.")

            st.subheader("Resultados Finales")
            meses = ["Enero", "Febrero", "Marzo", "Abril"]
            for i, mes in enumerate(meses[:len(utilidades_totales)]):
                st.write(f"{mes} | Utilidades: {utilidades_totales[i]:.2f} | Impuestos: {impuestos_totales[i]:.2f}")
        except ValueError:
            st.error("Por favor, ingrese los datos correctamente.")

# Función principal
def economia_flujo():
    opcion = st.radio(
        "Seleccione el ejercicio que desea resolver",
        ["Fabricante, Ingreso de producción", "Cuentas de la Joyería", "Tesoro del viajero", "Ventas y beneficios"], 
        index=0
    )

    if opcion == "Fabricante, Ingreso de producción":
        mostrar_ejercicio_fabricante()
    elif opcion == "Cuentas de la Joyería":
        mostrar_ejercicio_joyeria()
    elif opcion == "Tesoro del viajero":
        mostrar_ejercicio_turista()
    elif opcion == "Ventas y beneficios":
        mostrar_ejercicio_gran_compania()
##


# Función principal de la calculadora

def main():
    st.title("🧮 Calculadora de Álgebra Lineal")
    st.write("Calculadora para realizar operaciones con matrices y vectores. Ideal para estudiantes y profesionales que buscan resolver problemas de álgebra lineal de forma rápida y sencilla.")
    st.write("Seleccione la operación que desea realizar:")

    # Menú principal
    menu_principal = st.selectbox(
        "Menú de Categorías",
        [
            "Resolución de Sistemas de Ecuaciones",
            "Operaciones de Vectores",
            "Operaciones con Matrices",
            "Transformaciones de Matrices",
            "Métodos Numéricos",
            "Economía de flujo"
        ]
    )

    # Inicialización de la variable opcion
    opcion = None

    # Resolución de sistemas de ecuaciones
    if menu_principal == "Resolución de Sistemas de Ecuaciones":
        opcion = st.radio(
            "Seleccione una operación:",
            ["Eliminación por Gauss", "Regla de Cramer", "Sistemas de ecuaciones lineales"]
        )
        if opcion == "Eliminación por Gauss":
            st.write("### Eliminación por Gauss")
            matriz = recibir_matriz_local("matriz_gauss")
            eliminacion_por_gauss(matriz)
        elif opcion == "Regla de Cramer":
            cramer_calculadora()
        elif opcion == "Sistemas de ecuaciones lineales":
            st.write("### Sistemas de Ecuaciones Lineales")
            sistema_ecuac()

    # Operaciones con vectores
    elif menu_principal == "Operaciones de Vectores":
        opcion = st.radio(
            "Seleccione una operación:",
            [
                "Multiplicación de vectores",
                "Suma de vectores",
                "Multiplicación de vector por escalar",
                "Multiplicación de matriz por vector",
                "Verificar propiedad A(u + v) = Au + Av"
            ]
        )
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
    

    # Operaciones con matrices
    elif menu_principal == "Operaciones con Matrices":
        opcion = st.radio(
            "Seleccione una operación:",
            [
                "Suma de matrices",
                "Resta de matrices",
                "Multiplicación de matrices",
                "Inversa de una matriz",
                "Multiplicación de matriz por escalar"
            ]
        )
    if opcion == "Suma de matrices":
        st.header("Suma de Matrices")
        A, B = ingresar_matrices()  # Usa la función para obtener las matrices
        if A.shape == B.shape:  # Verifica que las matrices tengan las mismas dimensiones
            if st.button("Calcular Suma"):
                resultado = A + B
                st.subheader("Resultado de la suma de matrices:")
                st.write(resultado)
            else:
                st.error("Las matrices deben tener las mismas dimensiones para poder sumarse.")

    elif opcion == "Resta de matrices":
        st.header("Resta de Matrices")
        A, B = ingresar_matrices()  # Usa la función para obtener las matrices
        if A.shape == B.shape:  # Verifica que las matrices tengan las mismas dimensiones
            if st.button("Calcular Resta"):
                resultado = A - B
                st.subheader("Resultado de la resta de matrices:")
                st.write(resultado)
        else:
            st.error("Las matrices deben tener las mismas dimensiones para poder restarse.")

    elif opcion == "Multiplicación de matrices":
        matrices_multiplicacion()
    elif opcion == "Inversa de una matriz":
        inversa()
    elif opcion == "Multiplicación de matriz por escalar":
        multiplicar_matriz_por_escalar()

    # Métodos numéricos
    elif menu_principal == "Métodos Numéricos":
        metodo_tipo = st.radio(
            "Seleccione una categoría de métodos:",
            ["Métodos Cerrados", "Métodos Abiertos"]
        )

        if metodo_tipo == "Métodos Cerrados":
            opcion = st.radio(
                "Seleccione una operación (Métodos Cerrados):",
                ["Método de Falsa Posición", "Método de Bisección"]
            )
        elif metodo_tipo == "Métodos Abiertos":
            opcion = st.radio(
                "Seleccione una operación (Métodos Abiertos):",
                ["Método de Newton-Raphson", "Método de la Secante"]
            )

        if opcion == "Método de Falsa Posición":
            st.write("### Método de Falsa Posición")
            interfaz_falsa_posicion()
        elif opcion == "Método de Bisección":
            st.write("### Método de Bisección")
            bisection_interface()
        elif opcion == "Método de Newton-Raphson":
            st.write("### Método de Newton-Raphson")
            interfaz()
        elif opcion == "Método de la Secante":
            st.write("### Método de la Secante")
            interfaz_secante()

    # Economía de flujo
    elif menu_principal == "Economía de flujo":
        opcion = "Economía de flujo"
        economia_flujo()

if __name__ == "__main__":
    main()
