import streamlit as st
import sympy as sp

def prreprocesar_funcion(funcion):
    """
    Preprocesa la función para permitir notaciones comunes como `^` para exponentes 
    y multiplicaciones implícitas como `3x` y `x^2`.

    :param funcion: Función como cadena.
    :return: Función procesada como cadena.
    """
    # Reemplazar "^" por "**" para compatibilidad con SymPy
    funcion = funcion.replace("^", "**")
    
    # Convertir la cadena a una representación simbólica usando sympy
    funcion = sp.sympify(funcion, evaluate=False)
    
    return funcion

def metodo_falsa_posicion(funcion, x0, x1, tolerancia, max_iter):
    """
    Encuentra la raíz de una función usando el método de falsa posición.

    :param funcion: Función como cadena.
    :param x0: Primer valor inicial.
    :param x1: Segundo valor inicial.
    :param tolerancia: Tolerancia deseada para el error (en porcentaje: 0.0001 equivale a 0.01%).
    :param max_iter: Número máximo de iteraciones.
    :return: Diccionario con los resultados y la conclusión final.
    """
    x = sp.symbols('x')
    f = prreprocesar_funcion(funcion)

    resultados = []
    raiz_encontrada = False
    mensaje_final = ""

    for iteracion in range(1, max_iter + 1):
        fx0 = float(f.subs(x, x0))
        fx1 = float(f.subs(x, x1))

        if fx0 == fx1:  # Evitar división por cero
            mensaje_final = f"Error: División por cero en la iteración {iteracion}."
            break

        # Calcular el siguiente punto usando el método de falsa posición
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        fx2 = float(f.subs(x, x2))
        error = abs(x2 - x1)

        # Guardar los resultados de la iteración
        resultados.append((iteracion, x0, x1, x2, fx0, fx1, fx2, error))

        # Verificar si se alcanzó la tolerancia
        if error < tolerancia:
            raiz_encontrada = True
            mensaje_final = (
                f"La raíz encontrada es: {x2:.6f} en {iteracion} iteraciones "
                f"con un error de: {error:.6f}."
            )
            break

        # Actualizar los valores
        if fx0 * fx2 < 0:
            x1 = x2
        else:
            x0 = x2

    if not raiz_encontrada and not mensaje_final:
        mensaje_final = (
            f"No se encontró la raíz en el máximo de {max_iter} iteraciones. "
            "Esto puede deberse a que la raíz no está en el intervalo dado "
            "o a una elección inadecuada de valores iniciales x0 y x1."
        )

    return {
        "Iteración": [r[0] for r in resultados],
        "x0": [r[1] for r in resultados],
        "x1": [r[2] for r in resultados],
        "x2": [r[3] for r in resultados],
        "f(x0)": [r[4] for r in resultados],
        "f(x1)": [r[5] for r in resultados],
        "f(x2)": [r[6] for r in resultados],
        "Error": [r[7] for r in resultados],
        "Conclusión": mensaje_final,
    }
