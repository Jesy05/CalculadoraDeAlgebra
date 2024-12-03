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
        det = Fraction(0)
        for c in range(n):
            menor = obtener_menor(matrix, 0, c)
            det += ((-1) ** c) * matrix[0][c] * calcular_determinante(menor)
        return det

def obtener_menor(matrix, i, j):
    """Devuelve la matriz menor al eliminar la fila i y columna j."""
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def resolver_sistema_cramer(coeficientes, terminos):
    """Resuelve un sistema de ecuaciones lineales por la regla de Cramer con soporte para fracciones."""
    try:
        # Convertir matrices y términos a Fraction
        coeficientes = [[Fraction(cell) for cell in row] for row in coeficientes]
        terminos = [Fraction(term) for term in terminos]
        det_principal = calcular_determinante(coeficientes)
        
        if det_principal == 0:
            return {
                "soluciones": None,
                "mensaje": "El sistema no tiene solución única (determinante principal es 0).",
                "pasos": {}
            }
        
        soluciones = []
        pasos = {"det_principal": det_principal, "detalles": []}
        
        for i in range(len(terminos)):
            # Crear la matriz modificada reemplazando la columna i con los términos independientes
            matriz_modificada = [row[:] for row in coeficientes]
            for fila in range(len(terminos)):
                matriz_modificada[fila][i] = terminos[fila]
            
            det_i = calcular_determinante(matriz_modificada)
            soluciones.append(Fraction(det_i, det_principal))
            pasos["detalles"].append({
                "variable": f"x{i+1}",
                "det_i": det_i,
                "matriz_modificada": [[str(cell) for cell in row] for row in matriz_modificada]
            })
        
        return {
            "soluciones": soluciones,
            "mensaje": "Sistema resuelto con éxito.",
            "pasos": pasos
        }
    
    except Exception as e:
        return {"soluciones": None, "mensaje": str(e), "pasos": {}}
