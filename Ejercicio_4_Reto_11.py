def suma_columnas_matriz(matriz):
    columnas_resultante = [0] * len(matriz[0]) # se crea una matriz vacia con la cantidad de filas de la matriz ingresada
    resultado = 0
    for a in range(len(matriz)): # se recorre la matriz original por indice de fila
        for i in range(len(matriz[0])):
            resultado += matriz[i][a] # se agrega a la matriz resultante de forma que las filas se convierten en columnas y alrevez
        columnas_resultante[a] = (resultado)
        resultado = 0
    return columnas_resultante
if __name__ == "__main__":
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    suma_columnas = suma_columnas_matriz(matriz)
    print(f"la suma de las columnas de la matriz es: \n {suma_columnas}") # funciona :D