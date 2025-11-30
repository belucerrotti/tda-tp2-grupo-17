# Ejercicio 1 - Ruta Óptima en Redes

Este programa resuelve el problema de enviar un archivo a través de una red dirigida (grafo), donde cada arista tiene una capacidad máxima de transferencia. El objetivo es determinar cómo fragmentar y enviar el archivo desde un nodo origen hasta un nodo destino minimizando la cantidad de enlaces utilizados. El problema se modela como un problema de programación lineal entera y se resuelve utilizando la librería PuLP.

Para resolver el problema, se definen variables de flujo y variables binarias para el uso de cada enlace, se imponen restricciones de capacidad y de conservación de flujo en cada nodo, y se minimiza la cantidad de enlaces usados. El resultado muestra por consola el estado de la solución, el número de enlaces utilizados y el flujo por cada arista utilizada.

## Dependencias

- Python 3
- [PuLP](https://pypi.org/project/PuLP/)

## Instalación de dependencias

```bash
pip install pulp
```


## Instrucciones para correr el programa

1. Tener Python 3 instalado.
2. Instalar la dependencia PuLP.
3. Abrir una terminal y ubicarse dentro del directorio `Ejercicio_1` (donde está el archivo `ej1.py`).
4. Ejecutar el archivo con:

```bash
python ej1.py
```

Esto mostrará por pantalla el estado de la solución, la cantidad de enlaces usados y los fragmentos de archivo enviados por cada arista utilizada.

## Estructura de este directorio

- `ej1.py`: script principal con la implementación.
- `resultado.txt`: Resultado obtenido al ejecutar por consola al ejecutar `ej1.py`.
