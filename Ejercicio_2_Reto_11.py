def longitud_matriz(matriz): # funcion que calcula la longitud de una matriz
    longitud_matriz = 0
    for i in range(len(matriz)):
        for _ in   matriz[i]:
            longitud_matriz += 1
    return longitud_matriz
def producto_entre_matrices(matriz1,matriz2): 
    matriz_resultante = []  
    if matriz1 != matriz2: # si las matrices son diferente devuelve error
        print("error")
    else: # si son iguales en la matriz_resultante se crean las listas vacias
        for i in range(len(matriz1)):
            matriz_resultante.append([])
    for a in range(len(matriz1)): # el primer for recorre las filas de la matriz
        for i in range(len(matriz1[a])): # el segundo for recorre las columnas de la matriz
            matriz_resultante[a].append(matriz1[a][i] * matriz2[a][i])
    return print(f"la matriz resutande es: \n {matriz_resultante}") # imprime la matriz resultante
def producto_escalar(matriz,escalar): 
    matriz_resultante = []  
    for i in range(len(matriz)):
        matriz_resultante.append([])
    for a in range(len(matriz)): # el primer for recorre las filas de la matriz
        for i in range(len(matriz[a])): # el segundo for recorre las columnas de la matriz
            matriz_resultante[a].append(matriz[a][i] * escalar)
    return print(f"la matriz resutande es: \n {matriz_resultante}") # imprime la matriz resultante
if __name__ == "__main__":
    matriz1 = [[1,2,3],[4,5,6],[7,8,9]] 
    matriz2 = [[1,2,3],[4,5,6],[7,8,9]]
    producto_entre_matrices(matriz1 , matriz2)
    escalar = int(input("ingrese el escalar: "))
    producto_escalar(matriz1,escalar)