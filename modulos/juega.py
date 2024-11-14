import streamlit as st
import random
import time

# Preguntas de ejemplo basadas en las funciones de la calculadora
PREGUNTAS = [
    {"pregunta": "¿Cuál es el resultado de sumar los vectores (1,2) y (3,4)?", "respuesta": "(4,6)", "opciones": ["(4,5)", "(4,6)", "(3,6)"]},
    {"pregunta": "¿Qué propiedad cumple la transpuesta de una matriz?", "respuesta": "(A^T)^T = A", "opciones": ["A + B = B + A", "(A^T)^T = A", "A * B = B * A"]},
    # Agrega más preguntas en función de las operaciones de tu calculadora
]

# Variables iniciales para el temporizador
if 'time_left' not in st.session_state:
    st.session_state.time_left = 30  # Duración del juego en segundos
if 'is_running' not in st.session_state:
    st.session_state.is_running = False
if 'current_question' not in st.session_state:
    st.session_state.current_question = None
if 'current_options' not in st.session_state:
    st.session_state.current_options = None
if 'current_answer' not in st.session_state:
    st.session_state.current_answer = None

# Función para restablecer el temporizador
def reset_timer():
    st.session_state.time_left = 30
    st.session_state.is_running = False
# Función para iniciar el temporizador
def start_timer():
    st.session_state.is_running = True

# Función para generar una pregunta aleatoria
def generar_pregunta():
    pregunta = random.choice(PREGUNTAS)
    opciones = random.sample(pregunta["opciones"], len(pregunta["opciones"]))  # Mezcla las opciones
    return pregunta["pregunta"], opciones, pregunta["respuesta"]

# Función principal del juego
def pantalla_juego():
    st.write("### ¡Ejercita tus conocimientos con el juego de preguntas de álgebra lineal!")
    
    if st.button("Iniciar juego"):
        reset_timer()
        start_timer()
        st.session_state.current_question, st.session_state.current_options, st.session_state.current_answer = generar_pregunta()

    # Temporizador
    if st.session_state.is_running:
        st.write(f"Tiempo restante: {st.session_state.time_left} segundos")
        st.session_state.time_left -= 1
        if st.session_state.time_left <= 0:
            st.write("¡Tiempo agotado!")
            reset_timer()
            return

    # Mostrar pregunta y opciones
    if st.session_state.current_question:
        st.write(st.session_state.current_question)
        seleccion = st.radio("Selecciona la respuesta correcta:", st.session_state.current_options)

        # Verificar respuesta
        if st.button("Verificar respuesta"):
            if seleccion == st.session_state.current_answer:
                st.success("¡Correcto! 👍")
                if st.button("Siguiente"):
                    st.session_state.current_question, st.session_state.current_options, st.session_state.current_answer = generar_pregunta()
            else:
                st.error("Incorrecto 😞, intenta de nuevo.")
                if st.button("Volver a intentar"):
                    pass

# Llama a la pantalla del juego
if st.session_state.get('show_juega', False):
    pantalla_juego()
