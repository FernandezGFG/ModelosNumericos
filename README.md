![](https://img.shields.io/github/license/FernandezGFG/ModelosNumericos)
![](https://img.shields.io/github/last-commit/FernandezGFG/ModelosNumericos)

# Modelos numéricos en el diseño de sistemas clásicos de control para estructuras flexibles
Este proyecto se encuentra dentro del marco de trabajo del proyecto de investigación "Modelos Pedagógicos para el Aprendizaje Complejo y la Formación en
Competencias en Ciencias Básicas de Carreras Científico–Tecnológicas". Siendo la directora del proyecto la 
Mg. Ing. Silivia Raquel Raichman y Co-Director el Dr. Ing. Anibal Edmundo Mirasso.

## Resumen provisorio
Se diseñará e implementará un recurso computacional tal que, a partir de la interacción y
solución de distintos modelos matemáticos, permita comparar soluciones y seleccionar parámetros de diseño en
sistemas de control para la atenuación de vibraciones en estructuras flexibles dominadas por el primer modo
natural de vibración.

En un modelo matemático cuya respuesta está dominada por la primera autofunción solución de la ecuación
diferencial homogénea, es posible seleccionar parámetros de control de vibraciones con transformada de Laplace,
asignando polos en un modelo de un grado de libertad y aplicarlos en el sistema completo, bajo restricciones que
resultan de medir la eficiencia del sistema con fundamentos tecnológicos. A partir de un modelo de orden reducido
generado, se realiza la fase de diseño que incluye investigar cómo actúan determinados parámetros que se deben
seleccionar a los efectos de modificar la respuesta del sistema real.

La metodología descripta se implementará en un recurso computacional que permitirá seleccionar el número de
grados de libertad de los modelos de Diferencias Finitas o Elementos Finitos, el incremento temporal apropiado en
cada caso, parámetros y posiciones de polos en la función de transferencia y visualizaciones de las distintas
respuestas.

## Definiciones teóricas para una mejor comprensión
**Eigenpar**: Conjunto formado por un eigenvalor y su eigenvector asociado.

# Estado actual del proyecto
La explicación teórica del proyecto se encuentra en las distintas **Jupyter notebooks**: 

- En [main.ipynb](main.ipynb) se encuentra toda la información y código relacionado con la línea principal del proyecto. 
- [eigen.ipynb](eigen.ipynb) contiene la explicación teórica de los distintos métodos numéricos relacionados con el cálculo de eigenvalores y eigenvectores de una matriz. 

En la carpeta [project](project/) se encuentra el código fuente del proyecto. Actualmente se encuentran los siguientes archivos:

- [eigen.py](project/eigen.py): Módulo para la determinación de eigenvalores y eigenvectores de una matriz dada.

En la carpeta [docs](docs/) se encuentran archivos con mayor información del proyecto, como informes, consignas, etc.

## Módulo para la determinación de eigenvalores y eigenvectores
Actualmente se han implementado los siguientes algoritmos para su cálculo:

- Método de las potencias: para el cálculo del eigenpar mayor de la matriz A dada.
```python
# project/eigen.py
w, lmbd = power_iteration(A, err_adm=0.1, max_iter=1000)
```
- Método de las potencias inverso: para el cálculo del eigenpar menor.
*Falta documentar*
```python
# project/eigen.py
w, lmbd = inverse_iteration(A, err_adm=0.1, max_iter=1000)
```

**NOTA**: Para comprender mejor el uso de los métodos anteriores recurrir a la documentación del código.

# Licencia
[MIT License](https://github.com/FernandezGFG/ModelosNumericos/blob/master/LICENSE)
