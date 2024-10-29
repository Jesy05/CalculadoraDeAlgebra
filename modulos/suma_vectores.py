def sumar_vectores(u, v):
    if len(u) != len(v):
        raise ValueError("Los vectores deben tener el mismo tamaño para ser sumados.")
    return [u[i] + v[i] for i in range(len(u))]

def mostrar_resultado_vector(vector, nombre="Resultado"):
    print(f"\nVector {nombre}: {' '.join(map(str, vector))}")
