# Función para ingresar un vector desde la entrada del usuario
def ingresar_vector(dimension, nombre="vector"):
    vector = []
    print(f"\nIngrese los elementos del {nombre}:")
    for i in range(dimension):
        valor = float(input(f"Elemento {i+1}: "))
        vector.append(valor)
    return vector

# Función para sumar vectores
def sumar_vectores(u, v):
    if len(u) != len(v):
        print("Error: Los vectores deben tener la misma dimensión para sumarse.")
        return None
    return [u[i] + v[i] for i in range(len(u))]

# Función para multiplicar una matriz por un vector
def multiplicar_matriz_vector(A, u):
    if len(A[0]) != len(u):
        print("Error: El número de columnas de la matriz debe ser igual al número de elementos del vector.")
        return None
    resultado = []
    for i in range(len(A)):
        suma = 0
        for j in range(len(A[0])):
            suma += A[i][j] * u[j]
        resultado.append(suma)
    return resultado

# Función para ingresar una matriz desde la entrada del usuario
def ingresar_matriz(filas, columnas):
    matriz = []
    print(f"\nIngrese los elementos de la matriz {filas}x{columnas}:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Elemento [{i+1},{j+1}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

# Función para verificar la propiedad de distribución A(u + v) = Au + Av
def verificar_propiedad_distribucionalidad():
    filas = int(input("Ingrese el número de filas de la matriz A: "))
    columnas = int(input("Ingrese el número de columnas de la matriz A: "))
    A = ingresar_matriz(filas, columnas)
    
    u = ingresar_vector(columnas, "u")
    v = ingresar_vector(columnas, "v")

    # Calculamos A(u + v)
    u_plus_v = sumar_vectores(u, v)
    A_u_plus_v = multiplicar_matriz_vector(A, u_plus_v)

    # Calculamos Au y Av por separado, y luego su suma
    A_u = multiplicar_matriz_vector(A, u)
    A_v = multiplicar_matriz_vector(A, v)
    A_u_plus_A_v = sumar_vectores(A_u, A_v)

    # Mostramos resultados
    print("\nResultado de A(u + v):")
    print(A_u_plus_v)
    print("\nResultado de Au + Av:")
    print(A_u_plus_A_v)

    # Verificamos igualdad entre ambos resultados
    if A_u_plus_v == A_u_plus_A_v:
        print("\nLa propiedad de distribución se verifica correctamente: A(u + v) = Au + Av")
    else:
        print("\nLa propiedad de distribución NO se verifica: A(u + v) ≠ Au + Av")

# Llamada a la función principal del módulo
verificar_propiedad_distribucionalidad()
