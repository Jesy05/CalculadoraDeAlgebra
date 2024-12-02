import sympy as sp
import re

# Función para convertir y preparar la función matemática
def preparar_funcion(funcion):
    """
    Convierte una función matemática ingresada en formato natural a una expresión válida en SymPy.
    Reconoce funciones matemáticas en mayúsculas y minúsculas.
    """
    # Diccionario de funciones matemáticas permitidas
    funciones_math = {
        'sen': 'sin', 'sin': 'sin',  # Seno
        'cos': 'cos',  # Coseno
        'tan': 'tan',  # Tangente
        'cot': '1/tan',  # Cotangente
        'sec': '1/cos',  # Secante
        'csc': '1/sin',  # Cosecante
        'log': 'log10',  # Logaritmo base 10
        'ln': 'log',  # Logaritmo natural
        'exp': 'exp',  # Exponencial
        'sqrt': 'sqrt',  # Raíz cuadrada
        'pi': 'pi',  # Pi
        'e': 'E',  # Número de Euler
    }

    try:
        # Convertir toda la función a minúsculas para uniformidad
        funcion = funcion.lower()
        
        # Reemplazar potencias (^) por el operador SymPy (**)
        funcion = funcion.replace("^", "**").replace(' ', '')

        # Insertar multiplicaciones implícitas (e.g., 2x -> 2*x)
        funcion = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', funcion)  # Número seguido de letra
        funcion = re.sub(r'(\))(?=\d|[a-zA-Z])', r')*', funcion)  # Paréntesis seguido de letra/número

        # Reemplazar funciones trigonométricas y matemáticas
        for key, val in funciones_math.items():
            funcion = re.sub(r'\b' + key + r'\b', val, funcion)  # Reemplazo por su equivalente en SymPy

        return funcion
    except Exception as e:
        raise ValueError(f"Error al procesar la función: {e}")

# Método de la Secante
def metodo_secante(funcion, x0, x1, tolerancia, max_iter):
    """
    Implementación del método de la Secante para encontrar raíces.
    """
    resultados = []  # Lista para almacenar resultados de cada iteración
    f = sp.sympify(funcion)  # Convertir función a expresión simbólica
    x0, x1 = float(x0), float(x1)  # Asegurar que los valores iniciales sean flotantes
    ea = None  # Inicializar error relativo aproximado como None

    for i in range(max_iter):
        y0 = f.subs('x', x0)  # Evaluar f(x0)
        y1 = f.subs('x', x1)  # Evaluar f(x1)

        # Verificar si ocurre división por cero
        if y1 - y0 == 0:
            raise ZeroDivisionError("La división por cero ocurrió en el método de la secante.")

        # Calcular el siguiente valor x2
        x2 = x1 - y1 * (x1 - x0) / (y1 - y0)
        ea = abs((x2 - x1) / x2) * 100 if i > 0 else None  # Calcular error relativo aproximado

        # Guardar resultados de la iteración
        resultados.append([i + 1, x0, x1, x2, ea, y0, y1])

        # Verificar si el error está dentro de la tolerancia
        if ea is not None and ea < tolerancia:
            break

        # Actualizar valores para la siguiente iteración
        x0, x1 = x1, x2

    # Mensaje final de conclusión
    resultado_final = f"La raíz aproximada es {x2:.6f}, el error aproximado es {ea:.6f}%, el método converge a {i + 1} iteraciones."
    return resultados, resultado_final
