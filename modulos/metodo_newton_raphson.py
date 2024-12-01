import streamlit as st
import sympy as sp
import math
import matplotlib.pyplot as plt
import re

# Función para convertir y preparar la función matemática
def preparar_funcion(funcion):
    # Reemplaza las potencias y las multiplicaciones implícitas
    funcion = funcion.replace("^", "**")  # Cambiar ^ por ** para potencias
    funcion = re.sub(r'(\d)(x)', r'\1*\2', funcion)  # Convertir 2x en 2*x
    funcion = re.sub(r'(x)(\d)', r'\1*\2', funcion)  # Convertir x2 en x*2
    funcion = funcion.replace("x", "*x")  # Añadir multiplicación explícita para x (para cuando esté solo)

    # Añadir las funciones matemáticas
    funciones_math = {
        'sin': 'math.sin', 'cos': 'math.cos', 'tan': 'math.tan',
        'cot': '1/math.tan', 'sec': '1/math.cos', 'csc': '1/math.sin',
        'log': 'math.log10', 'ln': 'math.log', 'exp': 'math.exp',
        'sqrt': 'math.sqrt', 'pi': 'math.pi', 'e': 'math.e'
    }
    # Reemplazar las funciones matemáticas
    for key, val in funciones_math.items():
        funcion = funcion.replace(key, val)  # Reemplazar funciones por su equivalente en math
    return funcion

# Método de Newton-Raphson
def newton_raphson(f, df, xi, tol=1e-4, max_iter=100):
    for i in range(max_iter):
        fxi = f(xi)
        dfxi = df(xi)
        if dfxi == 0:
            st.warning(f'Iteración {i+1}: Derivada cero. No se puede continuar.')
            return None
        xi1 = xi - fxi / dfxi
        ea = abs(xi1 - xi)
        
        if ea < tol:
            st.success(f"El método CONVERGE después de {i+1} iteraciones.\nLa raíz aproximada es: {xi1:.10f}")
            return xi1
        xi = xi1

    st.error("No convergió.")
    return None

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
        funcion_str = st.text_input("Ingrese la función f(x):", "x**3 - 6*x**2 + 11*x - 6")
        df_str = st.text_input("Ingrese la derivada f'(x):", "3*x**2 - 12*x + 11")
        xi = st.number_input("Estimación inicial (xi):", value=1.0)
        xf = st.number_input("Límite superior para graficar (xf):", value=2.0)
        tol = st.number_input("Tolerancia:", value=0.001)
        max_iter = st.number_input("Máximo de iteraciones:", value=100, min_value=1)

        # Preparar las funciones
        f = eval(f"lambda x: {preparar_funcion(funcion_str)}", {"math": math})
        df = eval(f"lambda x: {preparar_funcion(df_str)}", {"math": math})

        # Llamar al método de Newton-Raphson
        raiz = newton_raphson(f, df, xi, tol, max_iter)

        # Graficar la función y la raíz si el cálculo fue exitoso
        if raiz is not None:
            graficar_funcion(f, xi, xf, raiz)

    except Exception as e:
        st.error(f"Ocurrió un error: {e}")

# Interfaz de Streamlit
def interfaz():
    st.title("Método de Newton-Raphson")
    st.markdown("Este es el método de **Newton-Raphson** para encontrar raíces de ecuaciones no lineales.")

    # Botón para calcular la raíz
    st.subheader("Entrada de Funciones y Parámetros")
    calcular_raiz()

if __name__ == "__main__":
    interfaz()
