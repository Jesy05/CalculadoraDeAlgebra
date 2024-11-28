# modulos/eliminacion_gauss.py

import streamlit as st


def print_matrix(matrix, operations):
    """Muestra la matriz y la última operación realizada."""
    st.write("Matriz actual:")
    for row in matrix:
        st.write(" ".join(f"{int(num)}" if num.is_integer() else f"{num:.2f}" for num in row))
    if operations:
        st.write("Operaciones realizadas:")
        st.write(operations[-1])

def eliminacion_por_gauss(matrix):
    """Realiza la eliminación de Gauss en la matriz dada."""
    rows = len(matrix)
    cols = len(matrix[0])
    operations = []

    for i in range(rows):
        max_row = i
        for k in range(i + 1, rows):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k

        # Intercambia filas si es necesario
        if max_row != i:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            operations.append(f"F{i+1} ↔ F{max_row+1}")
            print_matrix(matrix, operations)

        pivot = matrix[i][i]
        if pivot == 0:
            st.error("La matriz es singular y no tiene solución única.")
            return None
        
        if pivot != 1:
            matrix[i] = [x / pivot for x in matrix[i]]
            operations.append(f"F{i+1} / {pivot}")
            print_matrix(matrix, operations)

        for j in range(rows):
            if j != i:
                factor = matrix[j][i]
                if factor != 0:
                    matrix[j] = [matrix[j][k] - factor * matrix[i][k] for k in range(cols)]
                    operations.append(f"F{j+1} → F{j+1} - ({factor}) * F{i+1}")
                    print_matrix(matrix, operations)

    return matrix
