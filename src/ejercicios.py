# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz:list):
    """
    Recibe una lista de listas y devuelve la suma de todos sus elementos.
    Incluir el código aquí para sumar los elementos de la matriz.
    """


    suma = 0
    for filas in matriz:
        for datos in filas:
            suma += datos
    return suma
    

# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):
    """
    Recibe una lista de listas y devuelve el valor máximo.
    Incluir el código aquí para encontrar el valor máximo en la matriz.
    """

    valores=[]
    for i in matriz:
        maximo = max(i)
        valores.append(maximo)
    maximo_maximos=max(maximo)
    return maximo_maximos

        

    

# Ejercicio 3: Verificar si un número es primo
def es_primo(n):
    """
    Recibe un número y devuelve True si es primo, False en caso contrario.
    Incluir el código aquí para determinar si un número es primo.
    """
    numero = int(input("Ingrese un numero")
        contador=1
        while numero -= contador 
        contador += 1
        residuo
        lista = []
        contador.append(lista)
        if 
            lista == 2 
            print("Numero primo")
        else 
        print("Numero no primo")
                 


# Ejercicio 4: Transponer una matriz
def transponer_matriz(matriz):
    """
    Recibe una lista de listas y devuelve la matriz transpuesta.
    Incluir el código aquí para transponer la matriz.
    """
    FILAS = len(matriz)
    columnas = len(matriz[0])
    transpuesta = []
    
    for k in range(columnas):
        fila_nueva = []
        for l in range(FILASA):
            fila_nueva.append(matriz[l][k])
        transpuesta.append(fila_nueva)
    
    return transpuesta


# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):
    """
    Recibe una lista de números y devuelve una nueva lista con solo los números pares.
    Incluir el código aquí para filtrar los números pares.
    """
    lista_pares = []
    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)
    return pares



# Ejercicio 6: Contar la cantidad de palabras en una frase
def contar_palabras(frase):
    """
    Recibe una frase y devuelve el número de palabras.
    Incluir el código aquí para contar las palabras en la frase.
    """
    pass

# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):
    """
    Recibe un número y devuelve una lista con su tabla de multiplicar del 1 al 10.
    Incluir el código aquí para generar la tabla de multiplicar.
    """
    pass

# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
    """
    Recibe una lista de números y devuelve la cantidad de números negativos.
    Incluir el código aquí para contar los números negativos en la lista.
    """
    pass

# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
    """
    Recibe una lista de números y devuelve True si está ordenada de menor a mayor.
    Incluir el código aquí para verificar si la lista está ordenada.
    """
    pass

# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    """
    Recibe un texto y un desplazamiento, y devuelve el texto cifrado usando el cifrado César.
    Incluir el código aquí para cifrar el texto con el cifrado César.
    """
    pass


#Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
    def maximo_matriz(matriz:list):
       Valores = int(input("Ingrese los valores de la matriz"))
       


if __name__ == "__main__":
    main()
