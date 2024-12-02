import streamlit as st
import sympy as sp
import re

# Función para convertir y preparar la función matemática
def preparar_funcion(funcion):
    funciones_math = {
        'sen': 'sin',
        'sin': 'sin',
        'cos': 'cos',
        'tan': 'tan',
        'cot': '1/tan',
        'sec': '1/cos',
        'csc': '1/sin',
        'log': 'log10',
        'ln': 'log',
        'exp': 'exp',
        'sqrt': 'sqrt',
        'pi': 'pi',
        'e': 'E'
    }
    try:
        funcion = funcion.replace('^', '**').replace(' ', '')
        funcion = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', funcion)
        funcion = re.sub(r'(\))(?=\d|[a-zA-Z])', r')*', funcion)
        for key, val in funciones_math.items():
            funcion = re.sub(r'\b' + key + r'\b', val, funcion)
        return funcion
    except Exception as e:
        raise ValueError(f"Error al procesar la función: {e}")

# Método de Falsa Posición
def falsa_posicion(funcion, xi, xu, tolerancia, max_iter):
    resultados = []
    f = sp.sympify(funcion)
    xi, xu = float(xi), float(xu)
    
    # Inicialización de xr_ant
    xr_ant = None
    
    for i in range(max_iter):
        # Evaluar la función en los puntos xi, xu y en el valor xr
        yi = f.subs('x', xi)
        yu = f.subs('x', xu)
        
        # Calcular la raíz aproximada xr
        xr = xu - (yu * (xi - xu)) / (yi - yu)
        yr = f.subs('x', xr)
        
        # Calcular el error relativo respecto a la iteración anterior
        ea = abs((xr - xi) / xr) * 100 if xr_ant is None else abs((xr - xr_ant) / xr) * 100
        
        # Guardar los resultados en la lista de resultados
        resultados.append([i + 1, round(xi, 4), round(xu, 4), round(xr, 4), round(ea, 4) if ea else '', round(yi, 4), round(yu, 4), round(yr, 4)])
        
        # Verificar el criterio de detención basado en el error relativo entre iteraciones
        if ea is not None and ea < tolerancia:
            break
        
        # Actualizar el valor de xi o xu según el signo de f(x)
        if yi * yr < 0:
            xu = xr
        else:
            xi = xr
        
        # Actualizar xr_ant para la siguiente iteración
        xr_ant = xr
    
    resultado_final = f"Raíz aproximada: {xr:.6f}, Error aproximado: {ea:.6f}%, Método converge en {i + 1} iteraciones."
    return resultados, resultado_final

# Interfaz de usuario en Streamlit
st.title("Métodos Numéricos - Falsa Posición")

# Entradas
funcion = st.text_input("Función (con 'x' como variable):")
xi = st.text_input("xi:")
xu = st.text_input("xu:")
tolerancia = st.text_input("Tolerancia (%):")
max_iter = st.text_input("Máx. Iteraciones:")

# Calcular cuando el usuario presiona el botón
if st.button("Calcular"):
    if not funcion or not xi or not xu or not tolerancia or not max_iter:
        st.error("Por favor, completa todos los campos.")
    else:
        try:
            funcion = preparar_funcion(funcion)
            tol = float(tolerancia)
            max_iter = int(max_iter)
            resultados, resumen = falsa_posicion(funcion, xi, xu, tol, max_iter)
            # Mostrar resultados
            columnas = ['Iteración', 'xi', 'xu', 'xr', 'Ea', 'yi', 'yu', 'yr']
            st.write("### Resultados")
            st.table(resultados)
            st.write("### Resumen")
            st.write(resumen)
        except Exception as e:
            st.error(f"Se produjo un error: {e}")
            
# Limpiar campos cuando el usuario lo desee
if st.button("Limpiar"):
    st.experimental_rerun()  # Esto recarga la página y limpia los campos
