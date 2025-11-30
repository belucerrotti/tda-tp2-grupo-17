

import random
import time
import json
import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple, List, Dict


class ZeroKnowledgeProof:
    """
    Implementación de una Prueba de Conocimiento Cero para el problema
    de las esferas de colores entre Peggy y Victor.
    """
    
    def __init__(self, peggy_can_distinguish: bool = True):
        """
        Inicializa la prueba.
        
        Args:
            peggy_can_distinguish: True si Peggy realmente puede distinguir
                                   las esferas, False si está adivinando
        """
        self.peggy_can_distinguish = peggy_can_distinguish
        self.esfera_roja = "ROJA"
        self.esfera_verde = "VERDE"
    
    def una_ronda(self) -> bool:
        """
        Ejecuta una ronda del protocolo de Prueba de Conocimiento Cero.
        
       
        
        Returns:
            bool: True si Peggy responde correctamente, False si falla
        """
        # Paso 1 y 2: Victor elige aleatoriamente una esfera inicial
        esfera_inicial = random.choice([self.esfera_roja, self.esfera_verde])
        
        # Paso 3 y 4: Victor decide aleatoriamente si intercambiar
        victor_intercambio = random.choice([True, False])
        
        # Paso 5: Victor muestra la esfera resultante
        if victor_intercambio:
            esfera_final = self.esfera_verde if esfera_inicial == self.esfera_roja else self.esfera_roja
        else:
            esfera_final = esfera_inicial
        
        # Paso 6: Peggy responde
        if self.peggy_can_distinguish:
            # Peggy realmente puede distinguir los colores
            # Compara las esferas y determina si hubo intercambio
            peggy_respuesta = (esfera_inicial != esfera_final)
        else:
            # Peggy no puede distinguir, adivina aleatoriamente
            peggy_respuesta = random.choice([True, False])
        
        # Paso 7: Verificar si Peggy acerto
        return peggy_respuesta == victor_intercambio
    
    def ejecutar_protocolo(self, n_repeticiones: int) -> Tuple[int, int, float]:
        """
        Ejecuta el protocolo completo con n repeticiones.
        
        Args:
            n_repeticiones: Número de rondas a ejecutar
            
        Returns:
            Tuple con (éxitos, fracasos, grado_certeza)
        """
        exitos = 0
        fracasos = 0
        
        for _ in range(n_repeticiones):
            if self.una_ronda():
                exitos += 1
            else:
                fracasos += 1
        
        # Calcular grado de certeza de Victor
        # Si Peggy acierta todas las veces, la probabilidad de que
        # esté adivinando es (1/2)^n
        # Por lo tanto, la certeza de que realmente sabe es 1 - (1/2)^n
        if exitos == n_repeticiones:
            certeza = 1 - (0.5 ** n_repeticiones)
        else:
            
            certeza = 0.0
        
        return exitos, fracasos, certeza


def calcular_repeticiones_necesarias(certeza_objetivo: float) -> int:
    """
    Calcula cuántas repeticiones son necesarias para alcanzar
    un grado de certeza objetivo.
    
    
    Args:
        certeza_objetivo: Certeza deseada (ej: 0.90 para 90%)
        
    Returns:
        int: Número mínimo de repeticiones necesarias
    """
    import math
    n = math.ceil(math.log2(1 / (1 - certeza_objetivo)))
    return n


def generar_sets_datos() -> List[int]:
    """
    Genera los sets de datos (cantidad de repeticiones) para el experimento.
    
    Returns:
        Lista con las cantidades de repeticiones a probar
    """
    # Conjunto de repeticiones que permite observar la evolución de la certeza
    repeticiones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 40, 50]
    return repeticiones


def ejecutar_experimento(repeticiones_list: List[int], peggy_sabe: bool = True) -> Dict:
    """
    Ejecuta el experimento completo con diferentes cantidades de repeticiones.
    
    Args:
        repeticiones_list: Lista con cantidades de repeticiones a probar
        peggy_sabe: Si Peggy realmente puede distinguir las esferas
        
    Returns:
        Diccionario con los resultados del experimento
    """
    resultados = {
        'repeticiones': [],
        'exitos': [],
        'fracasos': [],
        'certeza': [],
        'tiempo_ejecucion': [],
        'peggy_sabe': peggy_sabe
    }
    
    zkp = ZeroKnowledgeProof(peggy_can_distinguish=peggy_sabe)
    
    for n_rep in repeticiones_list:
        print(f"Ejecutando {n_rep} repeticiones...")
        
        inicio = time.perf_counter()
        exitos, fracasos, certeza = zkp.ejecutar_protocolo(n_rep)
        fin = time.perf_counter()
        
        tiempo = fin - inicio
        
        resultados['repeticiones'].append(n_rep)
        resultados['exitos'].append(exitos)
        resultados['fracasos'].append(fracasos)
        resultados['certeza'].append(certeza)
        resultados['tiempo_ejecucion'].append(tiempo)
        
        print(f"  Éxitos: {exitos}/{n_rep}, Certeza: {certeza*100:.2f}%, Tiempo: {tiempo*1000:.4f}ms")
    
    return resultados


