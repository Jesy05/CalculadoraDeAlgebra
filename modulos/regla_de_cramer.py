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

def resolver_sistema(matrix, terms):
    """Resuelve un sistema de ecuaciones lineales por la Regla de Cramer.
    
    Args:
        matrix (list): Matriz de coeficientes.
        terms (list): Vector de términos independientes.

    Returns:
        dict: Resultados con las soluciones, determinantes, y pasos detallados.
    """
    n = len(matrix)
    det_principal = calcular_determinante(matrix)

    pasos = {
        "det_principal": det_principal,
        "detalles": []
    }

    if det_principal == 0:
        return {
            "soluciones": None,
            "mensaje": "El sistema no tiene solución (determinante principal es 0).",
            "pasos": pasos
        }

    soluciones = []
    for i in range(n):
        matriz_modificada = [row[:] for row in matrix]
        for fila in range(n):
            matriz_modificada[fila][i] = terms[fila]

        det_i = calcular_determinante(matriz_modificada)
        soluciones.append(Fraction(det_i, det_principal))

        pasos["detalles"].append({
            "variable": f"x{i+1}",
            "det_i": det_i,
            "matriz_modificada": matriz_modificada,
        })

    return {
        "soluciones": soluciones,
        "mensaje": "El sistema tiene solución única.",
        "pasos": pasos
    }
