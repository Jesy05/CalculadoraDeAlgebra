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

# Método de la Secante
def metodo_secante(funcion, x0, x1, tolerancia, max_iter):
    resultados = []
    f = sp.sympify(funcion)
    x0, x1 = float(x0), float(x1)
    ea = None  # Inicializamos el error aproximado
    
    for i in range(max_iter):
        y0 = f.subs('x', x0)
        y1 = f.subs('x', x1)

        if y1 - y0 == 0:
            raise ZeroDivisionError("La división por cero ocurrió en el método de la secante.")

        x2 = x1 - y1 * (x1 - x0) / (y1 - y0)
        ea = abs((x2 - x1) / x2) * 100 if i > 0 else None
        resultados.append([i + 1, x0, x1, x2, ea, y0, y1])

        # Detener el método si el error aproximado es menor que la tolerancia
        if ea is not None and ea < tolerancia:
            break

        x0, x1 = x1, x2

    # Conclusión final
    resultado_final = f"La raíz aproximada es {x2:.6f}, el error aproximado es {ea:.6f}, el método converge a {i + 1} iteraciones."
    return resultados, resultado_final

# Interfaz con Streamlit
st.title("Método de la Secante - Streamlit")
st.markdown("Aplicación para resolver ecuaciones no lineales usando el Método de la Secante.")

# Entrada de datos
funcion = st.text_input("Introduce la función (usa 'x' como variable):", value="x^3 - 6*x^2 + 11*x - 6")
usar_intervalos = st.checkbox("¿Usar intervalos?")

x0 = st.text_input("Introduce x0:", value="1" if usar_intervalos else "", key="x0")
x1 = st.text_input("Introduce x1:", value="2" if usar_intervalos else "", key="x1")
tolerancia = st.number_input("Tolerancia:", min_value=0.0, value=0.001, step=0.0001, format="%.6f")
max_iter = st.number_input("Máx. Iteraciones:", min_value=1, value=50, step=1)

# Botón de cálculo
if st.button("Calcular"):
    try:
        funcion_preparada = preparar_funcion(funcion)

        if usar_intervalos:
            if not x0 or not x1:
                st.error("Por favor, completa los intervalos si seleccionaste usarlos.")
            else:
                resultados, resumen = metodo_secante(funcion_preparada, x0, x1, tolerancia, max_iter)
                st.success(resumen)
        else:
            x0 = x0 if x0 else "1"
            x1 = x1 if x1 else "2"
            resultados, resumen = metodo_secante(funcion_preparada, x0, x1, tolerancia, max_iter)
            st.success(resumen)

        # Mostrar tabla de resultados
        st.subheader("Resultados por iteración")
        st.table(resultados)

    except Exception as e:
        st.error(f"Se produjo un error: {e}")
