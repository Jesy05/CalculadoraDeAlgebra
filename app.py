<<<<<<< HEAD
import streamlit as st

st.title("Calculadora de Determinantes 2x2")

# Entradas para la matriz 2x2
a = st.number_input("Ingrese el valor de a:", value=0.0)
b = st.number_input("Ingrese el valor de b:", value=0.0)
c = st.number_input("Ingrese el valor de c:", value=0.0)
d = st.number_input("Ingrese el valor de d:", value=0.0)

if st.button("Calcular Determinante"):
    determinante = a * d - b * c
    st.write(f"El determinante de la matriz es: {determinante}")
=======
import streamlit as st

# Título de la aplicación
st.title("Calculadora de Álgebra Lineal")

# Menú de opciones
opcion = st.sidebar.selectbox("Selecciona una operación:", [
    "Eliminación por Gauss",
    "Matriz de forma escalonada",
    "Multiplicación de vectores",
    "Vectores",
    "Ecuaciones vectoriales",
    "Transpuestas",
    "Determinante",
    "Regla de Cramer",
    "Matriz inversa",
    "Espacios vectoriales",
    "Subespacio vectorial"
])

# Espacio para mostrar cada sección según la selección del usuario
if opcion == "Eliminación por Gauss":
    st.subheader("Eliminación por Gauss")
    # Aquí código para la eliminación por Gauss

def print_matrix(matrix, operations):
    print("Matriz actual:")
    for row in matrix:
        print(" ".join(f"{int(num)}" if num.is_integer() else f"{num:.2f}" for num in row))
    if operations:
        print("Operaciones realizadas:")
        print(operations[-1])  # Imprime la última operación realizada
    print()

