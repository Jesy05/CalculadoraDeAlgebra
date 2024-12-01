import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def resolver_sistema(a1, b1, c1, a2, b2, c2):
    """
    Resuelve un sistema de ecuaciones lineales de la forma:
    a1*x + b1*y = c1
    a2*x + b2*y = c2

    Devuelve el tipo de solución y los valores (si aplica).
    """
    # Matriz de coeficientes
    A = np.array([[a1, b1], [a2, b2]])
    # Vector de términos independientes
    B = np.array([c1, c2])

    # Determinante de la matriz de coeficientes
    det = np.linalg.det(A)

    if det != 0:  # Solución única
        solucion = np.linalg.solve(A, B)
        return "Única solución", solucion
    else:  # Determinante cero: revisar si son equivalentes o paralelas
        # Verificar si los vectores son proporcionales
        proporcion_a = a1 / a2 if a2 != 0 else None
        proporcion_b = b1 / b2 if b2 != 0 else None
        proporcion_c = c1 / c2 if c2 != 0 else None

        if proporcion_a == proporcion_b == proporcion_c:
            return "Infinitas soluciones", None  # Rectas equivalentes
        else:
            return "Sin solución", None  # Rectas paralelas


def graficar_sistema(a1, b1, c1, a2, b2, c2):
    """
    Genera y devuelve una figura del sistema de ecuaciones.
    """
    # Crear puntos para las rectas
    x = np.linspace(-10, 10, 400)
    
    # Recta 1: despejamos y = (-a1*x + c1) / b1
    y1 = (-a1 * x + c1) / b1 if b1 != 0 else None
    
    # Recta 2: despejamos y = (-a2*x + c2) / b2
    y2 = (-a2 * x + c2) / b2 if b2 != 0 else None

    # Crear la figura
    fig, ax = plt.subplots(figsize=(8, 6))
    if y1 is not None:
        ax.plot(x, y1, label=f"{a1}x + {b1}y = {c1}", color='blue')
    if y2 is not None:
        ax.plot(x, y2, label=f"{a2}x + {b2}y = {c2}", color='red')
    
    ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
    ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
    ax.legend()
    ax.set_title("Gráfica del sistema de ecuaciones")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid()

    return fig
