import streamlit as st
import random

# Preguntas de ejemplo basadas en las funciones de la calculadora
PREGUNTAS = [
    {
        "pregunta": "¿Cuál es el resultado de sumar los vectores (1,2) y (3,4)?",
        "respuestas": ["(4,6)"],
        "opciones": ["(4,5)", "(4,6)", "(3,6)"]
    },
    {
        "pregunta": "¿Qué propiedad cumple la transpuesta de una matriz?",
        "respuestas": ["(A^T)^T = A"],
        "opciones": ["A + B = B + A", "(A^T)^T = A", "A * B = B * A"]
    },
    {
        "pregunta": "Si A es una matriz 2x2 con determinante 0, ¿qué significa?",
        "respuestas": ["La matriz no es invertible"],
        "opciones": ["La matriz es invertible", "La matriz no es invertible", "El determinante es mayor a 1"]
    },
    {
        "pregunta": "¿Qué significa que dos vectores sean linealmente dependientes?",
        "respuestas": ["Uno es múltiplo escalar del otro"],
        "opciones": ["Son perpendiculares", "Uno es múltiplo escalar del otro", "Forman un ángulo de 90 grados"]
    },
    {
        "pregunta": "¿Cuál es el resultado de multiplicar la matriz identidad por cualquier matriz A?",
        "respuestas": ["La matriz A"],
        "opciones": ["La matriz identidad", "La matriz A", "La matriz transpuesta de A"]
    }
]

# Inicializar las variables de estado si no existen
if 'is_running' not in st.session_state:
    st.session_state.is_running = False
if 'current_question' not in st.session_state:
    st.session_state.current_question = None
if 'current_options' not in st.session_state:
    st.session_state.current_options = None
if 'current_answers' not in st.session_state:
    st.session_state.current_answers = None

# Función para generar una pregunta aleatoria
def generar_pregunta():
    pregunta = random.choice(PREGUNTAS)
    opciones = random.sample(pregunta["opciones"], len(pregunta["opciones"]))  # Mezcla las opciones
    return pregunta["pregunta"], opciones, pregunta["respuestas"]

# Función principal del juego
def pantalla_juego():
    st.write("### 🎮¡Ejercita tus conocimientos con el juego de preguntas de álgebra lineal!🎮")

    # Iniciar el juego
    if st.button("Iniciar juego"):
        st.session_state.current_question, st.session_state.current_options, st.session_state.current_answers = generar_pregunta()

    # Mostrar pregunta y opciones
    if st.session_state.current_question:
        st.write(st.session_state.current_question)
        seleccion = st.radio("Selecciona la respuesta correcta:", st.session_state.current_options, key="opciones_radio")

        # Verificar respuesta
        if st.button("Verificar respuesta"):
            if seleccion in st.session_state.current_answers:
                st.success("¡Correcto! 👍")
            else:
                st.error("Incorrecto 😞, intenta de nuevo o pasa a la siguiente pregunta.")

        # Botón para mostrar la siguiente pregunta
        if st.button("Siguiente"):
            st.session_state.current_question, st.session_state.current_options, st.session_state.current_answers = generar_pregunta()

# Llamar a la pantalla del juego
pantalla_juego()