def gaussian_elimination(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    operations = []

    for i in range(rows):
        max_row = i
        for k in range(i + 1, rows):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k
        
        # Intercambia filas si es necesario
        if max_row != i:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            operations.append(f"F{i+1} ↔ F{max_row+1}")
            print_matrix(matrix, operations)

        pivot = matrix[i][i]
        if pivot == 0:
            raise ValueError("La matriz es singular y no tiene solución única.")
        
        if pivot != 1:
            matrix[i] = [x / pivot for x in matrix[i]]
            operations.append(f"F{i+1} / {pivot}")
            print_matrix(matrix, operations)

        for j in range(rows):
            if j != i:
                factor = matrix[j][i]
                if factor != 0:
                    matrix[j] = [matrix[j][k] - factor * matrix[i][k] for k in range(cols)]
                    operations.append(f"F{j+1} → F{j+1} - ({factor}) * F{i+1}")
                    print_matrix(matrix, operations)  # Muestra después de cada operación significativa
    
    return matrix

def main():
    print("Introduce el tamaño de la matriz aumentada (n x n+1):")
    n = int(input("n: "))
    matrix = []

    print("Introduce los datos de la matriz (cada fila en una línea, separada por espacios):")
    for i in range(n):
        row = list(map(int, input(f"Fila {i+1}: ").split()))
        matrix.append(row)

    print_matrix(matrix, [])

    result = gaussian_elimination(matrix)

    print("Matriz final (matriz unitaria):")
    for row in result:
        print(" ".join(f"{int(num)}" if num.is_integer() else f"{num:.2f}" for num in row))

if __name__ == "__main__":
    main()


elif opcion == "Matriz de forma escalonada":
    st.subheader("Matriz de forma escalonada")
    # Aquí código para la forma escalonada

def imprimir_matriz(matriz, operacion=""):
    """Función para imprimir la matriz en formato bien presentado"""
    for fila in matriz:
        print(' '.join(f"{int(val)}" if val.is_integer() else f"{val:3g}" for val in fila))  # formatea cada valor de la fila, sin decimales si es entero
    if operacion:
        print("Operaciones realizadas:")
        print(operacion)
    print()  # Línea en blanco para separar cada paso claramente


def encontrar_pivote(matriz, fila, columna):
    """Busca el pivote en la columna dada, comenzando en una fila específica."""
    num_filas = len(matriz)
    while columna < len(matriz[0]):
        for i in range(fila, num_filas):
            if matriz[i][columna] != 0:
                return i, columna
        columna += 1
    return -1, -1


def intercambiar_filas(matriz, f1, f2):
    """Intercambia dos filas si no son iguales."""
    if f1 != f2:
        matriz[f1], matriz[f2] = matriz[f2], matriz[f1]
        imprimir_matriz(matriz, f"F{f1+1} <-> F{f2+1}")


def escalar_fila(matriz, fila, escalar):
    """Escala una fila por un valor escalar."""
    matriz[fila] = [x * escalar for x in matriz[fila]]
    imprimir_matriz(matriz, f"F{fila+1} / {escalar}")


def sumar_filas(matriz, fuente, destino, escalar):
    """Suma a la fila destino, la fila fuente multiplicada por un escalar."""
    matriz[destino] = [destino_val + escalar * fuente_val for destino_val, fuente_val in zip(matriz[destino], matriz[fuente])]
    imprimir_matriz(matriz, f"F{destino+1} → F{destino+1} - ({-escalar}) * F{fuente+1}")


def forma_escalonada(matriz):
    """Convierte la matriz en forma escalonada"""
    fila_pivote = 0
    for columna in range(len(matriz[0]) - 1):
        pivote, columna_pivote = encontrar_pivote(matriz, fila_pivote, columna)
        if pivote == -1:
            continue
        intercambiar_filas(matriz, fila_pivote, pivote)
        pivot_val = matriz[fila_pivote][columna_pivote]
        if pivot_val != 1 and pivot_val != 0:
            escalar_fila(matriz, fila_pivote, 1 / pivot_val)
        for i in range(len(matriz)):
            if i != fila_pivote and matriz[i][columna_pivote] != 0:
                sumar_filas(matriz, fila_pivote, i, -matriz[i][columna_pivote])
        fila_pivote += 1


def imprimir_solucion(matriz):  #matris es un paramentro. La función imprimirá la solución de una matriz en ecuaciones, determinará si el sistema tiene soluciones infinitas, una solución única o si es inconsistente.
    """Imprime la solución de la matriz en forma de ecuaciones y determina si tiene soluciones infinitas o es inconsistente.""" #docstring: comentario que se utiliza para describir el propósito de una función o un bloque de código. es mas especifica para documentar una nuncion que un comentario simple. Se pone al inicio de la funcion.
    num_variables = len(matriz[0]) - 1  #Variable amlmacena el num. de elementos en una lista. Mide (matriz[0]), lo que corresponde al número de columnas. Calcula el número de variables. Resta el -1 porque la última columna de la matriz corresponde a los términos independientes 
    soluciones = ['libre' for _ in range(num_variables)] #sols es una lista, contendra solucion para cada variable. lista por comprensión, que es una forma compacta de crear listas en Python. bucle genera una lista de longitud. "_"Es una convención en Python.
    pivotes = {}  #diccionario vacio, almacena pares clave valor. pero no permite elementos duplicados. Aquí se usa para almacenar los índices de las columnas que contienen pivotes.
    inconsistente = False #definir si el sistema de ecuaciones es inconsistente, de lo contrario sera "true"

    # Comprobamos si es inconsistente o tiene soluciones infinitas
    for i, fila in enumerate(matriz): #i es una variable de control que almacena el índice/posición actual en el bucle.
        # Verificar si el sistema es inconsistente
        if all(f == 0 for f in fila[:-1]) and fila[-1] != 0:  #Es una declaración condicional. Verifica si la condición es verdadera o falsa. el for f in fila recorre todos los valores de la fila excepto el último (que es el término independiente). and el operador logico que se cumple si ambas condiciones son verdaderas, que la ultima fila no sea igual a 0.
            print("El sistema no tiene solución debido a la inconsistencia.")
            inconsistente = True
            return
        
        # Ignorar filas completamente cero
        if all(f == 0 for f in fila[:-1]):
            continue
        
        # Detectar el pivote en cada fila
        for j in range(num_variables): #recorre las columnas de cada fila, guarda la posicion del pivote en el diccionario.
            if fila[j] != 0:
                pivotes[j] = i  # Guardamos la posición del pivote
                break #terminar la ejecución de un bucle antes de que haya recorrido todos sus elementos.

    # Comprobación si tiene soluciones infinitas
    if len(pivotes) < num_variables and not inconsistente: #Compara el número de pivotes con el número de variables.
        print("La matriz es consistente y tiene soluciones infinitas.")
    elif not inconsistente: #manejar múltiples condiciones
        print("La matriz tiene una solución única.")

    # Generar las soluciones en formato de ecuación
    ecuaciones = []
    for j in range(num_variables): #j es el índice que representa la variable en cada iteración.
        if j in pivotes: #verificar si j,variable actual está en el diccionario pivotes
            ecuacion = "" #construccion de la ecuacion, cadena vacia.
            fila = matriz[pivotes[j]]  #se obtiene la fila completa
            for k in range(num_variables): #Bucle interno. recorre los coeficientes de cada variable en la fila actual.
                coef = fila[k] #obtiene el coeficiente de la variable k en la fila actual. 
                if coef != 0: 
                    if ecuacion:
                        ecuacion += " + " if coef > 0 else " - " #va a añadir un + o un - en dependencia de <0<.
                    term = f"{int(abs(coef))}X{k+1}" if abs(coef) != 1 else f"X{k+1}"
                    ecuacion += term
            constante = int(fila[-1]) if fila[-1].is_integer() else f"{fila[-1]:.2f}"
            ecuacion += f" = {constante}"
            ecuaciones.append(ecuacion.strip('+ '))
        else:
            ecuaciones.append(f"X{j+1} es una variable libre")

    # Imprimir las soluciones en el orden correcto, omitimos el primer '=' si es necesario
    print("Soluciones en forma de ecuaciones:")
    for i, ecuacion in enumerate(ecuaciones):
        if i == 0:
            # Si la primera ecuación tiene el término '= 0' al final, lo eliminamos
            if ecuacion.endswith(" = 0"):
                ecuacion = ecuacion[:-4]
        print(ecuacion)


def main():
    """Función principal que controla el flujo del programa"""
    # Validación de entradas para número de filas y columnas
    m = int(input("Número de filas (m): "))
    n = int(input("Número de columnas (n): "))

    # Verificaciones de tamaño de matriz
    if m <= 0 or n <= 0:
        print("El número de filas y columnas debe ser mayor que cero.")
        return
    if n <= m:
        print("El número de columnas debe ser mayor que el número de filas para garantizar un sistema consistente.")
        return

    matriz = []
    for i in range(m):
        fila = list(map(float, input(f"Fila {i+1}: ").split()))
        matriz.append(fila)

    print("Matriz actual:")
    imprimir_matriz(matriz)
    forma_escalonada(matriz)
    print("Matriz final (matriz escalonada):")
    imprimir_matriz(matriz)
    imprimir_solucion(matriz)

main()


# Y así sucesivamente para cada opción...
elif opcion == "Multiplicación de vectores":
    st.subheader("Multiplicación de vectores")

elif opcion == "Vectores":
    st.subheader("Vectores")

elif opcion == "Ecuaciones vectoriales":
    st.subheader("Ecuacion vectoriales")

elif opcion == "Transpuesta":
    st.subheader("Transpuesta")

elif opcion == "Determinante":
    st.subheader("Determinante")

elif opcion == "Matriz inversa":
    st.subheader("Matriz inversa")

elif opcion == "Matriz de forma escalonada":
    st.subheader("Matriz de forma escalonada")

elif opcion == "Espacios vectoriales":
    st.subheader("Espacios vectoriales")

elif opcion == "Subespacio vectorial":
    st.subheader("Subespacio vectorial")
>>>>>>> 2cdbd5a8899e7407c6688965ecdcfac61f266447
