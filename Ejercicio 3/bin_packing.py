import random
import time
import json
import matplotlib.pyplot as plt
import numpy as np

def first_fit_decreasing(items):
    """
    Algoritmo First Fit Decreasing para Bin Packing.
    Garantiza una solución a lo sumo 2 veces el óptimo.
    
    Args:
        items: Lista de tamaños de objetos (0 < item < 1)
    
    Returns:
        bins: Lista de bins, cada uno con sus objetos
        num_bins: Número de bins utilizados
    """
    
    sorted_items = sorted(enumerate(items), key=lambda x: x[1], reverse=True)
    
    bins = []  # Lista de bins, cada bin es una lista de (índice, tamaño)
    bin_capacities = []  # Capacidad restante de cada bin
    
    # Para cada item, intentar colocarlo en el primer bin que tenga espacio
    for idx, size in sorted_items:
        placed = False
        
        # Buscar el primer bin con capacidad suficiente - O(m) donde m es número de bins
        for i in range(len(bins)):
            if bin_capacities[i] >= size:
                bins[i].append((idx, size))
                bin_capacities[i] -= size
                placed = True
                break
        
        # Si no cabe en ningún bin existente, crear uno nuevo
        if not placed:
            bins.append([(idx, size)])
            bin_capacities.append(1.0 - size)
    
    return bins, len(bins)


def generate_dataset(n, seed=None):
    """
    Genera un conjunto de datos de n objetos con tamaños aleatorios.
    
    Args:
        n: Número de objetos
        seed: Semilla para reproducibilidad
    
    Returns:
        Lista de tamaños de objetos
    """
    if seed is not None:
        random.seed(seed)
    
    
    items = [random.uniform(0.01, 0.99) for _ in range(n)]
    return items


def lower_bound_bins(items):
    """
    Calcula una cota inferior teórica del número óptimo de bins.
    OPT >= ceil(sum(items))
    
    Args:
        items: Lista de tamaños de objetos
    
    Returns:
        Cota inferior del número óptimo de bins
    """
    total_size = sum(items)
    return int(np.ceil(total_size))


def run_experiment(sizes, num_runs=5):
    """
    Ejecuta el algoritmo para diferentes tamaños de entrada.
    
    Args:
        sizes: Lista de tamaños de entrada a probar
        num_runs: Número de ejecuciones por tamaño para promediar
    
    Returns:
        results: Diccionario con tiempos, bins usados, etc.
    """
    results = {
        'sizes': [],
        'times': [],
        'bins_used': [],
        'lower_bounds': [],
        'ratios': []
    }
    
    for n in sizes:
        print(f"Probando con n={n}...")
        
        time_sum = 0
        bins_sum = 0
        lb_sum = 0
        
        for run in range(num_runs):
            
            items = generate_dataset(n, seed=42 + run)
            
            
            start_time = time.perf_counter()
            bins, num_bins = first_fit_decreasing(items)
            end_time = time.perf_counter()
            
            elapsed = end_time - start_time
            lb = lower_bound_bins(items)
            
            time_sum += elapsed
            bins_sum += num_bins
            lb_sum += lb
        
        
        avg_time = time_sum / num_runs
        avg_bins = bins_sum / num_runs
        avg_lb = lb_sum / num_runs
        ratio = avg_bins / avg_lb if avg_lb > 0 else 0
        
        results['sizes'].append(n)
        results['times'].append(avg_time)
        results['bins_used'].append(avg_bins)
        results['lower_bounds'].append(avg_lb)
        results['ratios'].append(ratio)
        
        print(f"  Tiempo promedio: {avg_time:.6f}s")
        print(f"  Bins promedio: {avg_bins:.2f}")
        print(f"  Cota inferior: {avg_lb:.2f}")
        print(f"  Ratio: {ratio:.3f}")
    
    return results


def save_results(results, filename='resultados.json'):
    """Guarda los resultados en formato JSON"""
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResultados guardados en {filename}")


