def longitud_matriz(matriz): # funcion que calcula la longitud de una matriz
    longitud_matriz = 0
    for i in range(len(matriz)):
        for _ in   matriz[i]:
            longitud_matriz += 1
    return longitud_matriz
def suma_resta_matrices(matriz1,matriz2,suma_o_resta): 
    matriz_resultante = []  
    if matriz1 != matriz2: # si las matrices son diferente devuelve error
        print("error")
    else: # si son iguales en la matriz_resultante se crean las listas vacias
        for i in range(len(matriz1)):
            matriz_resultante.append([])
    if suma_o_resta not in (1,2): # si el valor de suma_o_resta no es 1 o 2 devuelve error
        print("error")
    else:  
        for a in range(len(matriz1)): # el primer for recorre las filas de la matriz
            for i in range(len(matriz1[a])): # el segundo for recorre las columnas de la matriz
                if suma_o_resta == 1: # de resto solo se suma o se resta
                    matriz_resultante[a].append(matriz1[a][i] + matriz2[a][i])
                else:
                    matriz_resultante[a].append(matriz1[a][i] - matriz2[a][i])
    return print(f"la matriz resutande es: \n {matriz_resultante}") # imprime la matriz resultante
if __name__ == "__main__":
    matriz1 = [[1,2,3],[4,5,6],[7,8,9]] 
    matriz2 = [[1,2,3],[4,5,6],[7,8,9]]
    suma_o_resta = int(input("si quiere sumar coloque (1) o restar coloque (2): "))
    suma_resta_matrices(matriz1 , matriz2,suma_o_resta)