def graficar_resultados(resultados: Dict, nombre_archivo: str):
    """
    Genera los gráficos de resultados.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    
    ax1.scatter(resultados['repeticiones'], 
                [c * 100 for c in resultados['certeza']], 
                color='blue', s=50, alpha=0.6, label='Certeza alcanzada')
    
    
    x_teorico = np.linspace(1, max(resultados['repeticiones']), 100)
    y_teorico = (1 - 0.5**x_teorico) * 100
    ax1.plot(x_teorico, y_teorico, 'r--', label='Certeza teórica', linewidth=2)
    
    
    ax1.axhline(y=90, color='green', linestyle=':', label='Objetivo 90%')
    
    ax1.set_xlabel('Número de Repeticiones', fontsize=12)
    ax1.set_ylabel('Grado de Certeza (%)', fontsize=12)
    ax1.set_title('Evolución del Grado de Certeza', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_ylim([0, 105])
    
    
    ax2.scatter(resultados['repeticiones'], 
                [t * 1000 for t in resultados['tiempo_ejecucion']], 
                color='purple', s=50, alpha=0.6, label='Tiempo medido')
    
    
    z = np.polyfit(resultados['repeticiones'], 
                   [t * 1000 for t in resultados['tiempo_ejecucion']], 1)
    p = np.poly1d(z)
    ax2.plot(resultados['repeticiones'], 
             p(resultados['repeticiones']), 
             'r--', label=f'O(n) ajustado', linewidth=2)
    
    ax2.set_xlabel('Número de Repeticiones', fontsize=12)
    ax2.set_ylabel('Tiempo de Ejecución (ms)', fontsize=12)
    ax2.set_title('Complejidad Temporal', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
    print(f"\nGráfico guardado en: {nombre_archivo}")
    plt.close()


def guardar_resultados(resultados: Dict, nombre_archivo: str):
    """
    Guarda los resultados en formato JSON.
    """
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, indent=2, ensure_ascii=False)
    print(f"Resultados guardados en: {nombre_archivo}")


def main():
    """
    
    """
    print("=" * 70)
    print("PROBLEMA 4 - PRUEBA DE CONOCIMIENTO CERO")
    print("Problema de las Esferas de Peggy y Victor")
    print("=" * 70)
    
    
    n_necesario = calcular_repeticiones_necesarias(0.90)
    print(f"\nPara alcanzar 90% de certeza, se necesitan al menos {n_necesario} repeticiones")
    print(f"Certeza teórica con {n_necesario} repeticiones: {(1 - 0.5**n_necesario)*100:.2f}%")
    
    
    print("\n" + "=" * 70)
    print("GENERANDO SETS DE DATOS")
    print("=" * 70)
    repeticiones_list = generar_sets_datos()
    print(f"Sets de datos generados: {repeticiones_list}")
    
    
    with open('sets_datos.json', 'w') as f:
        json.dump({'repeticiones': repeticiones_list}, f, indent=2)
    print("Sets de datos guardados en: sets_datos.json")
    
    
    print("\n" + "=" * 70)
    print("EJECUTANDO EXPERIMENTO (Peggy SÍ distingue colores)")
    print("=" * 70)
    resultados_peggy_sabe = ejecutar_experimento(repeticiones_list, peggy_sabe=True)
    
    
    guardar_resultados(resultados_peggy_sabe, 'resultados_peggy_sabe.json')
    
    
    print("\n" + "=" * 70)
    print("GENERANDO GRÁFICOS")
    print("=" * 70)
    graficar_resultados(resultados_peggy_sabe, 'grafico_certeza_peggy_sabe.png')
    
    
    print("\n" + "=" * 70)
    print("EJECUTANDO EXPERIMENTO COMPARATIVO (Peggy NO distingue colores)")
    print("=" * 70)
    resultados_peggy_no_sabe = ejecutar_experimento(repeticiones_list, peggy_sabe=False)
    guardar_resultados(resultados_peggy_no_sabe, 'resultados_peggy_no_sabe.json')
    graficar_resultados(resultados_peggy_no_sabe, 'grafico_certeza_peggy_no_sabe.png')
    
    print("\n" + "=" * 70)
    print("EXPERIMENTO COMPLETADO")
    print("=" * 70)
    print("\nArchivos generados:")
    print("  - sets_datos.json")
    print("  - resultados_peggy_sabe.json")
    print("  - resultados_peggy_no_sabe.json")
    print("  - grafico_certeza_peggy_sabe.png")
    print("  - grafico_certeza_peggy_no_sabe.png")


if __name__ == "__main__":
    main()