def plot_results(results):
    """Genera gráficos de los resultados"""
    sizes = results['sizes']
    times = results['times']
    
    
    theoretical = [n * np.log(n) * times[0] / (sizes[0] * np.log(sizes[0])) 
                   for n in sizes]
    
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(sizes, times, 'bo-', label='Tiempo medido', linewidth=2, markersize=8)
    plt.plot(sizes, theoretical, 'r--', label='O(n log n) teórico', linewidth=2)
    plt.xlabel('Tamaño de entrada (n)', fontsize=12)
    plt.ylabel('Tiempo (segundos)', fontsize=12)
    plt.title('Tiempos de Ejecución vs Complejidad Teórica', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    
    
    plt.subplot(1, 2, 2)
    plt.plot(sizes, results['ratios'], 'go-', linewidth=2, markersize=8)
    plt.axhline(y=2.0, color='r', linestyle='--', label='Garantía teórica (2.0)')
    plt.xlabel('Tamaño de entrada (n)', fontsize=12)
    plt.ylabel('Ratio FFD/Cota Inferior', fontsize=12)
    plt.title('Factor de Aproximación', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.ylim([0.8, 2.2])
    
    plt.tight_layout()
    plt.savefig('grafico_resultados.png', dpi=300, bbox_inches='tight')
    print("Gráfico guardado en grafico_resultados.png")
    plt.show()


def ejemplo_seguimiento():
    """Muestra un ejemplo de seguimiento del algoritmo"""
    print("="*60)
    print("EJEMPLO DE SEGUIMIENTO")
    print("="*60)
    
    items = [0.7, 0.3, 0.5, 0.6, 0.2, 0.4]
    print(f"\nItems originales: {items}")
    print(f"Suma total: {sum(items):.2f}")
    print(f"Cota inferior teórica: {lower_bound_bins(items)} bins")
    
    
    sorted_items = sorted(enumerate(items), key=lambda x: x[1], reverse=True)
    print(f"\nItems ordenados (índice, tamaño):")
    for idx, size in sorted_items:
        print(f"  Item {idx}: {size}")
    
    print("\nProceso de asignación:")
    bins = []
    bin_capacities = []
    
    for idx, size in sorted_items:
        placed = False
        for i in range(len(bins)):
            if bin_capacities[i] >= size:
                bins[i].append((idx, size))
                bin_capacities[i] -= size
                print(f"  Item {idx} (tamaño {size}) -> Bin {i+1} (capacidad restante: {bin_capacities[i]:.2f})")
                placed = True
                break
        
        if not placed:
            bins.append([(idx, size)])
            bin_capacities.append(1.0 - size)
            print(f"  Item {idx} (tamaño {size}) -> Bin {len(bins)} NUEVO (capacidad restante: {bin_capacities[-1]:.2f})")
    
    print(f"\nResultado final: {len(bins)} bins utilizados")
    for i, bin_content in enumerate(bins):
        total = sum(size for _, size in bin_content)
        print(f"  Bin {i+1}: {bin_content} -> Total: {total:.2f}")
    
    print("="*60)


def main():
    print("ALGORITMO DE APROXIMACIÓN - BIN PACKING")
    print("First Fit Decreasing (FFD)")
    print("="*60)
    
    
    ejemplo_seguimiento()
    
    
    print("\n\nGenerando datasets...")
    sizes_to_test = [10, 50, 100, 250, 500, 1000, 2000, 5000]
    
    datasets = {}
    for n in sizes_to_test:
        datasets[f'dataset_{n}'] = generate_dataset(n, seed=42)
    
    with open('datasets.json', 'w') as f:
        json.dump(datasets, f, indent=2)
    print("Datasets guardados en datasets.json")
    
    
   
    results = run_experiment(sizes_to_test, num_runs=5)
    
   
    save_results(results)
    
    
    
    plot_results(results)
    
    


if __name__ == "__main__":
    main()