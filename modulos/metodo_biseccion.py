import streamlit as st
import math

# Función para procesar y evaluar la función ingresada
def parse_function(func):
    func = func.replace("^", "**").replace(" ", "")
    func = func.replace("sin", "math.sin") \
               .replace("cos", "math.cos") \
               .replace("tan", "math.tan") \
               .replace("log", "math.log") \
               .replace("exp", "math.exp") \
               .replace("e", str(math.exp(1)))
    func = ''.join([f'*{char}' if i > 0 and char.isalpha() and func[i-1].isdigit() else char 
                    for i, char in enumerate(func)])
    return func

def eval_function(func, x):
    """Evalúa la función en x."""
    try:
        return eval(func)
    except Exception as e:
        raise ValueError(f"Error al evaluar la función: {e}")

def bisection_method(func, a, b, tol, max_iter=100):
    """Implementa el método de bisección."""
    func = parse_function(func)
    try:
        fa = eval_function(func, a)
        fb = eval_function(func, b)
    except Exception as e:
        return f"Error: {e}"

    if fa * fb > 0:
        return "El intervalo no contiene una raíz (f(a) * f(b) > 0)."
    
    results = []
    iterations = 0
    xr_prev = a
    while iterations < max_iter:
        xr = (a + b) / 2
        fc = eval_function(func, xr)
        ea = abs(xr - xr_prev) if iterations > 0 else None
        
        results.append({
            "iter": iterations + 1, "a": a, "fa": fa, "b": b, 
            "fb": fb, "xr": xr, "fc": fc, "ea": ea
        })
        
        if abs(fc) < tol or (ea is not None and ea < tol):
            return results, f"Raíz aproximada: {xr}, iteraciones: {iterations + 1}, error: {ea:.6f}" if ea else ""
        
        if fa * fc < 0:
            b = xr
            fb = fc
        else:
            a = xr
            fa = fc
        
        xr_prev = xr
        iterations += 1

    return results, "No se encontró una raíz dentro del máximo de iteraciones."
