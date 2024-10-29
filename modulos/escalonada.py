# forma_escalonada.py

import streamlit as st

def imprimir_matriz(matriz, operacion=""):
    """Muestra la matriz en Streamlit con formato cuadriculado."""
    for fila in matriz:
        st.write(" | ".join(f"{int(val)}" if val.is_integer() else f"{val:.2f}" for val in fila))
    if operacion:
        st.write(f"Operación: {operacion}")

def encontrar_pivote(matriz, fila, columna):
    """Busca el pivote en la columna dada, comenzando en una fila específica."""
    num_filas = len(matriz)
    while columna < len(matriz[0]):
        for i in range(fila, num_filas):
            if matriz[i][columna] != 0:
                return i, columna
        columna += 1
    return -1, -1

def intercambiar_filas(matriz, f1, f2):
    """Intercambia dos filas si no son iguales."""
    if f1 != f2:
        matriz[f1], matriz[f2] = matriz[f2], matriz[f1]
        imprimir_matriz(matriz, f"Intercambio F{f1+1} <-> F{f2+1}")

def escalar_fila(matriz, fila, escalar):
    """Escala una fila por un valor escalar."""
    matriz[fila] = [x * escalar for x in matriz[fila]]
    imprimir_matriz(matriz, f"F{fila+1} / {escalar}")

def sumar_filas(matriz, fuente, destino, escalar):
    """Suma a la fila destino la fila fuente multiplicada por un escalar."""
    matriz[destino] = [destino_val + escalar * fuente_val for destino_val, fuente_val in zip(matriz[destino], matriz[fuente])]
    imprimir_matriz(matriz, f"F{destino+1} → F{destino+1} - ({-escalar}) * F{fuente+1}")

def forma_escalonada(matriz):
    """Convierte la matriz en forma escalonada."""
    fila_pivote = 0
    for columna in range(len(matriz[0]) - 1):
        pivote, columna_pivote = encontrar_pivote(matriz, fila_pivote, columna)
        if pivote == -1:
            continue
        intercambiar_filas(matriz, fila_pivote, pivote)
        pivot_val = matriz[fila_pivote][columna_pivote]
        if pivot_val != 1 and pivot_val != 0:
            escalar_fila(matriz, fila_pivote, 1 / pivot_val)
        for i in range(len(matriz)):
            if i != fila_pivote and matriz[i][columna_pivote] != 0:
                sumar_filas(matriz, fila_pivote, i, -matriz[i][columna_pivote])
        fila_pivote += 1

def imprimir_solucion(matriz):
    """Muestra la solución de la matriz en forma de ecuaciones."""
    num_variables = len(matriz[0]) - 1
    soluciones = ["Variable libre" for _ in range(num_variables)]
    pivotes = {}
    inconsistente = False

    for i, fila in enumerate(matriz):
        if all(f == 0 for f in fila[:-1]) and fila[-1] != 0:
            st.write("El sistema es inconsistente y no tiene solución.")
            inconsistente = True
            return
        if all(f == 0 for f in fila[:-1]):
            continue
        for j in range(num_variables):
            if fila[j] != 0:
                pivotes[j] = i
                break

    if len(pivotes) < num_variables and not inconsistente:
        st.write("La matriz es consistente y tiene soluciones infinitas.")
    elif not inconsistente:
        st.write("La matriz tiene una solución única.")

    ecuaciones = []
    for j in range(num_variables):
        if j in pivotes:
            ecuacion = ""
            fila = matriz[pivotes[j]]
            for k in range(num_variables):
                coef = fila[k]
                if coef != 0:
                    if ecuacion:
                        ecuacion += " + " if coef > 0 else " - "
                    term = f"{abs(coef)}X{k+1}" if abs(coef) != 1 else f"X{k+1}"
                    ecuacion += term
            constante = fila[-1]
            ecuacion += f" = {constante}"
            ecuaciones.append(ecuacion)
        else:
            ecuaciones.append(f"X{j+1} es una variable libre")

    st.write("Soluciones:")
    for ecuacion in ecuaciones:
        st.write(ecuacion)
