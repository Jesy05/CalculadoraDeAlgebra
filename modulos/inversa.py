import streamlit as st
from fractions import Fraction

def calcular_inversa_matriz():
    st.write("### Cálculo de la Matriz Inversa")
    
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
                for i in range(n):
                    hacer_pivote(matriz_aumentada, i, i)

                # Extraer la parte derecha de la matriz aumentada como la inversa
                inversa = [fila[n:] for fila in matriz_aumentada]
                
                # Mostrar la matriz inversa
                st.subheader("Matriz Inversa (A^-1):")
                st.table([[str(elem) for elem in fila] for fila in inversa])

        except ValueError as e:
            st.error(f"Error: {e}")
        except ZeroDivisionError:
            st.error("No se puede dividir por cero durante el cálculo.")

# Funciones auxiliares para el cálculo

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

def calcular_determinante(matriz):
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    elif len(matriz) == 3:
        a, b, c = matriz[0]
        d, e, f = matriz[1]
        g, h, i = matriz[2]
        return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    elif len(matriz) == 4:
        det = 0
        for c in range(4):
            minor = [[matriz[i][j] for j in range(4) if j != c] for i in range(1, 4)]
            det += ((-1) ** c) * matriz[0][c] * calcular_determinante(minor)
        return det
    else:
        return None

def agregar_identidad(matriz):
    n = len(matriz)
    identidad = [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]
    return [fila_m + fila_i for fila_m, fila_i in zip(matriz, identidad)]

def hacer_pivote(matriz, fila_pivote, col_pivote):
    n = len(matriz)
    pivote = matriz[fila_pivote][col_pivote]
    if pivote == 0:
        for i in range(fila_pivote + 1, n):
            if matriz[i][col_pivote] != 0:
                matriz[fila_pivote], matriz[i] = matriz[i], matriz[fila_pivote]
                pivote = matriz[fila_pivote][col_pivote]
                break

    if pivote == 0:
        raise ValueError("La matriz no tiene inversa (pivote 0 encontrado).")

    if pivote != 1:
        matriz[fila_pivote] = [elem / pivote for elem in matriz[fila_pivote]]

    for i in range(n):
        if i != fila_pivote:
            factor = matriz[i][col_pivote]
            if factor != 0:
                matriz[i] = [elem_i - factor * elem_p for elem_i, elem_p in zip(matriz[i], matriz[fila_pivote])]
