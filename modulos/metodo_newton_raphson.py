import streamlit as st
import math
import matplotlib.pyplot as plt
import re

# Función para convertir y preparar la función matemática
def preparar_funcion(funcion):
    # Reemplaza las potencias y las multiplicaciones implícitas
    funcion = funcion.replace("^", "**")  # Cambiar ^ por ** para potencias
    funcion = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', funcion)  # Convertir 2x en 2*x
    funcion = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', funcion)  # Convertir x2 en x*2

    # Reemplazar funciones matemáticas en español
    funciones_spanish = {
        'sen': 'math.sin',  # seno
        'cos': 'math.cos',  # coseno
        'tan': 'math.tan',  # tangente
        'cot': '(1/math.tan)',  # cotangente
        'sec': '(1/math.cos)',  # secante
        'csc': '(1/math.sin)',  # cosecante
        'ln': 'math.log',       # logaritmo natural
        'log': 'math.log10',    # logaritmo base 10
        'exp': 'math.exp',      # exponencial
        'sqrt': 'math.sqrt',    # raíz cuadrada
        'pi': 'math.pi',        # constante pi
        'e': 'math.e'           # constante e
    }

    for key, val in funciones_spanish.items():
        funcion = funcion.replace(key, val)

    # Simplificaciones trigonométricas comunes
    funcion = funcion.replace("sen^2", "(math.sin(x)**2)")  # sen^2(x)
    funcion = funcion.replace("cos^2", "(math.cos(x)**2)")  # cos^2(x)
    funcion = funcion.replace("tan^2", "(math.tan(x)**2)")  # tan^2(x)

    return funcion

# Método de Newton-Raphson
def newton_raphson(f, df, xi, tol=1e-4, max_iter=100):
    resultados = []  # Lista para guardar los resultados de cada iteración
    for i in range(max_iter):
        fxi = f(xi)
        dfxi = df(xi)
        if dfxi == 0:
            st.warning(f'Iteración {i+1}: Derivada cero. No se puede continuar.')
            return None, resultados
        xi1 = xi - fxi / dfxi
        ea = abs(xi1 - xi)
        
        resultados.append((i+1, round(xi, 4), round(xi1, 4), round(ea, 4), round(fxi, 4), round(dfxi, 4)))
        
        if ea < tol:
            st.success(f"El método CONVERGE después de {i+1} iteraciones.\nLa raíz aproximada es: {xi1:.10f}")
            return xi1, resultados
        xi = xi1

    st.error("No convergió.")
    return None, resultados

# Graficar la función
def graficar_funcion(f, xi, xf, raiz):
    x = [xi + (xf - xi) * i / 1000 for i in range(1001)]
    y = [f(val) for val in x]
    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(raiz, color='r', linestyle='--', label=f'Raíz aproximada: {raiz:.4f}')
    plt.title('Gráfica de la función')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    st.pyplot(plt)

# Función principal para calcular la raíz
def calcular_raiz():
    try:
        # Recoger las entradas del usuario
        funcion_str = st.text_input("Ingrese la función f(x):", "sen^2(x) + cos^2(x) - 1")
        df_str = st.text_input("Ingrese la derivada f'(x):", "2*sen(x)*cos(x)")
        xi = st.number_input("Estimación inicial (xi):", value=0.5)
        xf = st.number_input("Límite superior para graficar (xf):", value=3.0)
        tol = st.number_input("Tolerancia:", value=0.001)
        max_iter = st.number_input("Máximo de iteraciones:", value=100, min_value=1)

        # Preparar las funciones
        f = eval(f"lambda x: {preparar_funcion(funcion_str)}", {"math": math})
        df = eval(f"lambda x: {preparar_funcion(df_str)}", {"math": math})

        # Llamar al método de Newton-Raphson
        raiz, resultados = newton_raphson(f, df, xi, tol, max_iter)

        # Mostrar tabla de resultados
        if raiz is not None:
            st.subheader("Resultados por Iteración")
            st.table(
                {
                    "Iteración": [r[0] for r in resultados],
                    "xi": [r[1] for r in resultados],
                    "xi+1": [r[2] for r in resultados],
                    "Ea": [r[3] for r in resultados],
                    "f(xi)": [r[4] for r in resultados],
                    "f'(xi)": [r[5] for r in resultados]
                }
            )

            # Graficar la función y la raíz si el cálculo fue exitoso
            graficar_funcion(f, xi, xf, raiz)

    except Exception as e:
        st.error(f"Ocurrió un error: {e}")

# Llamar la función principal
if __name__ == "__main__":
    st.title("Método de Newton-Raphson Mejorado (Funciones en Español)")
    calcular_raiz()
