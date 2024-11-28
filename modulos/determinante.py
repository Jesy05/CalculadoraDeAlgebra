from fractions import Fraction

def calcular_determinante(matrix):
    """Calcula el determinante de una matriz cuadrada."""
    n = len(matrix)
    if n == 2:
        # Determinante para matriz 2x2
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif n == 3:
        # Determinante por el método de Sarrus para matriz 3x3
        return (matrix[0][0] * matrix[1][1] * matrix[2][2] +
                matrix[0][1] * matrix[1][2] * matrix[2][0] +
                matrix[0][2] * matrix[1][0] * matrix[2][1]) - \
               (matrix[0][2] * matrix[1][1] * matrix[2][0] +
                matrix[0][0] * matrix[1][2] * matrix[2][1] +
                matrix[0][1] * matrix[1][0] * matrix[2][2])
    else:
        # Determinante por cofactores para matrices mayores
        det = 0
        for c in range(n):
            menor = obtener_menor(matrix, 0, c)
            det += ((-1) ** c) * matrix[0][c] * calcular_determinante(menor)
        return det

def obtener_menor(matrix, i, j):
    """Devuelve la matriz menor al eliminar la fila i y columna j."""
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def pasos_determinante(matrix):
    """Genera los pasos detallados para calcular el determinante."""
    pasos = "Pasos para calcular el determinante:\n"
    n = len(matrix)

    if n == 2:
        pasos += f"Para matriz 2x2: {matrix[0][0]} * {matrix[1][1]} - {matrix[0][1]} * {matrix[1][0]}.\n"
    elif n == 3:
        pasos += "Para matriz 3x3 usando Sarrus:\n"
        pasos += f"Positivo: {matrix[0][0]} * {matrix[1][1]} * {matrix[2][2]} + {matrix[0][1]} * {matrix[1][2]} * {matrix[2][0]} + {matrix[0][2]} * {matrix[1][0]} * {matrix[2][1]}.\n"
        pasos += f"Negativo: {matrix[0][2]} * {matrix[1][1]} * {matrix[2][0]} + {matrix[0][0]} * {matrix[1][2]} * {matrix[2][1]} + {matrix[0][1]} * {matrix[1][0]} * {matrix[2][2]}.\n"
    else:
        pasos += "Para matriz mayor, usando cofactores:\n"
        for c in range(len(matrix)):
            menor = obtener_menor(matrix, 0, c)
            pasos += f"Menor eliminando fila 1 y columna {c+1}: {menor}, coeficiente: {matrix[0][c]}.\n"

    return pasos
