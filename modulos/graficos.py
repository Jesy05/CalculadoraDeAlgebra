import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def pantalla_graficos():
    st.write("### 📈📊Herramientas para Gráficas📐📉")
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
        rango_x = st.slider("Seleccione el rango de x:", -10, 10, (-5, 5))
        puntos = st.number_input("Número de puntos:", min_value=10, max_value=1000, value=100)

        if st.button("Graficar Función"):
            try:
                x = np.linspace(rango_x[0], rango_x[1], puntos)
                y = eval(funcion)  # Se evalúa la función ingresada
                fig = plt.figure(figsize=(8, 5))
                plt.plot(x, y, label=f"y = {funcion}")
                plt.title("Gráfica de la función")
                plt.xlabel("x")
                plt.ylabel("y")
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

        if st.button("Graficar Vectores"):
            try:
                # Procesar los vectores
                v1 = np.array([float(n) for n in vector1.split(",")])
                v2 = np.array([float(n) for n in vector2.split(",")])
                
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

        if st.button("Graficar Matriz"):
            try:
                # Procesar la matriz
                matriz = np.array([[float(num) for num in fila.split(",")] for fila in matriz.split(";")])
                
                # Graficar matriz
                fig, ax = plt.subplots(figsize=(6, 6))
                cax = ax.imshow(matriz, cmap="viridis", aspect="auto")
                fig.colorbar(cax, label="Valores")
                ax.set_title("Gráfica de Matriz")
                ax.set_xlabel("Columnas")
                ax.set_ylabel("Filas")
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Error al graficar la matriz: {e}")
