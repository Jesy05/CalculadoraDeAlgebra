import streamlit as st
from fractions import Fraction

def verificar_propiedades_matrices():
    st.write("### Verificación de Propiedades de Matrices")

    # Configurar el tamaño de la matriz
    n = st.selectbox("Tamaño de la matriz (n x n):", [2, 3, 4], index=0)

    # Entradas para la matriz
    st.write(f"Ingrese los valores de la matriz {n}x{n} (puede usar enteros, decimales o fracciones como `3/4`):")
    matriz = []
    for i in range(n):
        fila = []
        cols = st.columns(n)
        for j in range(n):
            placeholder = f"({i+1},{j+1})"
            valor = cols[j].text_input(placeholder, value="", key=f"matriz_{i}_{j}")
            fila.append(valor)
        matriz.append(fila)

    # Botón para verificar propiedades
    if st.button("Verificar Propiedades"):
        try:
            # Procesar la entrada
            matriz = [[parsear_numero(cell) for cell in fila] for fila in matriz]

            # Transpuesta de la matriz
            matriz_transpuesta = transpuesta(matriz)

            # Mostrar matriz original y su transpuesta
            st.write("#### Matriz Original")
            st.write(matriz)
            st.write("#### Matriz Transpuesta")
            st.write(matriz_transpuesta)

            # Verificar y mostrar procedimientos
            st.write("### Procedimientos y Resultados:")
            verificar_propiedad_a_procedimiento(matriz)
            verificar_propiedad_b_procedimiento(matriz, matriz_transpuesta)
            verificar_propiedad_c_procedimiento(matriz, matriz_transpuesta)
            verificar_propiedad_d_procedimiento(matriz, matriz_transpuesta)

        except ValueError as e:
            st.error(f"Error: {e}")
        except ZeroDivisionError:
            st.error("No se puede dividir por cero durante el cálculo.")

# Funciones auxiliares para el cálculo de propiedades de matrices

def parsear_numero(valor):
    """
    Convierte una cadena en un número: entero, decimal o fracción.
    """
    try:
        if "/" in valor:
            return Fraction(valor)
        elif "." in valor:
            return float(valor)
        else:
            return int(valor)
    except ValueError:
        raise ValueError(f"El valor '{valor}' no es un número válido. Use enteros, decimales o fracciones (ej. 3/4).")

def transpuesta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def verificar_propiedad_a_procedimiento(A):
    """
    Procedimiento para verificar que (A^T)^T = A.
    """
    st.write("#### Propiedad 1: (A^T)^T = A")
    A_T = transpuesta(A)
    A_T_T = transpuesta(A_T)
    st.write("1. Transpuesta de la matriz (A^T):")
    st.write(A_T)
    st.write("2. Transpuesta de la transpuesta ((A^T)^T):")
    st.write(A_T_T)
    if A == A_T_T:
        st.success("La propiedad se cumple: (A^T)^T = A")
    else:
        st.error("La propiedad no se cumple: (A^T)^T ≠ A")

def verificar_propiedad_b_procedimiento(A, A_T):
    st.write("#### Propiedad 2: (A + B)^T = A^T + B^T")
    B = A  # Para simplificar, usamos B igual a A
    A_plus_B = suma_matrices(A, B)
    A_plus_B_T = transpuesta(A_plus_B)
    A_T_plus_B_T = suma_matrices(A_T, transpuesta(B))
    st.write("1. Suma de matrices (A + B):")
    st.write(A_plus_B)
    st.write("2. Transpuesta de (A + B):")
    st.write(A_plus_B_T)
    st.write("3. Suma de transpuestas (A^T + B^T):")
    st.write(A_T_plus_B_T)
    if A_plus_B_T == A_T_plus_B_T:
        st.success("La propiedad se cumple: (A + B)^T = A^T + B^T")
    else:
        st.error("La propiedad no se cumple: (A + B)^T ≠ A^T + B^T")

def verificar_propiedad_c_procedimiento(A, A_T):
    st.write("#### Propiedad 3: (rA)^T = rA^T")
    r = 2  # Escalar
    rA = multiplicar_por_escalar(A, r)
    rA_T = transpuesta(rA)
    rA_T_directo = multiplicar_por_escalar(A_T, r)
    st.write(f"1. Matriz escalada (rA) con r = {r}:")
    st.write(rA)
    st.write("2. Transpuesta de (rA):")
    st.write(rA_T)
    st.write(f"3. Escalar aplicado a la transpuesta (rA^T) con r = {r}:")
    st.write(rA_T_directo)
    if rA_T == rA_T_directo:
        st.success("La propiedad se cumple: (rA)^T = rA^T")
    else:
        st.error("La propiedad no se cumple: (rA)^T ≠ rA^T")

def verificar_propiedad_d_procedimiento(A, A_T):
    st.write("#### Propiedad 4: (AB)^T = B^T A^T")
    B = A  # Para simplificar, usamos B igual a A
    AB = multiplicar_matrices(A, B)
    AB_T = transpuesta(AB)
    B_T_A_T = multiplicar_matrices(transpuesta(B), A_T)
    st.write("1. Producto de matrices (AB):")
    st.write(AB)
    st.write("2. Transpuesta del producto ((AB)^T):")
    st.write(AB_T)
    st.write("3. Producto de las transpuestas (B^T A^T):")
    st.write(B_T_A_T)
    if AB_T == B_T_A_T:
        st.success("La propiedad se cumple: (AB)^T = B^T A^T")
    else:
        st.error("La propiedad no se cumple: (AB)^T ≠ B^T A^T")

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
    columnas_B = len(B[0])
    producto = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]
    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(len(B)):
                producto[i][j] += A[i][k] * B[k][j]
    return producto
