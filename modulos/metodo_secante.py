import streamlit as st
import sympy as sp

def preprocesar_funcion(funcion):
    """
    Preprocesa la función para permitir notaciones comunes como `^` para exponentes 
    y multiplicaciones implícitas como `3x` y `x^2`.

    :param funcion: Función como cadena.
    :return: Función procesada como una expresión simbólica de sympy.
    """
    # Reemplazar "^" por "**" para compatibilidad con SymPy
    funcion = funcion.replace("^", "**")
    
    # Convertir la cadena a una representación simbólica usando sympy
    try:
        funcion = sp.sympify(funcion, evaluate=False)
    except Exception as e:
        raise ValueError(f"Error en la función ingresada: {e}")
    
    return funcion

def metodo_secante(funcion, x0, x1, tolerancia, max_iter, usar_intervalos):
    """
    Encuentra la raíz de una función usando el método del secante.

    :param funcion: Función como cadena.
    :param x0: Primer valor inicial.
    :param x1: Segundo valor inicial.
    :param tolerancia: Tolerancia deseada para el error (en porcentaje: 0.0001 equivale a 0.01%).
    :param max_iter: Número máximo de iteraciones.
    :param usar_intervalos: Si es True, se trabaja con intervalos, si es False, no.
    :return: Diccionario con los resultados y la conclusión final.
    """
    x = sp.symbols('x')
    f = preprocesar_funcion(funcion)

    resultados = []
    raiz_encontrada = False
    mensaje_final = ""

    # Si no se utilizan intervalos, ajustamos x1 igual a x0
    if not usar_intervalos:
        x1 = x0 + 1e-5  # Usamos un valor arbitrario pequeño para x1

    for iteracion in range(1, max_iter + 1):
        fx0 = float(f.subs(x, x0))
        fx1 = float(f.subs(x, x1))

        if fx1 - fx0 == 0:  # Evitar división por cero
            mensaje_final = f"Error: División por cero en la iteración {iteracion}."
            break

        # Calcular el siguiente x2
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        error = abs(x2 - x1)

        # Guardar los resultados de la iteración
        resultados.append((iteracion, x0, x1, x2, error, fx0, fx1))

        # Verificar si se alcanzó la tolerancia
        if error < tolerancia:
            raiz_encontrada = True
            mensaje_final = (
                f"La raíz encontrada es: {x2:.6f} en {iteracion} iteraciones "
                f"con un error de: {error:.6f}."
            )
            break

        # Actualizar valores
        x0, x1 = x1, x2

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
        "Error": [r[4] for r in resultados],
        "f(x0)": [r[5] for r in resultados],
        "f(x1)": [r[6] for r in resultados],
        "Conclusión": mensaje_final,
    }
