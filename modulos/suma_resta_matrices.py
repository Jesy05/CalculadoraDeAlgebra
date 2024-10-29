def sumar_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones para sumarse.")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def restar_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones para restarse.")
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
