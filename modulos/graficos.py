import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

def convertir_a_float(valor):
    """Convierte una entrada en formato de fracción o flotante a un número flotante."""
    try:
        return float(Fraction(valor))
    except ValueError:
        raise ValueError(f"El valor '{valor}' no es un número válido o fracción.")

def pantalla_graficos():
    st.write("### 📈📊 Herramientas para Gráficas 📐📉")
    st.write("Prepara datos para graficar funciones, vectores o matrices. Aquí puedes configurar las entradas iniciales.")

    # Seleccionar tipo de gráfica
    tipo_grafica = st.selectbox(
        "Selecciona el tipo de gráfica:",
        ["Seleccione...", "Gráfica de Función", "Gráfica de Vectores", "Gráfica de Matrices"],
    )

    if tipo_grafica == "Gráfica de Función":
        st.write("#### Configuración para Gráfica de Función")

        # Entradas para función
        funcion = st.text_input("Ingrese la función (en términos de x):", value="x**2")
        rango_x = st.text_input("Ingrese el rango de x (formato: min,max):", value="-5,5")
        puntos = st.number_input("Número de puntos:", min_value=10, max_value=1000, value=100)
        nombre_ejes = st.text_input("Nombres de los ejes (formato: x,y):", value="x,y")

        if st.button("Graficar Función"):
            try:
                # Procesar rango y nombres de ejes
                min_x, max_x = [convertir_a_float(v) for v in rango_x.split(",")]
                nombre_x, nombre_y = nombre_ejes.split(",")

                # Crear datos y graficar
                x = np.linspace(min_x, max_x, puntos)
                y = eval(funcion)  # Se evalúa la función ingresada
                fig = plt.figure(figsize=(8, 5))
                plt.plot(x, y, label=f"y = {funcion}")
                plt.title("Gráfica de la función")
                plt.xlabel(nombre_x.strip())
                plt.ylabel(nombre_y.strip())
                plt.grid()
                plt.legend()
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Error al graficar la función: {e}")

    elif tipo_grafica == "Gráfica de Vectores":
        st.write("#### Configuración para Gráfica de Vectores")

        # Entradas para vectores
        st.write("Ingrese las coordenadas de los vectores (2D o 3D):")
        vector1 = st.text_input("Vector 1 (formato: x,y,z):", value="1,2,0")
        vector2 = st.text_input("Vector 2 (formato: x,y,z):", value="2,1,0")
        nombre_ejes = st.text_input("Nombres de los ejes (formato: x,y[,z]):", value="x,y,z")

        if st.button("Graficar Vectores"):
            try:
                # Procesar los vectores y nombres de ejes
                v1 = np.array([convertir_a_float(n) for n in vector1.split(",")])
                v2 = np.array([convertir_a_float(n) for n in vector2.split(",")])
                nombres = nombre_ejes.split(",")

                # Comprobar dimensiones
                if len(v1) != len(v2) or len(v1) not in [2, 3]:
                    st.error("Ambos vectores deben tener la misma dimensión (2D o 3D).")
                    return

                # Graficar
                fig = plt.figure(figsize=(8, 5))
                ax = fig.add_subplot(111, projection="3d" if len(v1) == 3 else None)
                ax.quiver(0, 0, 0, *v1, color="r", label="Vector 1")
                ax.quiver(0, 0, 0, *v2, color="b", label="Vector 2")
                ax.set_title("Gráfica de Vectores")
                ax.set_xlabel(nombres[0].strip())
                ax.set_ylabel(nombres[1].strip())
                if len(v1) == 3:
                    ax.set_zlabel(nombres[2].strip())
                ax.legend()
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Error al graficar los vectores: {e}")

    elif tipo_grafica == "Gráfica de Matrices":
        st.write("#### Configuración para Gráfica de Matrices")

        # Entrada de matriz
        matriz = st.text_area(
            "Ingrese la matriz (filas separadas por ';', valores separados por ','):",
            value="1,2,3;4,5,6;7,8,9",
        )
        nombre_ejes = st.text_input("Nombres de los ejes (formato: x,y):", value="Columnas,Filas")

        if st.button("Graficar Matriz"):
            try:
                # Procesar la matriz y nombres de ejes
                matriz = np.array([[convertir_a_float(num) for num in fila.split(",")] for fila in matriz.split(";")])
                nombre_x, nombre_y = nombre_ejes.split(",")

                # Graficar matriz
                fig, ax = plt.subplots(figsize=(6, 6))
                cax = ax.imshow(matriz, cmap="viridis", aspect="auto")
                fig.colorbar(cax, label="Valores")
                ax.set_title("Gráfica de Matriz")
                ax.set_xlabel(nombre_x.strip())
                ax.set_ylabel(nombre_y.strip())
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Error al graficar la matriz: {e}")
