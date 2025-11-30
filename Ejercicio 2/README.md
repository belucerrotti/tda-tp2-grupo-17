# Ejercicio 2 - Redes de Flujo

Este programa resuelve el problema de enviar un archivo a través de una red modelada como un grafo, donde cada arista tiene una capacidad máxima de transferencia. El objetivo es determinar el flujo máximo posible y cómo se fragmenta el archivo a través de la red.

Para resolver el problema, se utiliza la librería [NetworkX](https://networkx.org/) tanto para crear el grafo dirigido que modela la red como para calcular el flujo máximo. En particular, se emplea la función `maximum_flow`, que implementa el algoritmo de Edmonds–Karp. Este algoritmo es una versión específica del método de Ford–Fulkerson, donde los caminos aumentantes se encuentran utilizando búsqueda en anchura (BFS).

## Dependencias

- Python 3
- [NetworkX](https://networkx.org/) 

## Instalación de dependencias

```bash
pip install networkx
```

## Instrucciones para correr el programa

1. Tener Python 3 instalado.
2. Instalar la dependencia NetworkX.
3. Abrir una terminal y ubicarse dentro del directorio Ejercicio 2 (donde está el archivo ej2.py).
4. Ejecutar el archivo `ej2.py` desde la terminal:

```bash
python3 ej2.py
```

Esto mostrará por pantalla los fragmentos de archivo enviados por cada arista y el flujo máximo alcanzado en la red.
