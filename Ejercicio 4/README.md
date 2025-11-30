# Ejercicio 4 - Algoritmos Randomizados
## Prueba de Conocimiento Cero: Esferas de Peggy y Victor

---

## Lenguaje y Requisitos

### Lenguaje de Programación
- **Python 3.8 o superior**

### Bibliotecas Requeridas
- `numpy >= 1.20.0`
- `matplotlib >= 3.3.0`

### Instalación de Dependencias

```bash
pip install numpy matplotlib
```


---

## Estructura de Archivos

```
problema4/
├── zero_knowledge_proof.py    # Programa principal
├── README.md                   # Este archivo
├── requirements.txt            # Dependencias de Python
├── sets_datos.json            # Sets de datos generados (salida)
├── resultados_peggy_sabe.json # Resultados cuando Peggy distingue (salida)
├── resultados_peggy_no_sabe.json # Resultados cuando Peggy NO distingue (salida)
├── grafico_certeza_peggy_sabe.png # Gráfico de resultados (salida)
└── grafico_certeza_peggy_no_sabe.png # Gráfico comparativo (salida)
```

---

## Instrucciones de Ejecución

### Ejecución Simple

```bash
python zero_knowledge_proof.py
```

### Descripción del Proceso

El programa ejecuta automáticamente:

1. **Cálculo teórico:** Determina cuántas repeticiones son necesarias para alcanzar 90% de certeza
2. **Generación de sets de datos:** Crea conjuntos de repeticiones [1, 2, 3, ..., 50]
3. **Experimento principal:** Ejecuta el protocolo ZKP con Peggy que SÍ puede distinguir colores
4. **Experimento comparativo:** Ejecuta el protocolo con Peggy que NO puede distinguir (para demostrar la diferencia)
5. **Generación de resultados:** Crea archivos JSON con datos detallados
6. **Visualización:** Genera gráficos de:
   - Evolución del grado de certeza vs número de repeticiones
   - Tiempo de ejecución vs número de repeticiones (análisis de complejidad)

---

## Archivos de Salida

### 1. sets_datos.json
Contiene los valores de repeticiones utilizados en el experimento.

**Formato:**
```json
{
  "repeticiones": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 40, 50]
}
```

### 2. resultados_peggy_sabe.json
Resultados del experimento cuando Peggy puede distinguir las esferas.

**Formato:**
```json
{
  "repeticiones": [1, 2, 3, ...],
  "exitos": [1, 2, 3, ...],
  "fracasos": [0, 0, 0, ...],
  "certeza": [0.5, 0.75, 0.875, ...],
  "tiempo_ejecucion": [0.0001, 0.0002, ...],
  "peggy_sabe": true
}
```

### 3. resultados_peggy_no_sabe.json
Resultados cuando Peggy NO puede distinguir (adivina aleatoriamente).

### 4. Gráficos PNG
- **grafico_certeza_peggy_sabe.png:** Visualización de certeza y tiempo de ejecución
- **grafico_certeza_peggy_no_sabe.png:** Visualización comparativa

---

