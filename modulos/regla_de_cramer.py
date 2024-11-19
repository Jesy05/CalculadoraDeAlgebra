import streamlit as st
from fractions import Fraction

# Función para calcular el determinante de una matriz
def determinante(matrix):
    n = len(matrix)
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif n == 3:
        return (matrix[0][0] * matrix[1][1] * matrix[2][2] +
                matrix[0][1] * matrix[1][2] * matrix[2][0] +
                matrix[0][2] * matrix[1][0] * matrix[2][1]) - \
               (matrix[0][2] * matrix[1][1] * matrix[2][0] +
                matrix[0][0] * matrix[1][2] * matrix[2][1] +
                matrix[0][1] * matrix[1][0] * matrix[2][2])
    else:
        det = 0
        for c in range(n):
            det += ((-1) ** c) * matrix[0][c] * determinante(menor(matrix, 0, c))
        return det

# Función para obtener el menor de una matriz
def menor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

# Función para resolver el sistema de ecuaciones usando la regla de Cramer
def cramer_regla(matrix, terms):
    det_principal = determinante(matrix)
    texto_pasos = "<b>Determinante principal:</b>\n\n"

    # Mostrar la matriz original
    texto_pasos += "Matriz original:\n"
    texto_pasos += formatear_matriz(matrix, -1)

    # Mostrar el proceso del cálculo del determinante principal
    texto_pasos += multiplicaciones_detalle(matrix)
    texto_pasos += f"Determinante principal: {det_principal}\n"

    if det_principal == 0:
        texto_pasos += "<b>El sistema no tiene solución ya que el determinante principal es 0.</b>\n"
        st.write("El sistema no tiene solución (determinante principal es 0).")
        st.write(texto_pasos, unsafe_allow_html=True)
        return None

    variables = ['x', 'y', 'z', 'w']
    soluciones = []
    texto_pasos += "<b>Determinantes y soluciones:</b>\n\n"
    
    for i in range(len(matrix)):
        matriz_modificada = [row[:] for row in matrix]
        texto_pasos += f"\n<b>Calculando determinante para {variables[i]}:</b>\n"
        
        for fila in range(len(matriz_modificada)):
            texto_pasos += f"Reemplazando columna {i+1} por los términos independientes: {matriz_modificada[fila][i]} -> <font color='blue'>{terms[fila]}</font>\n"
            matriz_modificada[fila][i] = terms[fila]

        texto_pasos += formatear_matriz(matriz_modificada, i)
        texto_pasos += multiplicaciones_detalle(matriz_modificada)

        det_i = determinante(matriz_modificada)
        texto_pasos += f"Determinante de {variables[i]}: {det_i}/{det_principal} = {Fraction(det_i, det_principal)}\n"
        soluciones.append(Fraction(det_i, det_principal))

    texto_resultado = "Soluciones:\n"
    for i in range(len(soluciones)):
        texto_resultado += f"{variables[i]} = {soluciones[i]}\n"

    st.write(texto_resultado)
    st.write(texto_pasos, unsafe_allow_html=True)
    return soluciones

# Función para formatear la matriz
def formatear_matriz(matrix, columna_reemplazada):
    texto = ""
    for fila in matrix:
        texto += "["
        for i, valor in enumerate(fila):
            if i == columna_reemplazada:
                texto += f"<font color='blue'>{valor}</font>\t"
            else:
                texto += f"{valor}\t"
        texto = texto.strip() + "]\n"
    texto += "\n"
    return texto

# Función para mostrar el detalle de las multiplicaciones
def multiplicaciones_detalle(matrix):
    texto = ""
    if len(matrix) == 2:
        texto += f"Multiplicación: {matrix[0][0]} * {matrix[1][1]} - {matrix[0][1]} * {matrix[1][0]}\n"
    elif len(matrix) == 3:
        texto += f"Multiplicación:\n {matrix[0][0]} * {matrix[1][1]} * {matrix[2][2]} + {matrix[0][1]} * {matrix[1][2]} * {matrix[2][0]} + {matrix[0][2]} * {matrix[1][0]} * {matrix[2][1]}\n"
        texto += f" - ({matrix[0][2]} * {matrix[1][1]} * {matrix[2][0]} + {matrix[0][0]} * {matrix[1][2]} * {matrix[2][1]} + {matrix[0][1]} * {matrix[1][0]} * {matrix[2][2]})\n"
    texto += "\n"
    return texto

# Función principal para la interfaz de Streamlit
def main():
    st.title("Calculadora de Cramer")
    st.write("Seleccione el número de variables y luego ingrese los coeficientes:")

    num_variables = st.selectbox("Número de variables", [2, 3, 4])

    matrix = []
    terms = []
    for i in range(num_variables):
        row = []
        for j in range(num_variables):
            row.append(st.number_input(f"Coeficiente ({i+1},{j+1})", key=f"coef_{i}_{j}"))
        matrix.append(row)
        terms.append(st.number_input(f"Término independiente {i+1}", key=f"term_{i}"))

    if st.button("Resolver"):
        soluciones = cramer_regla(matrix, terms)
        if soluciones:
            st.write("Soluciones:")
            for i, sol in enumerate(soluciones):
                st.write(f"x_{i+1} = {sol}")

if __name__ == "__main__":
    main()
