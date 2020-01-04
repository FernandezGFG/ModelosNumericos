"""Determinación numérica de eigenvalores y eigenvectores

El módulo consiste en una serie de métodos numéricos para la determinación
de eigenvalores y eigenvectores de una determinada matriz. Queda a
elección del usuario el método a utilizar según su aplicación específica.
En la documentación de cada método se encuentran los casos de uso y las 
características del problema en lo que debería aplicarse.

En general, se recibe una matriz de 2 dimensiones de tipo `numpy.array`.
Dicha matriz según sea el método debera respetar una serie de 
restricciones. De no ser respetadas las limitaciones del método,
se lanzará el error correspondiente.

Para utilizar estas herramientas se requiere tener instalado el módulo
`numpy` en el entorno virtual de python donde ejecuta el script.

El archivo se puede importar como módulo, y consta de las siguientes
funciones:

    * power_iteration - Método de potencias, devuelve el máximo eigenpar de la matriz A
"""

import numpy as np
from numpy import linalg as LA

# TODO: 
#   - Manipulación de los errores
#   - Análisis teórico de eigenvectores por izquierda y por derecha

def power_iteration(A, err_adm=0.1, max_iter=1000):
    """Método de potencias para el cálculo del eigenpar mayor
    De Chapra "Métodos Numéricos para Ingenieros", página 810. Hay que tener en cuenta que 
    para algunos casos especiales el método converge al segundo autovalor mayor.

    Parameters
    ----------
    A : 2-D array
        Matriz A de la que se desea obtener el eigenpar. Dicha matriz debe ser cuadrada.
    max_iter : int, optional
        Máximo número de iteraciones antes de que el método finalice
        si no encontró un eigenpar con un error menor al admisible.
    err_adm : float, optional
        Máximo error porcentual admisible (entre o y 100%).

    Returns
    -------
    float64, 1-D array
        un float con el mayor eigenvalor de la matriz A y un 1-D array con el eigenvector aociado
    """

    # TODO: 
    #   - Establecer como parámetro opcional la cantidad máxima de iteraciones y el error admisible
    #   - Lanzar error si la matriz A recibida no es cuadrada

    err_adm = err_adm / 100 # Normalización del error a rango 0-1

    N = A.shape[0]
    lmbd = N*[1]
    w = 1

    i = 0
    while (1):
        newLmbd = A.dot(lmbd)
        newWmax = max(newLmbd)
        newLmbd = (1/newWmax) * newLmbd
        err = abs((newWmax - w)/newWmax)
        # print(err)
        if (err < err_adm or i > max_iter):
            lmbd = newLmbd
            w = newWmax
            # print("Error: " + str(err) + " - Iteración: " + str(i)) # Informe como parámetro opcional?
            break
        lmbd = newLmbd
        w = newWmax
        i += 1
        
    return w, lmbd


def inverse_iteration(A, err_adm=0.1, max_iter=1000):
    """Método de iteración inversa para el cálculo del eigenpar menor
    De Chapra "Métodos Numéricos para Ingenieros", página 812.

    Parameters
    ----------
    A : 2-D array
        Matriz A de la que se desea obtener el eigenpar. Dicha matriz debe ser cuadrada.
    max_iter : int, optional
        Máximo número de iteraciones antes de que el método finalice
        si no encontró un eigenpar con un error menor al admisible.
    err_adm : float, optional
        Máximo error porcentual admisible (entre o y 100%).

    Returns
    -------
    float64, 1-D array
        un float con el mayor eigenvalor de la matriz A y un 1-D array con el eigenvector aociado
    """

    # TODO: 
    #   - Establecer como parámetro opcional la cantidad máxima de iteraciones y el error admisible
    #   - Lanzar error si la matriz A recibida no es cuadrada

    err_adm = err_adm / 100 # Normalización del error a rango 0-1

    N = A.shape[0]

    B = LA.inv(A) # Error si la matriz A no es invertible?
    lmbd = N*[1]
    w = 1

    i = 0
    while (1):
        newLmbd = B.dot(lmbd)
        newWmax = max(newLmbd)
        newLmbd = (1/newWmax) * newLmbd
        err = abs((newWmax - w)/newWmax)
        # print(err)
        if (err < err_adm or i > max_iter):
            lmbd = newLmbd
            w = newWmax
            # print("Error: " + str(err) + " - Iteración: " + str(i)) # Informe como parámetro opcional?
            break
        lmbd = newLmbd
        w = newWmax
        i += 1

    w = max(A.dot(lmbd))
    lmbd = (1/w) * A.dot(lmbd)
    # Error si w = 0?
    #return 1/w, 1/lmbd
    return w, lmbd