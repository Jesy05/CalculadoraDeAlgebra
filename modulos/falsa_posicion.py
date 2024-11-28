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

# Función para actualizar la entrada de la función con los botones
def actualizar_funcion(simbolo):
    if "funcion" not in st.session_state:
        st.session_state["funcion"] = ""
    # Concatenar el símbolo al final de la función actual
    st.session_state["funcion"] += simbolo

# Función principal
def falsa_posicion():
    st.title("Método de Falsa Posición")

    # Inicializar variable dinámica para la entrada de la función si no existe
    if "funcion" not in st.session_state:
        st.session_state["funcion"] = ""

    # Mostrar panel de botones interactivos
    st.subheader("Panel de Símbolos y Funciones")

    # Botones organizados en una matriz
    botones = [
        ["sen", "cos", "tan", "log", "ln"],
        ["+F", "-", "*", "/", "^"],
        ["raiz^2", "pi", "e", "(", ")"]
    ]



    # Generar botones en forma de cuadrícula
    for fila in botones:
        cols = st.columns(len(fila))  # Crear columnas dinámicamente
        for i, simbolo in enumerate(fila):
            with cols[i]:
                st.button(simbolo, on_click=lambda s=simbolo: actualizar_funcion(s))

    # Sincronizar el cuadro de texto con el estado de la sesión
    funcion_str = st.text_input(
        "Ingrese la función f(x):",
        value=st.session_state["funcion"],
        key="funcion_input",
        placeholder="Escriba aquí su función",
    )

    # Verificar si se modificó manualmente el cuadro de texto
    if funcion_str != st.session_state["funcion"]:
        st.session_state["funcion"] = funcion_str  # Actualizar el estado dinámico

    # Campos de entrada adicionales
    xi = st.number_input("Ingrese el valor de xi:", format="%.4f")
    xu = st.number_input("Ingrese el valor de xu:", format="%.4f")
    tolerancia = st.number_input("Ingrese la tolerancia (%):", value=0.01, step=0.01, format="%.4f")
    max_iter = st.number_input("Máximo de iteraciones:", min_value=1, value=50, step=1)

    if st.button("Calcular"):
        try:
            # Convertir la función ingresada
            funcion = sp.sympify(preparar_funcion(st.session_state["funcion"]))
            x = sp.symbols('x')

            # Validación inicial
            f_xi = funcion.subs(x, xi)
            f_xu = funcion.subs(x, xu)
            if f_xi * f_xu > 0:
                st.error("La función no cambia de signo en el intervalo dado. Intente con otros valores de xi y xu.")
                return

            # Inicialización
            iteracion = 0
            xr_anterior = None
            resultados = []

            # Iteraciones del método
            while iteracion < max_iter:
                f_xi = funcion.subs(x, xi)
                f_xu = funcion.subs(x, xu)
                
                # Calcular xr y f(xr)
                xr = xu - (f_xu * (xi - xu)) / (f_xi - f_xu)
                f_xr = funcion.subs(x, xr)

                # Calcular error relativo
                ea = abs((xr - xr_anterior) / xr) * 100 if xr_anterior is not None else None

                # Guardar datos de la iteración
                resultados.append(
                    [iteracion + 1, round(xi, 4), round(xu, 4), round(xr, 4), round(ea, 4) if ea else '-', round(f_xi, 4), round(f_xu, 4), round(f_xr, 4)]
                )

                # Verificar convergencia
                if ea is not None and ea < tolerancia:
                    break

                # Actualizar intervalos
                if f_xi * f_xr < 0:
                    xu = xr
                else:
                    xi = xr

                xr_anterior = xr
                iteracion += 1

            # Mostrar resultados en tabla
            st.write("### Resultados por Iteración")
            st.dataframe(
                {
                    "Iteración": [r[0] for r in resultados],
                    "xi": [r[1] for r in resultados],
                    "xu": [r[2] for r in resultados],
                    "xr": [r[3] for r in resultados],
                    "Error (%)": [r[4] for r in resultados],
                    "f(xi)": [r[5] for r in resultados],
                    "f(xu)": [r[6] for r in resultados],
                    "f(xr)": [r[7] for r in resultados],
                }
            )

            # Resumen final
            st.success(f"Raíz aproximada: {xr:.6f}")
            st.info(f"Error aproximado: {ea:.6f}%")
            st.info(f"Método converge en {iteracion + 1} iteraciones.")

        except Exception as e:
            st.error(f"Ocurrió un error: {e}")

# Ejecutar la función principal
if __name__ == "__main__":
    falsa_posicion()
