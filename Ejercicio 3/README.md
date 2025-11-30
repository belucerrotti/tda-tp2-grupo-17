# PROBLEMA 3 - Algoritmos de Aproximación 

## Descripción
Implementación del algoritmo First Fit Decreasing (FFD) para el problema de Bin Packing,
con garantía de aproximación de a lo sumo 2 veces el valor óptimo.

## Requisitos

### Lenguaje
- Python 3.8 o superior

### Bibliotecas requeridas
```
numpy>=1.20.0
matplotlib>=3.3.0
```

### Instalación de dependencias
```bash
pip install numpy matplotlib
```

## Estructura de archivos
- `bin_packing.py`: Código principal del algoritmo
- `README.md`: Este archivo
- `datasets.json`: Conjuntos de datos generados
- `resultados.json`: Resultados de las ejecuciones
- `grafico_resultados.png`: Gráficos de tiempos y aproximación

## Instrucciones de ejecución

### Ejecución completa
```bash
python bin_packing.py
```

Este comando:
1. Muestra un ejemplo de seguimiento con dataset pequeño
2. Genera datasets de diferentes tamaños (10 a 5000 items)
3. Ejecuta el algoritmo sobre cada dataset
4. Guarda los resultados en JSON
5. Genera gráficos comparativos

### Salida esperada
- **datasets.json**: Conjuntos de datos utilizados
- **resultados.json**: Tiempos de ejecución, bins usados, ratios de aproximación
- **grafico_resultados.png**: Gráficos de análisis
- Salida en consola con seguimiento detallado

## Análisis del algoritmo

### Complejidad temporal
- Ordenamiento: O(n log n)
- Asignación: O(n·m) donde m ≤ n es el número de bins
- **Total: O(n²)** en el peor caso, pero típicamente O(n log n) en la práctica

### Garantía de aproximación
El algoritmo FFD garantiza que:
**FFD(I) ≤ 2·OPT(I)**

Donde FFD(I) es el número de bins usados por el algoritmo y OPT(I) es el óptimo.

## Interpretación de resultados

Los gráficos muestran:
1. **Gráfico izquierdo**: Comparación entre tiempo medido y complejidad O(n log n)
2. **Gráfico derecho**: Factor de aproximación real vs garantía teórica (línea en 2.0)