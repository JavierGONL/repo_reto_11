<div align='center'>
<figure> <img src="https://res.cloudinary.com/dm0p2ljin/image/upload/v1714416338/error-418_dtb3ak.png" alt="" width="300" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

## Reto 11
Desarrolle la mayoría de ejercicios en clase, por cado punto resuelto en clase tendrá media décima en el examen 2 (créanme, las van a necesitar). Para cada punto cree un programa individual. Al finalizar suba todo a un repo y súbalo al canal reto_11 en slack.

1. Desarrolle un programa que permita realizar la [suma/resta de matrices](https://es.wikipedia.org/wiki/Adici%C3%B3n_matricial). El programa debe validar las condiciones necesarias para ejecutar la operación.
```python
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
```
2. Desarrolle un programa que permita realizar el [producto de matrices](https://es.wikipedia.org/wiki/Multiplicaci%C3%B3n_de_matrices). El programa debe validar las condiciones necesarias para ejecutar la operación.
```python
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
```

3. Desarrolle un programa que permita obtener la  [matriz transpuesta](https://es.wikipedia.org/wiki/Matriz_transpuesta) de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.
```python
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
```

4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.
```python
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
```

5. Desarrollar un programa que sume los elementos de una fila dada de
una matriz.
```python
def suma_filas_matriz(matriz):
    columnas_resultante = [0] * len(matriz) # se crea una matriz vacia con la cantidad de columnas de la matriz ingresada
    resultado = 0
    for a in range(len(matriz)): # se recorre la matriz original por indice de fila
        for i in range(len(matriz[0])):
            resultado += matriz[a][i] # se agrega a la matriz resultante de forma que las filas se convierten en columnas y alrevez
        columnas_resultante[a] = (resultado)
        resultado = 0
    return columnas_resultante
if __name__ == "__main__":
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    suma_columnas = suma_filas_matriz(matriz)
    print(f"la suma de las columnas de la matriz es: \n {suma_columnas}") # funciona :D
```
