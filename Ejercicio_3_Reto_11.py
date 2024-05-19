def matriz_transpuesta(matriz):
    matriz_resultante = []
    for i in range(len(matriz[0])): # se crea una matriz vacia con la cantidad de filas de la matriz ingresada
        matriz_resultante.append([])
    for a in range(len(matriz)): # se recorre la matriz original por indice de fila
        for i in range(len(matriz[a])): # se recorre la matriz original por indice de columna
            matriz_resultante[i].append(matriz[a][i]) # se agrega a la matriz resultante de forma que las filas se convierten en columnas y alrevez
    return matriz_resultante
if __name__ == "__main__":
    matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[10,11,12]] # matriz de 4x3 de comprobacion
    matriz2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] # matriz de 3x4 de comprobacion
    matriz_inversa_de_1 = [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]] # matriz inversa de la matriz 1 para comprobar que la funcion esta correcta 
    matriz_inversa_de_2 = [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]] # matriz inversa de la matriz 2
    matriz_tranpuesta = matriz_transpuesta(matriz_inversa_de_1)
    print(f"la matriz transpuesta es: \n {matriz_tranpuesta}") # funciona :D